from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional, Dict, List
import time
from datetime import datetime
import asyncio
import aiohttp
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import re
from dataclasses import dataclass

# Imports dos seus módulos existentes
from .services.orgaos_data import ORGAOS_DATA
from .services.criterios_comum import CRITERIOS_TRANSPARENCIA
from .services.criterios_comum_exceto_estatais_independentes import CRITERIOS_COMUM_EXCETO_ESTATAIS_INDEPENDENTES
from .services.criterios_comum_exceto_estatais import CRITERIOS_COMUM_EXCETO_ESTATAIS
from .services.criterios_executivo import CRITERIOS_EXECUTIVO
from .services.criterios_executivo_consorcios import CRITERIOS_EXECUTIVO_CONSORCIOS
from .services.criterios_legislativo import CRITERIOS_LEGISLATIVO
from .services.criterios_judiciario import CRITERIOS_JUDICIARIO
from .services.criterios_tribunal_contas import CRITERIOS_TRIBUNAL_CONTAS
from .services.criterios_ministerio_publico import CRITERIOS_MINISTERIO_PUBLICO
from .services.criterios_defensoria import CRITERIOS_DEFENSORIA
from .services.criterios_consorcios_publicos import CRITERIOS_CONSORCIOS_PUBLICOS
from .services.criterios_estatais import CRITERIOS_ESTATAIS
from .services.criterios_estatais_independentes import CRITERIOS_ESTATAIS_INDEPENDENTES

