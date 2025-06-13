# app.py - Servidor Flask
from flask import Flask, request, jsonify, Response
from flask_cors import CORS
import json
import threading
import queue
from datetime import datetime
from scraper import TransparenciaScraperTurbinado, encontrar_site_oficial

app = Flask(__name__)
CORS(app)

# Variáveis globais para controle de avaliação
current_evaluation = None
evaluation_queue = queue.Queue()
stop_evaluation = False

@app.route('/api/avaliar-transparencia', methods=['POST'])
def avaliar_transparencia():
    global current_evaluation, stop_evaluation
    
    try:
        data = request.get_json()
        
        # Valida se recebeu os dados necessários
        if not all(key in data for key in ['esfera', 'matriz', 'orgao']):
            return jsonify({'error': 'Dados insuficientes. Necessário: esfera, matriz, orgao'}), 400
            
        esfera = data['esfera']
        matriz = data['matriz']
        orgao = data['orgao']
        
        print(f"🔍 Buscando site oficial para: {orgao}")
        
        # Reset do controle de parada
        stop_evaluation = False
        
        # Encontra o site oficial através de busca
        site_oficial = encontrar_site_oficial(esfera, matriz, orgao)
        
        if not site_oficial:
            return jsonify({'error': 'Site oficial não encontrado'}), 404
            
        print(f"✅ Site encontrado: {site_oficial}")
        
        # Inicia avaliação em thread separada
        def run_evaluation():
            avaliar_transparencia_portal(site_oficial, esfera, matriz, orgao)
        
        current_evaluation = threading.Thread(target=run_evaluation)
        current_evaluation.start()
        
        return jsonify({
            'message': 'Avaliação iniciada',
            'orgao': orgao,
            'site_encontrado': site_oficial,
            'totalPerguntas': 14
        })
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/stream-resultados')
def stream_resultados():
    """Endpoint para streaming dos resultados via Server-Sent Events"""
    def generate():
        global evaluation_queue
        
        while True:
            try:
                resultado = evaluation_queue.get(timeout=1)
                
                if resultado.get('type') == 'complete':
                    yield f"event: complete\ndata: {json.dumps({'message': 'Avaliação concluída'})}\n\n"
                    break
                elif resultado.get('type') == 'error':
                    yield f"event: error\ndata: {json.dumps(resultado)}\n\n"
                    break
                elif resultado.get('type') == 'status':
                    yield f"data: {json.dumps(resultado)}\n\n"
                else:
                    yield f"data: {json.dumps(resultado)}\n\n"
                    
            except queue.Empty:
                yield f"data: {json.dumps({'type': 'heartbeat'})}\n\n"
            except Exception as e:
                yield f"event: error\ndata: {json.dumps({'message': str(e)})}\n\n"
                break
    
    return Response(
        generate(),
        mimetype='text/event-stream',
        headers={
            'Cache-Control': 'no-cache',
            'Connection': 'keep-alive',
            'Access-Control-Allow-Origin': '*'
        }
    )

@app.route('/api/cancelar-avaliacao', methods=['POST'])
def cancelar_avaliacao():
    """Cancela a avaliação em andamento"""
    global stop_evaluation, current_evaluation
    
    stop_evaluation = True
    
    if current_evaluation and current_evaluation.is_alive():
        current_evaluation.join(timeout=5)
    
    return jsonify({'message': 'Avaliação cancelada'})

@app.route('/api/health')
def health_check():
    """Endpoint para verificar se a API está funcionando"""
    return jsonify({
        'status': 'ok',
        'message': 'Sistema funcionando',
        'timestamp': datetime.now().isoformat()
    })

