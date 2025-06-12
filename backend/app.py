# app.py - Versão completa
from flask import Flask, request, jsonify, Response, send_from_directory
from flask_cors import CORS
import scraper
import queue
import threading
import json
import time
import os
import pandas as pd
from datetime import datetime, timedelta, date
from utils import save_criteria_json
import requests
from bs4 import BeautifulSoup
from known_urls import get_known_url
from amazonas_portals import get_amazonas_url, get_all_amazonas_municipalities

# Configuração da aplicação
app = Flask(__name__, 
            static_folder='../sapt-frontend/build', 
            static_url_path='')
CORS(app)

# ===== ROTAS PARA SERVIR O REACT (DEVEM VIR PRIMEIRO) =====
@app.route('/')
def index():
    return send_from_directory(app.static_folder, 'index.html')

# Rota catch-all para o React Router
@app.route('/<path:path>')
def serve(path):
    # Se for uma rota da API, deixa passar
    if path.startswith('api/'):
        return jsonify({'error': 'Not found'}), 404
    
    # Se o arquivo existe no build, serve ele
    if os.path.exists(os.path.join(app.static_folder, path)):
        return send_from_directory(app.static_folder, path)
    
    # Caso contrário, retorna o index.html (para o React Router funcionar)
    return send_from_directory(app.static_folder, 'index.html')

# ===== SUAS ROTAS DE API EXISTENTES =====

# Fila global para comunicação entre threads
result_queue = queue.Queue()

@app.route('/api/analyze', methods=['POST'])
def analyze():
    data = request.json
    url = data.get('url')
    
    if not url:
        return jsonify({"error": "URL é obrigatória"}), 400
    
    # Cria um ID único para esta análise
    analysis_id = str(time.time())
    
    # Inicia a análise em uma thread separada
    thread = threading.Thread(target=run_analysis, args=(url, analysis_id))
    thread.start()
    
    return jsonify({"analysis_id": analysis_id, "status": "started"})

def run_analysis(url, analysis_id):
    try:
        # Executa o scraper
        results = scraper.analyze_portal(url)
        
        # Adiciona o ID da análise aos resultados
        results['analysis_id'] = analysis_id
        results['status'] = 'completed'
        
        # Coloca os resultados na fila
        result_queue.put(results)
    except Exception as e:
        error_result = {
            'analysis_id': analysis_id,
            'status': 'error',
            'error': str(e)
        }
        result_queue.put(error_result)

@app.route('/api/results/<analysis_id>')
def get_results(analysis_id):
    # Procura pelos resultados na fila
    results = []
    while not result_queue.empty():
        results.append(result_queue.get())
    
    # Procura pelo resultado específico
    for result in results:
        if result.get('analysis_id') == analysis_id:
            return jsonify(result)
        else:
            # Recoloca na fila se não for o resultado procurado
            result_queue.put(result)
    
    return jsonify({"status": "processing"}), 202

@app.route('/api/stream-analysis', methods=['POST'])
def stream_analysis():
    data = request.json
    url = data.get('url')
    
    if not url:
        return jsonify({"error": "URL é obrigatória"}), 400
    
    def generate():
        try:
            # Envia status inicial
            yield f"data: {json.dumps({'status': 'starting', 'message': 'Iniciando análise...'})}\n\n"
            
            # Executa o scraper com streaming
            for update in scraper.analyze_portal_stream(url):
                yield f"data: {json.dumps(update)}\n\n"
                time.sleep(0.1)  # Pequeno delay para não sobrecarregar
                
        except Exception as e:
            yield f"data: {json.dumps({'status': 'error', 'error': str(e)})}\n\n"
    
    return Response(generate(), mimetype='text/event-stream')

@app.route('/api/save-criteria', methods=['POST'])
def save_criteria():
    try:
        data = request.json
        if not data:
            return jsonify({"error": "Dados não fornecidos"}), 400
        
        # Salva os critérios usando a função do utils.py
        filepath = save_criteria_json(data)
        
        return jsonify({
            "success": True,
            "message": "Critérios salvos com sucesso",
            "file": filepath
        })
    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500