app = FastAPI(title="PNTP API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://localhost:3001"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Schemas para a API
class AuditoriaRequest(BaseModel):
    transparencia_url: str
    orgao_nome: str
    site_url: Optional[str] = None
    esfera: str
    poder: str

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

# Suas funções existentes adaptadas
def obter_criterios_por_poder(poder_selecionado, esfera_selecionada=""):
    """Obtém os critérios aplicáveis baseado no poder selecionado"""
    criterios_aplicaveis = {}
    criterios_aplicaveis.update(CRITERIOS_TRANSPARENCIA)
    
    poder_normalizado = poder_selecionado.lower().replace(" ", "_")
    if "executivo" in poder_normalizado:
        criterios_aplicaveis.update(CRITERIOS_COMUM_EXCETO_ESTATAIS_INDEPENDENTES)
        criterios_aplicaveis.update(CRITERIOS_COMUM_EXCETO_ESTATAIS)
        criterios_aplicaveis.update(CRITERIOS_EXECUTIVO)
        criterios_aplicaveis.update(CRITERIOS_EXECUTIVO_CONSORCIOS)
    elif "legislativo" in poder_normalizado:
        criterios_aplicaveis.update(CRITERIOS_COMUM_EXCETO_ESTATAIS_INDEPENDENTES)
        criterios_aplicaveis.update(CRITERIOS_COMUM_EXCETO_ESTATAIS)
        criterios_aplicaveis.update(CRITERIOS_LEGISLATIVO)
    elif "judiciário" in poder_normalizado or "judiciario" in poder_normalizado:
        criterios_aplicaveis.update(CRITERIOS_COMUM_EXCETO_ESTATAIS_INDEPENDENTES)
        criterios_aplicaveis.update(CRITERIOS_COMUM_EXCETO_ESTATAIS)
        criterios_aplicaveis.update(CRITERIOS_JUDICIARIO)
    elif "tribunal" in poder_normalizado and "contas" in poder_normalizado:
        criterios_aplicaveis.update(CRITERIOS_COMUM_EXCETO_ESTATAIS_INDEPENDENTES)
        criterios_aplicaveis.update(CRITERIOS_COMUM_EXCETO_ESTATAIS)
        criterios_aplicaveis.update(CRITERIOS_TRIBUNAL_CONTAS)
    elif "ministério" in poder_normalizado and "público" in poder_normalizado:
        criterios_aplicaveis.update(CRITERIOS_COMUM_EXCETO_ESTATAIS_INDEPENDENTES)
        criterios_aplicaveis.update(CRITERIOS_COMUM_EXCETO_ESTATAIS)
        criterios_aplicaveis.update(CRITERIOS_MINISTERIO_PUBLICO)
    elif "defensoria" in poder_normalizado:
        criterios_aplicaveis.update(CRITERIOS_COMUM_EXCETO_ESTATAIS_INDEPENDENTES)
        criterios_aplicaveis.update(CRITERIOS_COMUM_EXCETO_ESTATAIS)
        criterios_aplicaveis.update(CRITERIOS_DEFENSORIA)
    elif "consórcios" in poder_normalizado or "consórcio" in poder_normalizado:
        criterios_aplicaveis.update(CRITERIOS_COMUM_EXCETO_ESTATAIS_INDEPENDENTES)
        criterios_aplicaveis.update(CRITERIOS_EXECUTIVO_CONSORCIOS)
        criterios_aplicaveis.update(CRITERIOS_CONSORCIOS_PUBLICOS)
    elif "estatais" in poder_normalizado:
        if "independente" in poder_normalizado:
            criterios_aplicaveis.update(CRITERIOS_ESTATAIS_INDEPENDENTES)
        else:
            criterios_aplicaveis.update(CRITERIOS_COMUM_EXCETO_ESTATAIS_INDEPENDENTES)
            criterios_aplicaveis.update(CRITERIOS_ESTATAIS)
    return criterios_aplicaveis

def converter_criterios_para_auditoria(criterios_dict):
    """Converte o dicionário de critérios modulados para o formato da classe AuditoriaTransparenciaCriterios"""
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
    """Gera seletores CSS automaticamente baseado nas palavras-chave"""
    seletores = [
        "title", "meta[name='description']", "header", ".header", "#header",
        "nav a", "menu a", ".menu a", ".nav a", "a", "h1", "h2", "h3",
        "footer a", ".footer a", "main", ".main", "#main"
    ]
    for palavra in palavras_chave:
        palavra_limpa = palavra.replace(" ", "-").lower()
        seletores.extend([
            f"a[href*='{palavra_limpa}']",
            f".{palavra_limpa}",
            f"#{palavra_limpa}",
            f"a:contains('{palavra.title()}')"
        ])
    return seletores

class AuditoriaTransparenciaCriterios:
    def __init__(self, criterios_customizados=None):
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
        self.timeout = 15

    def _definir_criterios_auditoria(self) -> Dict[str, CriterioAuditoria]:
        criterios = {
            "1.1": CriterioAuditoria(
                dimensao="Informações Prioritárias",
                id_criterio="1.1",
                criterio="Possui sítio oficial próprio na internet?",
                classificacao="Essencial",
                fundamentacao="Art. 48, §1º, II, da LC nº 101/00 e arts. 3º, III, 6º, I, e 8º, §2º, da Lei nº 12.527/2011 – LAI.",
                palavras_chave=["site oficial", "portal oficial", "página oficial", "sítio oficial", "website oficial"],
                seletores_especificos=["title", "meta[name='description']", "header", ".header", "#header"]
            ),
        }
        return criterios

    async def _fetch_page_async(self, session: aiohttp.ClientSession, url: str) -> Optional[BeautifulSoup]:
        if not url:
            return None
        try:
            await asyncio.sleep(0.5)
            async with session.get(url, timeout=self.timeout, headers=self.headers) as response:
                if response.status == 200:
                    content = await response.text()
                    return BeautifulSoup(content, 'html.parser')
        except Exception as e:
            print(f"Erro ao acessar {url}: {e}")
            return None

    async def _verificar_criterio_async(self, session: aiohttp.ClientSession, base_url: str, criterio: CriterioAuditoria, main_site_url: Optional[str] = None) -> ResultadoCriterio:
        if criterio.id_criterio == "1.1":
            return await self._verificar_criterio_site_oficial_async(session, base_url, criterio, main_site_url)
        
        url_to_check = base_url
        soup = await self._fetch_page_async(session, url_to_check)
        
        disponivel = False
        link_evidencia = ""
        texto_evidencia = ""
        metodo_encontrado = "Não encontrado"
        score_relevancia = 0
        observacoes = ""

        if soup:
            for selector in criterio.seletores_especificos:
                try:
                    elements = soup.select(selector)
                    for element in elements:
                        text = element.get_text().lower().strip()
                        href = element.get('href', '').lower().strip()
                        if any(kw in text or kw in href for kw in criterio.palavras_chave):
                            disponivel = True
                            link_evidencia = urljoin(url_to_check, href) if href else url_to_check
                            texto_evidencia = text[:200] + "..." if len(text) > 200 else text
                            metodo_encontrado = f"Seletor: {selector}"
                            score_relevancia = 100 if selector in ["header a", ".menu a", "nav a"] else 80
                            observacoes = f"Encontrado via seletor '{selector}'"
                            break
                except Exception as e:
                    pass
                if disponivel and score_relevancia == 100:
                    break

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

    async def _verificar_criterio_site_oficial_async(self, session: aiohttp.ClientSession, base_url: str, criterio: CriterioAuditoria, main_site_url: Optional[str] = None) -> ResultadoCriterio:
        url_to_check = main_site_url if main_site_url else base_url
        
        try:
            async with session.head(url_to_check, timeout=self.timeout) as response:
                is_online = response.status == 200
                status_message = f"Status HTTP: {response.status}"
        except:
            is_online = False
            status_message = "Site inacessível"

        if not is_online:
            return ResultadoCriterio(
                dimensao=criterio.dimensao,
                id_criterio=criterio.id_criterio,
                criterio=criterio.criterio,
                classificacao=criterio.classificacao,
                fundamentacao=criterio.fundamentacao,
                disponivel=False,
                link_evidencia=url_to_check if url_to_check else "",
                texto_evidencia="",
                metodo_encontrado="Verificação de status HTTP",
                score_relevancia=0,
                timestamp=datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                observacoes=f"Site inacessível: {status_message}"
            )

        return ResultadoCriterio(
            dimensao=criterio.dimensao,
            id_criterio=criterio.id_criterio,
            criterio=criterio.criterio,
            classificacao=criterio.classificacao,
            fundamentacao=criterio.fundamentacao,
            disponivel=True,
            link_evidencia=url_to_check,
            texto_evidencia="Site acessível",
            metodo_encontrado="Status HTTP 200",
            score_relevancia=100,
            timestamp=datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            observacoes=f"Site online: {status_message}"
        )

    async def auditoria_completa_async(self, transparencia_url: str, orgao_nome: str, site_url: Optional[str] = None) -> Dict:
        start_time = time.time()
        resultados_criterios = []
        links_evidencia = []
        criterios_conformes = 0
        total_criterios = len(self.criterios)
        
        criterios_ordenados = sorted(self.criterios.values(), key=lambda c: c.id_criterio)

        async with aiohttp.ClientSession() as session:
            for i, criterio in enumerate(criterios_ordenados):
                url_para_verificar = transparencia_url
                if criterio.id_criterio == "1.1":
                    url_para_verificar = site_url

                resultado = await self._verificar_criterio_async(session, url_para_verificar, criterio, site_url)

                resultados_criterios.append({
                    "dimensao": resultado.dimensao,
                    "id_criterio": resultado.id_criterio,
                    "criterio": resultado.criterio,
                    "classificacao": resultado.classificacao,
                    "fundamentacao_legal": resultado.fundamentacao,
                    "disponivel": resultado.disponivel,
                    "link_evidencia": resultado.link_evidencia,
                    "texto_evidencia": resultado.texto_evidencia,
                    "metodo_encontrado": resultado.metodo_encontrado,
                    "timestamp": resultado.timestamp,
                    "observacoes": resultado.observacoes
                })

                if resultado.disponivel:
                    criterios_conformes += 1
                    links_evidencia.append({
                        "id_criterio": resultado.id_criterio,
                        "criterio": resultado.criterio,
                        "link": resultado.link_evidencia,
                        "texto_evidencia": resultado.texto_evidencia
                    })

        end_time = time.time()
        tempo_auditoria = end_time - start_time
        percentual_geral = (criterios_conformes / total_criterios) * 100 if total_criterios > 0 else 0

        return {
            "orgao": orgao_nome,
            "url_analisada": transparencia_url,
            "timestamp_auditoria": datetime.now().isoformat(),
            "tempo_auditoria_segundos": tempo_auditoria,
            "metricas_conformidade": {
                "criterios_conformes": criterios_conformes,
                "total_criterios": total_criterios,
                "percentual_geral": percentual_geral
            },
            "criterios_verificados": resultados_criterios,
            "links_evidencia": links_evidencia
        }

# Endpoints da API
@app.get("/")
async def root():
    return {"message": "PNTP API funcionando", "version": "1.0.0"}

@app.get("/api/orgaos")
async def get_orgaos():
    return ORGAOS_DATA

@app.post("/api/auditoria/iniciar")
async def iniciar_auditoria(request: AuditoriaRequest):
    try:
        criterios_poder = obter_criterios_por_poder(request.poder, request.esfera)
        criterios_auditoria = converter_criterios_para_auditoria(criterios_poder)
        
        auditor = AuditoriaTransparenciaCriterios(criterios_auditoria)
        
        resultado = await auditor.auditoria_completa_async(
            request.transparencia_url,
            request.orgao_nome,
            request.site_url
        )
        
        return {
            "status": "completed",
            "resultado": resultado
        }
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro na auditoria: {str(e)}")
