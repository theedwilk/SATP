# ================================
# ARQUIVO ÚNICO: app.py
# ================================
import pandas as pd
import numpy as np
from datetime import datetime
import streamlit as st
import requests
from urllib.parse import urlparse, urljoin
import time
from bs4 import BeautifulSoup
import re
import warnings
import json
from dataclasses import dataclass
from typing import Dict, List, Tuple, Optional
from io import BytesIO

# ================================
# IMPORTS DOS DADOS DOS ÓRGÃOS
# ================================
from orgaos_data import ORGAOS_DATA

# ================================
# IMPORTS DOS CRITÉRIOS MODULADOS
# ================================
try:
    from criterios_comum import CRITERIOS_TRANSPARENCIA
    from criterios_comum_exceto_estatais_independentes import CRITERIOS_COMUM_EXCETO_ESTATAIS_INDEPENDENTES
    from criterios_comum_exceto_estatais import CRITERIOS_COMUM_EXCETO_ESTATAIS
    from criterios_executivo import CRITERIOS_EXECUTIVO
    from criterios_executivo_consorcios import CRITERIOS_EXECUTIVO_CONSORCIOS
    from criterios_legislativo import CRITERIOS_LEGISLATIVO
    from criterios_judiciario import CRITERIOS_JUDICIARIO
    from criterios_tribunal_contas import CRITERIOS_TRIBUNAL_CONTAS
    from criterios_ministerio_publico import CRITERIOS_MINISTERIO_PUBLICO
    from criterios_defensoria import CRITERIOS_DEFENSORIA
    from criterios_consorcios_publicos import CRITERIOS_CONSORCIOS_PUBLICOS
    from criterios_estatais import CRITERIOS_ESTATAIS
    from criterios_estatais_independentes import CRITERIOS_ESTATAIS_INDEPENDENTES
except ImportError as e:
    st.error(f"Erro ao importar módulos de critérios: {e}")
    st.stop()

warnings.filterwarnings('ignore') # Ignora warnings de SSL, etc.