def avaliar_transparencia_portal(url, esfera, matriz, orgao):
    """Função principal que coordena a avaliação"""
    global stop_evaluation, evaluation_queue
    
    # Lista de critérios
    criterios = [
        {
            "id": "1.1",
            "nome": "Estrutura Organizacional",
            "pergunta": "O portal disponibiliza a estrutura organizacional da entidade (organograma)?",
            "termos_busca": ["organograma", "estrutura organizacional", "hierarquia", "organização"]
        },
        {
            "id": "1.2",
            "nome": "Competências",
            "pergunta": "O portal disponibiliza as competências de cada unidade?",
            "termos_busca": ["competências", "atribuições", "responsabilidades", "funções"]
        },
        {
            "id": "1.3",
            "nome": "Base Jurídica",
            "pergunta": "O portal disponibiliza a base jurídica da estrutura organizacional?",
            "termos_busca": ["base jurídica", "base legal", "legislação", "lei", "decreto"]
        },
        {
            "id": "1.4",
            "nome": "Lista de Autoridades",
            "pergunta": "O portal disponibiliza a lista dos principais cargos e seus ocupantes?",
            "termos_busca": ["autoridades", "dirigentes", "gestores", "secretários", "diretores"]
        },
        {
            "id": "2.1",
            "nome": "Agenda de Autoridades",
            "pergunta": "O portal disponibiliza agenda de autoridades?",
            "termos_busca": ["agenda", "compromissos", "eventos", "reuniões", "audiências"]
        },
        {
            "id": "2.2",
            "nome": "Horários de Atendimento",
            "pergunta": "O portal disponibiliza horários de atendimento?",
            "termos_busca": ["horário de atendimento", "funcionamento", "expediente"]
        },
        {
            "id": "2.3",
            "nome": "Contatos",
            "pergunta": "O portal disponibiliza telefones, endereços e e-mails?",
            "termos_busca": ["contato", "telefone", "endereço", "e-mail", "fale conosco"]
        },
        {
            "id": "3.1",
            "nome": "Receitas",
            "pergunta": "O portal disponibiliza informações sobre receitas?",
            "termos_busca": ["receitas", "arrecadação", "recursos", "orçamento"]
        },
        {
            "id": "4.1",
            "nome": "Despesas",
            "pergunta": "O portal disponibiliza informações sobre despesas?",
            "termos_busca": ["despesas", "gastos", "pagamentos", "empenhos"]
        },
        {
            "id": "8.1",
            "nome": "Licitações",
            "pergunta": "O portal disponibiliza informações sobre licitações?",
            "termos_busca": ["licitações", "licitação", "pregão", "concorrência", "editais"]
        },
        {
            "id": "9.1",
            "nome": "Contratos",
            "pergunta": "O portal disponibiliza informações sobre contratos?",
            "termos_busca": ["contratos", "contratações", "termos aditivos", "fornecedores"]
        },
        {
            "id": "6.1",
            "nome": "Servidores",
            "pergunta": "O portal disponibiliza informações sobre servidores?",
            "termos_busca": ["servidores", "funcionários", "folha de pagamento", "remuneração"]
        },
        {
            "id": "12.1",
            "nome": "SIC Físico",
            "pergunta": "O portal indica a existência de SIC físico?",
            "termos_busca": ["sic", "serviço de informação ao cidadão", "atendimento presencial"]
        },
        {
            "id": "12.2",
            "nome": "e-SIC",
            "pergunta": "O portal disponibiliza e-SIC?",
            "termos_busca": ["e-sic", "esic", "sic eletrônico", "pedido de informação"]
        }
    ]
    
    scraper = TransparenciaScraperTurbinado(headless=True)
    
    try:
        print(f"🔍 Avaliando transparência de: {orgao}")
        
        evaluation_queue.put({
            'type': 'status',
            'message': f'Iniciando avaliação de {len(criterios)} critérios...',
            'progress': 0
        })
        
        for i, criterio in enumerate(criterios):
            if stop_evaluation:
                break
                
            print(f"📋 Critério {i+1}/{len(criterios)}: {criterio['nome']}")
            
            evaluation_queue.put({
                'type': 'status',
                'message': f'Avaliando: {criterio["nome"]}',
                'progress': int((i / len(criterios)) * 100)
            })
            
            resultado = scraper.avaliar_criterio(url, criterio)
            resultado['id'] = criterio['id']
            
            evaluation_queue.put(resultado)
            
    except Exception as e:
        evaluation_queue.put({
            'type': 'error',
            'message': f'Erro: {str(e)}'
        })
    finally:
        scraper.driver.quit()
        evaluation_queue.put({'type': 'complete'})

if __name__ == '__main__':
    print("🚀 Servidor iniciado!")
    print("📍 http://localhost:5000")
    app.run(debug=True, host='0.0.0.0', port=5000)