@app.route('/api/export-results', methods=['POST'])
def export_results():
    try:
        data = request.json
        results = data.get('results', {})
        format_type = data.get('format', 'excel')
        
        if format_type == 'excel':
            # Criar DataFrame com os resultados
            df_data = []
            
            # Adicionar informações gerais
            df_data.append({
                'Categoria': 'Informações Gerais',
                'Item': 'URL',
                'Valor': results.get('url', ''),
                'Pontuação': ''
            })
            df_data.append({
                'Categoria': 'Informações Gerais',
                'Item': 'Data da Análise',
                'Valor': results.get('timestamp', ''),
                'Pontuação': ''
            })
            df_data.append({
                'Categoria': 'Informações Gerais',
                'Item': 'Pontuação Total',
                'Valor': '',
                'Pontuação': f"{results.get('score', 0):.1f}%"
            })
            
            # Adicionar critérios
            criteria = results.get('criteria', {})
            for category, items in criteria.items():
                for item in items:
                    df_data.append({
                        'Categoria': category,
                        'Item': item['name'],
                        'Valor': 'Sim' if item['found'] else 'Não',
                        'Pontuação': f"{item['score']:.1f}" if item['found'] else '0.0'
                    })
            
            # Criar DataFrame
            df = pd.DataFrame(df_data)
            
            # Salvar como Excel
            filename = f"analise_portal_{datetime.now().strftime('%Y%m%d_%H%M%S')}.xlsx"
            filepath = os.path.join('exports', filename)
            
            # Criar diretório se não existir
            os.makedirs('exports', exist_ok=True)
            
            # Salvar Excel com formatação
            with pd.ExcelWriter(filepath, engine='openpyxl') as writer:
                df.to_excel(writer, sheet_name='Análise', index=False)
                
                # Ajustar largura das colunas
                worksheet = writer.sheets['Análise']
                for column in df:
                    column_width = max(df[column].astype(str).map(len).max(), len(column))
                    col_idx = df.columns.get_loc(column)
                    worksheet.column_dimensions[chr(65 + col_idx)].width = column_width + 2
            
            return jsonify({
                "success": True,
                "filename": filename,
                "message": "Arquivo exportado com sucesso"
            })
            
        elif format_type == 'pdf':
            # Implementar exportação PDF se necessário
            return jsonify({
                "success": False,
                "error": "Exportação PDF ainda não implementada"
            }), 501
            
    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500

@app.route('/api/health')
def health():
    return jsonify({"status": "healthy", "timestamp": datetime.now().isoformat()})

# Nova rota para buscar URL conhecida
@app.route('/api/known-url/<state>/<city>')
def get_known_url_route(state, city):
    """Busca URL conhecida para um município"""
    url = get_known_url(state, city)
    if url:
        return jsonify({"url": url, "found": True})
    else:
        return jsonify({"url": None, "found": False})

# Nova rota para buscar URL do Amazonas
@app.route('/api/amazonas-url/<municipio>')
def get_amazonas_url_route(municipio):
    """Busca URL do portal de transparência de um município do Amazonas"""
    try:
        url = get_amazonas_url(municipio)
        if url:
            return jsonify({
                "url": url,
                "found": True,
                "municipio": municipio
            })
        else:
            return jsonify({
                "url": None,
                "found": False,
                "municipio": municipio,
                "message": "URL não encontrada para este município"
            })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Nova rota para listar todos os municípios do Amazonas
@app.route('/api/amazonas-municipios')
def list_amazonas_municipios():
    """Lista todos os municípios do Amazonas disponíveis"""
    try:
        municipios = get_all_amazonas_municipalities()
        return jsonify({
            "municipios": municipios,
            "total": len(municipios)
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# NO FINAL DO ARQUIVO:
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)