# Configuração da página
st.set_page_config(
    page_title="Sistema de Avaliação de Portais de Transparência",
    page_icon="🔍",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# CSS customizado (SEU CSS + alguns estilos novos)
st.markdown("""
<style>
    [data-testid="stSidebar"] {
        display: none;
    }
    .main-container {
        max-width: 800px;
        margin: 0 auto;
        padding: 2rem;
    }
    .main-title {
        text-align: center;
        color: #1e3a8a;
        font-size: 2.5rem;
        font-weight: bold;
        margin-bottom: 3rem;
    }
    .stSelectbox {
        margin-bottom: 1.5rem;
    }
    .stButton > button {
        background-color: #1e3a8a;
        color: white;
        font-size: 1.2rem;
        padding: 0.75rem 3rem;
        border-radius: 8px;
        border: none;
        margin-top: 2rem;
        width: 100%;
    }
    .stButton > button:hover {
        background-color: #1e40af;
    }
    /* Estilos novos para auditoria */
    .criterio-card {
        border: 1px solid #e5e7eb;
        border-radius: 8px;
        padding: 1rem;
        margin: 0.5rem 0;
        background-color: #f9fafb;
    }
    .criterio-conforme {
        border-left: 4px solid #10b981;
    }
    .criterio-nao-conforme {
        border-left: 4px solid #ef4444;
    }
    .link-evidencia {
        background-color: #dbeafe;
        padding: 0.5rem;
        border-radius: 4px;
        margin-top: 0.5rem;
        word-break: break-all; /* Quebra a linha para URLs longas */
    }
    /* Scroll suave */
    html {
        scroll-behavior: smooth;
    }
    /* Seções bem definidas */
    .section-divider {
        border-top: 2px solid #e5e7eb;
        margin: 2rem 0;
    }
</style>
""", unsafe_allow_html=True)

def adicionar_botao_topo():
    """Adiciona um botão flutuante para voltar ao topo."""
    st.markdown("""
    <style>
    /* Botão flutuante para voltar ao topo */
    .botao-topo {
        position: fixed;
        bottom: 20px;
        right: 20px;
        width: 60px;
        height: 60px;
        background-color: #1e40af;
        color: white;
        border: none;
        border-radius: 50%;
        cursor: pointer;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 24px;
        font-weight: bold;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
        z-index: 1000;
        opacity: 0;
        pointer-events: none;
        transition: opacity 0.3s, transform 0.3s;
        text-decoration: none;
    }
    .botao-topo.show {
        opacity: 1;
        pointer-events: all;
        transform: scale(1);
    }
    .botao-topo:hover {
        background-color: #2563eb;
        transform: translateY(-5px);
    }
    /* Animação suave ao scroll */
    html {
        scroll-behavior: smooth;
    }
    /* Seções bem definidas */
    .section-divider {
        border-top: 2px solid #e5e7eb;
        margin: 2rem 0;
    }
    </style>
    <a href="#top" class="botao-topo" id="btnTopo" title="Voltar ao topo">↑</a>
    <script>
    // Mostrar/esconder o botão com base no scroll
    const botaoTopo = document.getElementById('btnTopo');
    window.onscroll = function() {
        if (document.body.scrollTop > 100 || document.documentElement.scrollTop > 100) {
            botaoTopo.classList.add('show');
        } else {
            botaoTopo.classList.remove('show');
        }
    };
    </script>
    """, unsafe_allow_html=True)

# ================================
# FUNÇÃO PARA APLICAR FILTROS DE CRITÉRIOS
# ================================
def obter_criterios_por_poder(poder_selecionado, esfera_selecionada=""):
    """
    Obtém os critérios aplicáveis baseado no poder selecionado
    
    Args:
        poder_selecionado (str): Poder selecionado pelo usuário
        esfera_selecionada (str): Esfera selecionada (Estadual/Municipal)
        
    Returns:
        dict: Dicionário com todos os critérios aplicáveis
    """
    criterios_aplicaveis = {}
    
    # Sempre adiciona critérios comuns a todos
    criterios_aplicaveis.update(CRITERIOS_TRANSPARENCIA)
    
    # Mapeia os poderes para aplicar filtros corretos
    poder_normalizado = poder_selecionado.lower().replace(" ", "_")
    
    if "executivo" in poder_normalizado:
        # Critérios comuns exceto estatais independentes
        criterios_aplicaveis.update(CRITERIOS_COMUM_EXCETO_ESTATAIS_INDEPENDENTES)
        # Critérios comuns exceto estatais
        criterios_aplicaveis.update(CRITERIOS_COMUM_EXCETO_ESTATAIS)
        # Critérios específicos do executivo
        criterios_aplicaveis.update(CRITERIOS_EXECUTIVO)
        # Critérios executivo e consórcios
        criterios_aplicaveis.update(CRITERIOS_EXECUTIVO_CONSORCIOS)
        
    elif "legislativo" in poder_normalizado:
        # Critérios comuns exceto estatais independentes
        criterios_aplicaveis.update(CRITERIOS_COMUM_EXCETO_ESTATAIS_INDEPENDENTES)
        # Critérios comuns exceto estatais
        criterios_aplicaveis.update(CRITERIOS_COMUM_EXCETO_ESTATAIS)
        # Critérios específicos do legislativo
        criterios_aplicaveis.update(CRITERIOS_LEGISLATIVO)
        
    elif "judiciário" in poder_normalizado or "judiciario" in poder_normalizado:
        # Critérios comuns exceto estatais independentes
        criterios_aplicaveis.update(CRITERIOS_COMUM_EXCETO_ESTATAIS_INDEPENDENTES)
        # Critérios comuns exceto estatais
        criterios_aplicaveis.update(CRITERIOS_COMUM_EXCETO_ESTATAIS)
        # Critérios específicos do judiciário
        criterios_aplicaveis.update(CRITERIOS_JUDICIARIO)
        
    elif "tribunal" in poder_normalizado and "contas" in poder_normalizado:
        # Critérios comuns exceto estatais independentes
        criterios_aplicaveis.update(CRITERIOS_COMUM_EXCETO_ESTATAIS_INDEPENDENTES)
        # Critérios comuns exceto estatais
        criterios_aplicaveis.update(CRITERIOS_COMUM_EXCETO_ESTATAIS)
        # Critérios específicos do tribunal de contas
        criterios_aplicaveis.update(CRITERIOS_TRIBUNAL_CONTAS)
        
    elif "ministério" in poder_normalizado and "público" in poder_normalizado:
        # Critérios comuns exceto estatais independentes
        criterios_aplicaveis.update(CRITERIOS_COMUM_EXCETO_ESTATAIS_INDEPENDENTES)
        # Critérios comuns exceto estatais
        criterios_aplicaveis.update(CRITERIOS_COMUM_EXCETO_ESTATAIS)
        # Critérios específicos do ministério público
        criterios_aplicaveis.update(CRITERIOS_MINISTERIO_PUBLICO)
        
    elif "defensoria" in poder_normalizado:
        # Critérios comuns exceto estatais independentes
        criterios_aplicaveis.update(CRITERIOS_COMUM_EXCETO_ESTATAIS_INDEPENDENTES)
        # Critérios comuns exceto estatais
        criterios_aplicaveis.update(CRITERIOS_COMUM_EXCETO_ESTATAIS)
        # Critérios específicos da defensoria
        criterios_aplicaveis.update(CRITERIOS_DEFENSORIA)
        
    elif "consórcios" in poder_normalizado or "consórcio" in poder_normalizado:
        # Critérios comuns exceto estatais independentes
        criterios_aplicaveis.update(CRITERIOS_COMUM_EXCETO_ESTATAIS_INDEPENDENTES)
        # Critérios executivo e consórcios
        criterios_aplicaveis.update(CRITERIOS_EXECUTIVO_CONSORCIOS)
        # Critérios específicos dos consórcios
        criterios_aplicaveis.update(CRITERIOS_CONSORCIOS_PUBLICOS)
        
    elif "estatais" in poder_normalizado:
        # Verifica se é estatal independente
        if "independente" in poder_normalizado:
            # Apenas critérios comuns e específicos de estatais independentes
            criterios_aplicaveis.update(CRITERIOS_ESTATAIS_INDEPENDENTES)
        else:
            # Critérios comuns exceto estatais independentes
            criterios_aplicaveis.update(CRITERIOS_COMUM_EXCETO_ESTATAIS_INDEPENDENTES)
            # Critérios específicos das estatais
            criterios_aplicaveis.update(CRITERIOS_ESTATAIS)
    
    return criterios_aplicaveis

def converter_criterios_para_auditoria(criterios_dict):
    """
    Converte o dicionário de critérios modulados para o formato da classe AuditoriaTransparenciaCriterios
    
    Args:
        criterios_dict (dict): Dicionário de critérios modulados
        
    Returns:
        dict: Dicionário no formato esperado pela classe de auditoria
    """
    criterios_auditoria = {}
    
    for id_criterio, dados in criterios_dict.items():
        criterios_auditoria[id_criterio] = CriterioAuditoria(
            dimensao=dados['dimensao'],
            id_criterio=dados['id'],
            criterio=dados['criterio'],
            classificacao=dados['classificacao'],
            fundamentacao=dados['fundamentacao'],
            palavras_chave=dados['palavras_chave'],
            seletores_especificos=gerar_seletores_automaticos(dados['palavras_chave']),
            validacao_adicional=None
        )
    
    return criterios_auditoria

def gerar_seletores_automaticos(palavras_chave):
    """
    Gera seletores CSS automaticamente baseado nas palavras-chave
    
    Args:
        palavras_chave (list): Lista de palavras-chave
        
    Returns:
        list: Lista de seletores CSS
    """
    seletores = [
        "title", "meta[name='description']", "header", ".header", "#header",
        "nav a", "menu a", ".menu a", ".nav a", "a", "h1", "h2", "h3",
        "footer a", ".footer a", "main", ".main", "#main"
    ]
    
    # Adiciona seletores específicos baseados nas palavras-chave
    for palavra in palavras_chave:
        palavra_limpa = palavra.replace(" ", "-").lower()
        seletores.extend([
            f"a[href*='{palavra_limpa}']",
            f".{palavra_limpa}",
            f"#{palavra_limpa}",
            f"a:contains('{palavra.title()}')"
        ])
    
    return seletores

# ================================
# CLASSES PARA AUDITORIA (NOVAS)
# ================================
@dataclass
class CriterioAuditoria:
    dimensao: str
    id_criterio: str
    criterio: str
    classificacao: str
    fundamentacao: str
    palavras_chave: List[str]
    seletores_especificos: List[str]
    validacao_adicional: Optional[str] = None

@dataclass
class ResultadoCriterio:
    dimensao: str
    id_criterio: str
    criterio: str
    classificacao: str
    fundamentacao: str
    disponivel: bool
    link_evidencia: str
    texto_evidencia: str
    metodo_encontrado: str
    score_relevancia: int
    timestamp: str
    observacoes: str

class AuditoriaTransparenciaCriterios:
    """Sistema de auditoria integrado com critérios modulados"""
    def __init__(self, criterios_customizados=None):
        # Se critérios customizados forem fornecidos, usa eles; senão usa os padrão
        if criterios_customizados:
            self.criterios = criterios_customizados
        else:
            self.criterios = self._definir_criterios_auditoria()
        
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'pt-BR,pt;q=0.9,en;q=0.8',
            'Connection': 'keep-alive'
        }
        self.session = requests.Session()
        self.session.headers.update(self.headers)
        self.timeout = 15 # Tempo limite para requisições

    def _definir_criterios_auditoria(self) -> Dict[str, CriterioAuditoria]:
        """Define todos os critérios baseados na legislação"""
        criterios = {
        # ===== INFORMAÇÕES PRIORITÁRIAS =====
        "1.1": CriterioAuditoria(
            dimensao="Informações Prioritárias",
            id_criterio="1.1",
            criterio="Possui sítio oficial próprio na internet?",
            classificacao="Essencial",
            fundamentacao="Art. 48, §1º, II, da LC nº 101/00 e arts. 3º, III, 6º, I, e 8º, §2º, da Lei nº 12.527/2011 – LAI.",
            palavras_chave=["site oficial", "portal oficial", "página oficial", "sítio oficial", "website oficial", "governo", "prefeitura", "câmara", "tribunal", "ministério público", "defensoria"],
            seletores_especificos=["title", "meta[name='description']", "header", ".header", "#header", ".logo", "#logo", "h1", "h2"]
        ),
        "1.2": CriterioAuditoria(
            dimensao="Informações Prioritárias",
            id_criterio="1.2",
            criterio="Possui portal da transparência próprio ou compartilhado na internet?",
            classificacao="Essencial",
            fundamentacao="Art. 48, §1º, II, da LC nº 101/00 e arts. 3º, III, 6º, I, e 8º, §2º, da Lei nº 12.527/2011 – LAI.",
            palavras_chave=["portal da transparência", "transparência", "portal transparência", "acesso à informação", "transparencia", "dados abertos"],
            seletores_especificos=["a[href*='transparencia']", "a[href*='portal-transparencia']", "a[href*='acesso-informacao']", "a[href*='dados-abertos']", ".transparencia", "#transparencia", ".portal-transparencia", "h1", "h2", "title"]
        ),
        # Adicione outros critérios conforme necessário...
        }
        return criterios

    def _fetch_page(self, url: str) -> Optional[BeautifulSoup]:
        """Busca o conteúdo de uma URL e retorna um objeto BeautifulSoup."""
        if not url:
            return None
        try:
            # Adiciona um pequeno delay para evitar sobrecarregar o servidor
            time.sleep(0.5)
            response = self.session.get(url, timeout=self.timeout, verify=False)
            response.raise_for_status() # Lança exceção para status codes ruins (4xx ou 5xx)
            return BeautifulSoup(response.content, 'html.parser')
        except requests.exceptions.RequestException as e:
            st.warning(f"Falha ao acessar {url}: {e}")
            return None

    def _is_same_domain(self, base_url: str, target_url: str) -> bool:
        """Verifica se duas URLs pertencem ao mesmo domínio."""
        try:
            return urlparse(base_url).netloc == urlparse(target_url).netloc
        except:
            return False

    def _verificar_criterio(self, base_url: str, criterio: CriterioAuditoria, main_site_url: Optional[str] = None) -> ResultadoCriterio:
        """Verifica a disponibilidade de um critério no portal."""
        url_to_check = base_url
        if criterio.validacao_adicional == "verificar_visibilidade_capa" and main_site_url:
             url_to_check = main_site_url # Para o critério 1.3, verifica o site principal

        soup = self._fetch_page(url_to_check)
        disponivel = False
        link_evidencia = ""
        texto_evidencia = ""
        metodo_encontrado = "Não encontrado"
        score_relevancia = 0
        observacoes = ""

        if soup:
            # 1. Buscar por seletores específicos e palavras-chave
            for selector in criterio.seletores_especificos:
                try:
                    elements = soup.select(selector)
                    for element in elements:
                        text = element.get_text().lower().strip()
                        href = element.get('href', '').lower().strip()

                        # Prioriza links e texto em elementos específicos
                        if any(kw in text or kw in href for kw in criterio.palavras_chave):
                            disponivel = True
                            link_evidencia = urljoin(url_to_check, href) if href else url_to_check
                            texto_evidencia = text[:200] + "..." if len(text) > 200 else text
                            metodo_encontrado = f"Seletor: {selector}"
                            score_relevancia = 100 if selector in ["header a", ".menu a", "nav a"] else 80 # Maior score para elementos de menu/cabeçalho
                            observacoes = f"Encontrado via seletor '{selector}' e palavras-chave."
                            # Se encontrou via seletor prioritário, pode parar
                            if score_relevancia == 100:
                                break
                except Exception as e:
                    # Ignora erros de seletores inválidos
                    pass
                if disponivel and score_relevancia == 100: break # Sai do loop de seletores se encontrou com alta relevância

            # 2. Buscar por palavras-chave no texto geral da página (se não encontrado via seletores prioritários)
            if not disponivel or score_relevancia < 80:
                text_content = soup.get_text().lower()
                for kw in criterio.palavras_chave:
                    if kw in text_content:
                        disponivel = True
                        link_evidencia = url_to_check
                        # Tenta encontrar o trecho com a palavra-chave para evidência
                        match = re.search(f'.{{0,50}}{re.escape(kw)}.{0,50}', text_content)
                        texto_evidencia = match.group(0).strip() if match else text_content[:200] + "..."
                        metodo_encontrado = "Texto geral da página"
                        score_relevancia = 50 # Score menor para texto geral
                        observacoes = f"Encontrado via palavra-chave '{kw}' no texto geral."
                        break # Encontrou uma palavra-chave, pode parar a busca no texto geral

        if not disponivel:
             observacoes = observacoes if observacoes else "Não foi possível encontrar evidências para este critério."

        return ResultadoCriterio(
            dimensao=criterio.dimensao,
            id_criterio=criterio.id_criterio,
            criterio=criterio.criterio,
            classificacao=criterio.classificacao,
            fundamentacao=criterio.fundamentacao,
            disponivel=disponivel,
            link_evidencia=link_evidencia,
            texto_evidencia=texto_evidencia,
            metodo_encontrado=metodo_encontrado,
            score_relevancia=score_relevancia,
            timestamp=datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            observacoes=observacoes
        )

    def auditoria_completa_criterios(self, transparencia_url: str, orgao_nome: str, site_url: Optional[str] = None) -> Dict:
        """Executa a auditoria completa para todos os critérios."""
        start_time = time.time()
        resultados_criterios = []
        links_evidencia = []
        criterios_conformes = 0
        total_criterios = len(self.criterios)

        # Ordena os critérios por ID para exibição
        criterios_ordenados = sorted(self.criterios.values(), key=lambda c: c.id_criterio)

        for criterio in criterios_ordenados:
            # Para o critério 1.1 (site oficial), verificamos o site_url, não o de transparência
            url_para_verificar = transparencia_url
            if criterio.id_criterio == "1.1":
                 url_para_verificar = site_url
            elif criterio.id_criterio == "1.3":
                 # Critério 1.3 é sobre a visibilidade na capa do SITE, não do portal
                 url_para_verificar = site_url

            resultado = self._verificar_criterio(url_para_verificar, criterio, site_url)

            resultados_criterios.append({
                "Dimensão": resultado.dimensao,
                "ID Critério": resultado.id_criterio,
                "Critério": resultado.criterio,
                "Classificação": resultado.classificacao,
                "Fundamentação Legal": resultado.fundamentacao,
                "Disponível": "Sim" if resultado.disponivel else "Não",
                "Link de Evidência": resultado.link_evidencia,
                "Texto de Evidência": resultado.texto_evidencia,
                "Método Encontrado": resultado.metodo_encontrado,
                "Score Relevância": resultado.score_relevancia,
                "Timestamp": resultado.timestamp,
                "Observações": resultado.observacoes
            })

            if resultado.disponivel:
                criterios_conformes += 1
                links_evidencia.append({
                    "ID Critério": resultado.id_criterio,
                    "Critério": resultado.criterio,
                    "Link": resultado.link_evidencia,
                    "Texto Evidência": resultado.texto_evidencia
                })

        end_time = time.time()
        tempo_auditoria = end_time - start_time

        percentual_geral = (criterios_conformes / total_criterios) * 100 if total_criterios > 0 else 0

        return {
            "orgao": orgao_nome,
            "url_analisada": transparencia_url,
            "timestamp_auditoria": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            "tempo_auditoria_segundos": tempo_auditoria,
            "metricas_conformidade": {
                "criterios_conformes": criterios_conformes,
                "total_criterios": total_criterios,
                "percentual_geral": percentual_geral
            },
            "criterios_verificados": resultados_criterios,
            "links_evidencia": links_evidencia
        }

# ================================
# FUNÇÕES AUXILIARES
# ================================
def check_website_status(url, timeout=10):
    """Verifica o status de uma URL."""
    if not url:
        return "⚪ Não informado", "URL não fornecida"
    try:
        # Adiciona um pequeno delay
        time.sleep(0.2)
        response = requests.head(url, timeout=timeout, verify=False)
        if response.status_code == 200:
            return "🟢 Online", f"Status: {response.status_code}"
        else:
            return "🟠 Offline/Erro", f"Status: {response.status_code}"
    except requests.exceptions.ConnectionError:
        return "🔴 Offline", "Erro de conexão"
    except requests.exceptions.Timeout:
        return "🟡 Timeout", "Tempo limite excedido"
    except requests.exceptions.RequestException as e:
        return "❌ Erro", f"Erro na requisição: {str(e)[:50]}..."
    except Exception as e:
        return "❌ Erro", str(e)[:50]

# ================================
# FUNÇÃO PRINCIPAL (SUA + NOVA ABA)
# ================================
def main():
    if "page" not in st.session_state:
        st.session_state.page = "home"

    if st.session_state.page == "home":
        # SUA PÁGINA INICIAL (exatamente igual)
        st.markdown('<h1 class="main-title">Sistema de Avaliação de Portais de Transparência</h1>', unsafe_allow_html=True)

        with st.container():
            col1, col2, col3 = st.columns([1, 2, 1])
            with col2:
                esfera = st.selectbox("Esfera:", ["Selecione...", "Estadual", "Municipal"], key="esfera_select")

                poder_options = ["Selecione..."]
                if esfera == "Estadual":
                    poder_options.extend(list(ORGAOS_DATA["Estadual"].keys()))
                elif esfera == "Municipal":
                    poder_options.extend(list(ORGAOS_DATA["Municipal"].keys()))
                poder = st.selectbox("Poder:", poder_options, key="poder_select")

                orgao_options = ["Selecione..."]
                if esfera != "Selecione..." and poder != "Selecione...":
                    if esfera in ORGAOS_DATA and poder in ORGAOS_DATA[esfera]:
                        orgao_options.extend(list(ORGAOS_DATA[esfera][poder].keys()))
                orgao = st.selectbox("Órgão:", orgao_options, key="orgao_select")

                if st.button("Buscar", type="primary", use_container_width=True):
                    if esfera != "Selecione..." and poder != "Selecione..." and orgao != "Selecione...":
                        st.session_state.selected_esfera = esfera
                        st.session_state.selected_poder = poder
                        st.session_state.selected_orgao = orgao
                        st.session_state.page = "analysis"
                        st.session_state.resultado_auditoria = None # Limpa resultado anterior
                        st.rerun()
                    else:
                        st.error("Por favor, selecione todos os filtros antes de buscar.")

    elif st.session_state.page == "analysis":
        # Cabeçalho com botão voltar (SUBSTITUI O SIDEBAR)
        with st.container():
            col1, col2 = st.columns([1, 3])
            with col1:
                if st.button("⬅️ Voltar ao Início", type="secondary"):
                    st.session_state.page = "home"
                    st.session_state.resultado_auditoria = None # Limpa resultado ao voltar
                    st.rerun()
            with col2:
                st.info(f"""
                **Auditoria em Andamento:**
                📍 {st.session_state.selected_esfera} → {st.session_state.selected_poder}
                🏛️ **{st.session_state.selected_orgao}**
                """)

        st.title("Análise de Transparência")
        st.markdown(f"### {st.session_state.selected_orgao}")

        orgao_data = ORGAOS_DATA[st.session_state.selected_esfera][st.session_state.selected_poder][st.session_state.selected_orgao]
        site_url = orgao_data.get("site")
        transparencia_url = orgao_data.get("transparencia")

        # ===== SEÇÃO 1: STATUS DOS SITES =====
        st.markdown("---")
        st.markdown("## 📊 Status dos Sites")
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("#### Site Oficial")
            with st.spinner("Verificando site oficial..."):
                status, details = check_website_status(site_url)
                st.metric("Status", status)
                st.caption(details)
                if site_url:
                    st.code(site_url)
        with col2:
            st.markdown("#### Portal da Transparência")
            with st.spinner("Verificando portal de transparência..."):
                status, details = check_website_status(transparencia_url)
                st.metric("Status", status)
                st.caption(details)
                if transparencia_url:
                    st.code(transparencia_url)
            if not transparencia_url:
                 st.warning("URL do Portal de Transparência não informada para este órgão.")

        # ===== SEÇÃO 2: AUDITORIA POR CRITÉRIOS =====
        st.markdown("---")
        st.markdown("## 🎯 Auditoria Detalhada por Critérios Legais")

        if transparencia_url:
            # Obtém critérios específicos para o poder selecionado
            criterios_poder = obter_criterios_por_poder(
                st.session_state.selected_poder, 
                st.session_state.selected_esfera
            )
            
            # Converte para formato de auditoria
            criterios_auditoria = converter_criterios_para_auditoria(criterios_poder)
            
            # Exibe informações sobre os critérios aplicáveis
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Total de Critérios", len(criterios_auditoria))
            with col2:
                essenciais = len([c for c in criterios_poder.values() if c['classificacao'] == 'Essencial'])
                st.metric("Essenciais", essenciais)
            with col3:
                obrigatorios = len([c for c in criterios_poder.values() if c['classificacao'] == 'Obrigatória'])
                st.metric("Obrigatórios", obrigatorios)
            
            # Adiciona seção expandível com critérios aplicáveis
            with st.expander("📋 Ver Critérios Aplicáveis para este Poder"):
                st.write(f"**Critérios aplicáveis para:** {st.session_state.selected_poder}")
                
                # Agrupa por dimensão
                dimensoes = {}
                for criterio in criterios_poder.values():
                    dimensao = criterio['dimensao']
                    if dimensao not in dimensoes:
                        dimensoes[dimensao] = []
                    dimensoes[dimensao].append(criterio)
                
                for dimensao, criterios_dim in dimensoes.items():
                    st.write(f"**{dimensao}** ({len(criterios_dim)} critérios)")
                    for criterio in criterios_dim:
                        cor = "🔴" if criterio['classificacao'] == 'Essencial' else "🟡" if criterio['classificacao'] == 'Obrigatória' else "🟢"
                        st.write(f"  {cor} {criterio['id']} - {criterio['criterio'][:80]}...")
            
            if st.button("🚀 Iniciar Auditoria Detalhada", type="primary", use_container_width=True):
                # Cria auditor com critérios específicos do poder
                auditor = AuditoriaTransparenciaCriterios(criterios_auditoria)
                
                with st.spinner(f"Executando auditoria detalhada no portal: {transparencia_url}..."):
                    resultado = auditor.auditoria_completa_criterios(
                        transparencia_url,
                        st.session_state.selected_orgao,
                        site_url # Passa o URL do site principal também
                    )
                st.session_state.resultado_auditoria = resultado
                st.success("✅ Auditoria concluída!")

            # ===== SEÇÃO 3: RESULTADOS DA AUDITORIA (Métricas e Exportação) =====
            if "resultado_auditoria" in st.session_state and st.session_state.resultado_auditoria:
                resultado = st.session_state.resultado_auditoria

                st.markdown("---")
                st.markdown("## 📊 Resultados da Auditoria")
                # Métricas
                col1, col2, col3 = st.columns(3)
                with col1:
                    st.metric("Conformidade Geral", f"{resultado['metricas_conformidade']['percentual_geral']:.1f}%")
                with col2:
                    st.metric("Critérios Conformes", f"{resultado['metricas_conformidade']['criterios_conformes']}/{resultado['metricas_conformidade']['total_criterios']}")
                with col3:
                    st.metric("Tempo de Auditoria", f"{resultado['tempo_auditoria_segundos']:.1f}s")

                # ===== SEÇÃO 4: EXPORTAÇÃO DO RELATÓRIO =====
                st.markdown("---")
                st.markdown("## 📥 Exportar Relatório de Auditoria")
                col1, col2 = st.columns([2, 1])
                with col1:
                    # Prepara dados para Excel
                    df_criterios = pd.DataFrame(resultado["criterios_verificados"])
                    df_evidencias = pd.DataFrame(resultado["links_evidencia"])

                    buffer_auditoria = BytesIO()
                    try:
                        with pd.ExcelWriter(buffer_auditoria, engine='openpyxl') as writer:
                            # Resumo
                            resumo_data = {
                                "Órgão": [resultado["orgao"]],
                                "URL Analisada": [resultado["url_analisada"]],
                                "Data Auditoria": [resultado["timestamp_auditoria"]],
                                "Conformidade (%)": [resultado["metricas_conformidade"]["percentual_geral"]],
                                "Critérios Conformes": [resultado["metricas_conformidade"]["criterios_conformes"]],
                                "Total de Critérios": [resultado["metricas_conformidade"]["total_criterios"]],
                                "Tempo de Auditoria (s)": [resultado["tempo_auditoria_segundos"]]
                            }
                            pd.DataFrame(resumo_data).to_excel(writer, sheet_name='Resumo', index=False)
                            # Critérios
                            df_criterios.to_excel(writer, sheet_name='Critérios', index=False)
                            # Evidências
                            if not df_evidencias.empty:
                                df_evidencias.to_excel(writer, sheet_name='Evidências', index=False)
                    except Exception as e:
                         st.error(f"Erro ao gerar arquivo Excel: {e}")
                         buffer_auditoria = None # Garante que o botão não apareça se houver erro

                    if buffer_auditoria:
                        st.download_button(
                            label="📥 Baixar Relatório Completo (Excel)",
                            data=buffer_auditoria.getvalue(),
                            file_name=f"auditoria_completa_{st.session_state.selected_orgao.replace(' ', '_')}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.xlsx",
                            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                            type="primary",
                            use_container_width=True
                        )
                with col2:
                    st.info(f"""
                    **📊 Relatório contém:**
                    • Resumo executivo
                    • {len(df_criterios) if 'df_criterios' in locals() else 0} critérios verificados
                    • {len(df_evidencias) if 'df_evidencias' in locals() else 0} links de evidência
                    • Base legal completa
                    """)

                # ===== SEÇÃO 5: RESULTADOS DETALHADOS POR CRITÉRIO =====
                st.markdown("---")
                st.markdown("## 📋 Resultados Detalhados por Critério")
                for criterio_res in resultado['criterios_verificados']:
                    card_class = "criterio-conforme" if criterio_res['Disponível'] == "Sim" else "criterio-nao-conforme"
                    status_icon = "✅" if criterio_res['Disponível'] == "Sim" else "❌"
                    st.markdown(f"""
                    <div class="criterio-card {card_class}">
                        <h4>{status_icon} {criterio_res['ID Critério']} - {criterio_res['Classificação']}</h4>
                        <p><strong>Critério:</strong> {criterio_res['Critério']}</p>
                        <p><strong>Fundamentação:</strong> {criterio_res['Fundamentação Legal']}</p>
                    </div>
                    """, unsafe_allow_html=True)
                    if criterio_res['Disponível'] == "Sim":
                        st.markdown(f"""
                        <div class="link-evidencia">
                            <strong>🔗 Link:</strong> <a href="{criterio_res['Link de Evidência']}" >{criterio_res['Link de Evidência']}</a><br>
                            <strong>📝 Evidência (trecho):</strong> `{criterio_res['Texto de Evidência']}`<br>
                            <strong>🔎 Método:</strong> {criterio_res['Método Encontrado']} | <strong>📊 Score:</strong> {criterio_res['Score Relevância']}
                        </div>
                        """, unsafe_allow_html=True)
                    else:
                         st.markdown(f"""
                         <div class="link-evidencia">
                             <strong>Observação:</strong> {criterio_res['Observações']}
                         </div>
                         """, unsafe_allow_html=True)
                    st.markdown("---")

                # Exibe o botão flutuante de "Voltar ao Topo"
                adicionar_botao_topo()

        else:
            st.warning("URL do Portal de Transparência não disponível para iniciar a auditoria detalhada.")

if __name__ == "__main__":
    main()