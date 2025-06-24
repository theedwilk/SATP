import pandas as pd
import numpy as np
from datetime import datetime
import ipywidgets as widgets
from IPython.display import display, clear_output, HTML
import requests
from urllib.parse import urlparse, urljoin, urlsplit
import time
from bs4 import BeautifulSoup
import re
import warnings
warnings.filterwarnings('ignore')
import streamlit as st
import json

# Configuração da página
st.set_page_config(
    page_title="Sistema de Avaliação de Portais de Transparência",
    page_icon="🔍",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# CSS customizado
st.markdown("""
<style>
    /* Esconde a sidebar na página inicial */
    [data-testid="stSidebar"] {
        display: none;
    }
    
    /* Container principal centralizado */
    .main-container {
        max-width: 800px;
        margin: 0 auto;
        padding: 2rem;
    }
    
    /* Título estilizado */
    .main-title {
        text-align: center;
        color: #1e3a8a;
        font-size: 2.5rem;
        font-weight: bold;
        margin-bottom: 3rem;
    }
    
    /* Estilo dos selectboxes */
    .stSelectbox {
        margin-bottom: 1.5rem;
    }
    
    /* Botão customizado */
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
</style>
""", unsafe_allow_html=True)

# Dados dos órgãos com URLs
ORGAOS_DATA = {
    "Estadual": {
        "Poder Executivo": {
            "Governo do Estado do Amazonas": {
                "site": "https://www.amazonas.am.gov.br/",
                "transparencia": "https://www.transparencia.am.gov.br/"
            }
        },
        "Poder Legislativo": {
            "Assembleia Legislativa (ALEAM)": {
                "site": "https://www.ale.am.gov.br/",
                "transparencia": "https://transparencia.ale.am.gov.br/"
            }
        },
        "Poder Judiciário": {
            "Tribunal de Justiça TJAM": {
                "site": "https://www.tjam.jus.br/",
                "transparencia": "https://www.tjam.jus.br/index.php/transparencia"
            }
        },
        "Tribunal de Contas": {
            "Tribunal de Contas TCE": {
                "site": "https://www.tce.am.gov.br/",
                "transparencia": "https://transparencia.tce.am.gov.br/"
            }
        },
        "Ministério Público": {
            "Ministério Público MPE": {
                "site": "https://www.mpam.mp.br/",
                "transparencia": "https://transparencia.mpam.mp.br/"
            }
        },
        "Defensoria": {
            "Defensoria DPE": {
                "site": "https://www.defensoria.am.gov.br/",
                "transparencia": "https://transparencia.defensoria.am.gov.br/"
            }
        },
        "Consórcios Públicos": {
            "Consórcio Interestadual de Desenvolvimento Sustentável da Amazônia Legal (CAL)": {
                "site": "https://amazonialegal.info/",
                "transparencia": ""
            }
        },
        "Estatais": {
            "Companhia de Saneamento do Amazonas – COSAMA": {
                "site": "https://cosama.am.gov.br/",
                "transparencia": "https://cosama.portaldatransparencia.org/"
            },
            "Processamento de Dados Amazonas S/A – PRODAM": {
                "site": "https://www.prodam.am.gov.br/",
                "transparencia": "https://prodam.am.gov.br/transparencia/"
            },
            "Companhia de Gás do Amazonas – CIGÁS": {
                "site": "https://www.cigas-am.com.br/",
                "transparencia": "https://www.cigas-am.com.br/institucional/transparencia/"
            }
        }
    },
    "Municipal": {
        "Poder Executivo": {
            # Prefeituras
            "Prefeitura de Alvarães": {"site": "https://www.alvaraes.am.gov.br/", "transparencia": "https://www.alvaraes.am.gov.br/transparencia"},
            "Prefeitura de Amaturá": {"site": "https://www.amatura.am.gov.br/", "transparencia": "https://www.amatura.am.gov.br/transparencia"},
            "Prefeitura de Anamã": {"site": "https://www.anama.am.gov.br/", "transparencia": "https://www.anama.am.gov.br/transparencia"},
            "Prefeitura de Anori": {"site": "https://www.anori.am.gov.br/", "transparencia": "https://www.anori.am.gov.br/transparencia"},
            "Prefeitura de Apuí": {"site": "https://www.apui.am.gov.br/", "transparencia": "https://transparencia.apui.am.gov.br/"},
            "Prefeitura de Atalaia do Norte": {"site": "https://www.atalaiadonorte.am.gov.br/", "transparencia": "https://www.atalaiadonorte.am.gov.br/transparencia"},
            "Prefeitura de Autazes": {"site": "https://www.autazes.am.gov.br/", "transparencia": "https://www.autazes.am.gov.br/transparencia"},
            "Prefeitura de Barcelos": {"site": "https://www.barcelos.am.gov.br/", "transparencia": "https://www.barcelos.am.gov.br/transparencia"},
            "Prefeitura de Barreirinha": {"site": "https://www.barreirinha.am.gov.br/", "transparencia": "https://www.barreirinha.am.gov.br/transparencia"},
            "Prefeitura de Benjamin Constant": {"site": "https://www.benjaminconstant.am.gov.br/", "transparencia": "https://transparencia.benjaminconstant.am.gov.br/"},
            "Prefeitura de Beruri": {"site": "https://www.beruri.am.gov.br/", "transparencia": "https://www.beruri.am.gov.br/transparencia"},
            "Prefeitura de Boa Vista do Ramos": {"site": "https://www.boavistadoramos.am.gov.br/", "transparencia": "https://www.boavistadoramos.am.gov.br/transparencia"},
            "Prefeitura de Boca do Acre": {"site": "https://www.bocadoacre.am.gov.br/", "transparencia": "https://www.bocadoacre.am.gov.br/transparencia"},
            "Prefeitura de Borba": {"site": "https://www.borba.am.gov.br/", "transparencia": "https://transparencia.borba.am.gov.br/"},
            "Prefeitura de Caapiranga": {"site": "https://www.caapiranga.am.gov.br/", "transparencia": "https://www.caapiranga.am.gov.br/transparencia"},
            "Prefeitura de Canutama": {"site": "https://www.canutama.am.gov.br/", "transparencia": "https://www.canutama.am.gov.br/transparencia"},
            "Prefeitura de Carauari": {"site": "https://www.carauari.am.gov.br/", "transparencia": "https://www.carauari.am.gov.br/transparencia"},
            "Prefeitura de Careiro": {"site": "https://www.careiro.am.gov.br/", "transparencia": "https://transparencia.careiro.am.gov.br/"},
            "Prefeitura de Careiro da Várzea": {"site": "https://www.careirodavarzea.am.gov.br/", "transparencia": "https://www.careirodavarzea.am.gov.br/transparencia"},
            "Prefeitura de Coari": {"site": "https://www.coari.am.gov.br/", "transparencia": "https://transparencia.coari.am.gov.br/"},
            "Prefeitura de Codajás": {"site": "https://www.codajas.am.gov.br/", "transparencia": "https://www.codajas.am.gov.br/transparencia"},
            "Prefeitura de Eirunepé": {"site": "https://www.eirunepe.am.gov.br/", "transparencia": "https://www.eirunepe.am.gov.br/transparencia"},
            "Prefeitura de Envira": {"site": "https://www.envira.am.gov.br/", "transparencia": "https://www.envira.am.gov.br/transparencia"},
            "Prefeitura de Fonte Boa": {"site": "https://www.fonteboa.am.gov.br/", "transparencia": "https://www.fonteboa.am.gov.br/transparencia"},
            "Prefeitura de Guajará": {"site": "https://www.guajara.am.gov.br/", "transparencia": "https://www.guajara.am.gov.br/transparencia"},
            "Prefeitura de Humaitá": {"site": "https://www.humaita.am.gov.br/", "transparencia": "https://transparencia.humaita.am.gov.br/"},
            "Prefeitura de Ipixuna": {"site": "https://www.ipixuna.am.gov.br/", "transparencia": "https://www.ipixuna.am.gov.br/transparencia"},
            "Prefeitura de Iranduba": {"site": "https://www.iranduba.am.gov.br/", "transparencia": "https://transparencia.iranduba.am.gov.br/"},
            "Prefeitura de Itacoatiara": {"site": "https://www.itacoatiara.am.gov.br/", "transparencia": "https://transparencia.itacoatiara.am.gov.br/"},
            "Prefeitura de Itamarati": {"site": "https://www.itamarati.am.gov.br/", "transparencia": "https://www.itamarati.am.gov.br/transparencia"},
            "Prefeitura de Itapiranga": {"site": "https://www.itapiranga.am.gov.br/", "transparencia": "https://transparencia.itapiranga.am.gov.br/"},
            "Prefeitura de Japurá": {"site": "https://www.japura.am.gov.br/", "transparencia": "https://www.japura.am.gov.br/transparencia"},
            "Prefeitura de Juruá": {"site": "https://www.jurua.am.gov.br/", "transparencia": "https://www.jurua.am.gov.br/transparencia"},
            "Prefeitura de Jutaí": {"site": "https://www.jutai.am.gov.br/", "transparencia": "https://www.jutai.am.gov.br/transparencia"},
            "Prefeitura de Lábrea": {"site": "https://www.labrea.am.gov.br/", "transparencia": "https://transparencia.labrea.am.gov.br/"},
            "Prefeitura de Manacapuru": {"site": "https://www.manacapuru.am.gov.br/", "transparencia": "https://transparencia.manacapuru.am.gov.br/"},
            "Prefeitura de Manaquiri": {"site": "https://www.manaquiri.am.gov.br/", "transparencia": "https://www.manaquiri.am.gov.br/transparencia"},
            "Prefeitura de Manaus (PMM)": {"site": "https://www.manaus.am.gov.br/", "transparencia": "https://transparencia.manaus.am.gov.br/"},
            "Prefeitura de Manicoré": {"site": "https://www.manicore.am.gov.br/", "transparencia": "https://transparencia.manicore.am.gov.br/"},
            "Prefeitura de Maraã": {"site": "https://www.maraa.am.gov.br/", "transparencia": "https://www.maraa.am.gov.br/transparencia"},
            "Prefeitura de Maués": {"site": "https://www.maues.am.gov.br/", "transparencia": "https://transparencia.maues.am.gov.br/"},
            "Prefeitura de Nhamundá": {"site": "https://www.nhamunda.am.gov.br/", "transparencia": "https://www.nhamunda.am.gov.br/transparencia"},
            "Prefeitura de Nova Olinda do Norte": {"site": "https://www.novaolindadonorte.am.gov.br/", "transparencia": "https://www.novaolindadonorte.am.gov.br/transparencia"},
            "Prefeitura de Novo Airão": {"site": "https://www.novoairao.am.gov.br/", "transparencia": "https://transparencia.novoairao.am.gov.br/"},
            "Prefeitura de Novo Aripuanã": {"site": "https://www.novoaripuana.am.gov.br/", "transparencia": "https://www.novoaripuana.am.gov.br/transparencia"},
            "Prefeitura de Parintins": {"site": "https://www.parintins.am.gov.br/", "transparencia": "https://transparencia.parintins.am.gov.br/"},
            "Prefeitura de Pauini": {"site": "https://www.pauini.am.gov.br/", "transparencia": "https://www.pauini.am.gov.br/transparencia"},
            "Prefeitura de Presidente Figueiredo": {"site": "https://www.presidentefigueiredo.am.gov.br/", "transparencia": "https://transparencia.presidentefigueiredo.am.gov.br/"},
            "Prefeitura de Rio Preto da Eva": {"site": "https://www.riopretodaeva.am.gov.br/", "transparencia": "https://transparencia.riopretodaeva.am.gov.br/"},
            "Prefeitura de Santa Isabel do Rio Negro": {"site": "https://www.santaisabel.am.gov.br/", "transparencia": "https://www.santaisabel.am.gov.br/transparencia"},
            "Prefeitura de Santo Antônio do Içá": {"site": "https://www.santoantoniodoica.am.gov.br/", "transparencia": "https://www.santoantoniodoica.am.gov.br/transparencia"},
            "Prefeitura de Silves": {"site": "https://www.silves.am.gov.br/", "transparencia": "https://www.silves.am.gov.br/transparencia"},
            "Prefeitura de São Gabriel da Cachoeira": {"site": "https://www.saogabrieldacachoeira.am.gov.br/", "transparencia": "https://transparencia.saogabrieldacachoeira.am.gov.br/"},
            "Prefeitura de São Paulo de Olivença": {"site": "https://www.saopaulodeolivenca.am.gov.br/", "transparencia": "https://www.saopaulodeolivenca.am.gov.br/transparencia"},
            "Prefeitura de São Sebastião do Uatumã": {"site": "https://www.saosebastiaodouatuma.am.gov.br/", "transparencia": "https://www.saosebastiaodouatuma.am.gov.br/transparencia"},
            "Prefeitura de Tabatinga": {"site": "https://www.tabatinga.am.gov.br/", "transparencia": "https://transparencia.tabatinga.am.gov.br/"},
            "Prefeitura de Tapauá": {"site": "https://www.tapaua.am.gov.br/", "transparencia": "https://www.tapaua.am.gov.br/transparencia"},
            "Prefeitura de Tefé": {"site": "https://www.tefe.am.gov.br/", "transparencia": "https://transparencia.tefe.am.gov.br/"},
            "Prefeitura de Tonantins": {"site": "https://www.tonantins.am.gov.br/", "transparencia": "https://www.tonantins.am.gov.br/transparencia"},
            "Prefeitura de Uarini": {"site": "https://www.uarini.am.gov.br/", "transparencia": "https://www.uarini.am.gov.br/transparencia"},
            "Prefeitura de Urucará": {"site": "https://www.urucara.am.gov.br/", "transparencia": "https://www.urucara.am.gov.br/transparencia"},
            "Prefeitura de Urucurituba": {"site": "https://www.urucurituba.am.gov.br/", "transparencia": "https://www.urucurituba.am.gov.br/transparencia"}
        },
        "Poder Legislativo": {
            # Câmaras Municipais
            "Câmara de Alvarães": {"site": "https://www.alvaraes.am.leg.br/", "transparencia": "https://www.alvaraes.am.leg.br"},
            "Câmara de Amaturá": {"site": "https://www.amatura.am.leg.br/", "transparencia": "https://www.amatura.am.leg.br"},
            "Câmara de Anamã": {"site": "https://www.anama.am.leg.br/", "transparencia": "https://www.anama.am.leg.br"},
            "Câmara de Anori": {"site": "https://www.anori.am.leg.br/", "transparencia": "https://www.anori.am.leg.br"},
            "Câmara de Apuí": {"site": "https://www.apui.am.leg.br/", "transparencia": "https://www.apui.am.leg.br"},
            "Câmara de Atalaia do Norte": {"site": "https://www.atalaiadonorte.am.leg.br/", "transparencia": "https://www.atalaiadonorte.am.leg.br"},
            "Câmara de Autazes": {"site": "https://www.autazes.am.leg.br/", "transparencia": "https://www.autazes.am.leg.br"},
            "Câmara de Barcelos": {"site": "https://www.barcelos.am.leg.br/", "transparencia": "https://www.barcelos.am.leg.br"},
            "Câmara de Barreirinha": {"site": "https://www.barreirinha.am.leg.br/", "transparencia": "https://www.barreirinha.am.leg.br"},
            "Câmara de Benjamin Constant": {"site": "https://www.benjaminconstant.am.leg.br/", "transparencia": "https://www.benjaminconstant.am.leg.br"},
            "Câmara de Beruri": {"site": "https://www.beruri.am.leg.br/", "transparencia": "https://www.beruri.am.leg.br"},
            "Câmara de Boa Vista do Ramos": {"site": "https://www.boavistadoramos.am.leg.br/", "transparencia": "https://www.boavistadoramos.am.leg.br"},
            "Câmara de Boca do Acre": {"site": "https://www.bocadoacre.am.leg.br/", "transparencia": "https://www.bocadoacre.am.leg.br"},
            "Câmara de Borba": {"site": "https://www.borba.am.leg.br/", "transparencia": "https://www.borba.am.leg.br"},
            "Câmara de Caapiranga": {"site": "https://www.caapiranga.am.leg.br/", "transparencia": "https://www.caapiranga.am.leg.br"},
            "Câmara de Canutama": {"site": "https://www.canutama.am.leg.br/", "transparencia": "https://www.canutama.am.leg.br"},
            "Câmara de Carauari": {"site": "https://www.carauari.am.leg.br/", "transparencia": "https://www.carauari.am.leg.br"},
            "Câmara de Careiro": {"site": "https://www.cmcareiro.am.gov.br/", "transparencia": "https://www.careiro.am.leg.br"},
            "Câmara de Careiro da Várzea": {"site": "https://www.careirodavarzea.am.leg.br/", "transparencia": "https://www.careirodavarzea.am.leg.br"},
            "Câmara de Coari": {"site": "https://www.coari.am.leg.br/", "transparencia": "https://www.coari.am.leg.br"},
            "Câmara de Codajás": {"site": "https://www.codajas.am.leg.br/", "transparencia": "https://www.codajas.am.leg.br"},
            "Câmara de Eirunepé": {"site": "https://www.eirunepe.am.leg.br/", "transparencia": "https://www.eirunepe.am.leg.br"},
            "Câmara de Envira": {"site": "https://www.envira.am.leg.br/", "transparencia": "https://www.envira.am.leg.br"},
            "Câmara de Fonte Boa": {"site": "https://www.fonteboa.am.leg.br/", "transparencia": "https://www.fonteboa.am.leg.br"},
            "Câmara de Guajará": {"site": "https://www.guajara.am.leg.br/", "transparencia": "https://www.guajara.am.leg.br"},
            "Câmara de Humaitá": {"site": "https://www.humaita.am.leg.br/", "transparencia": "https://www.humaita.am.leg.br"},
            "Câmara de Ipixuna": {"site": "https://www.ipixuna.am.leg.br/", "transparencia": "https://www.ipixuna.am.leg.br"},
            "Câmara de Iranduba": {"site": "https://www.iranduba.am.leg.br/", "transparencia": "https://www.iranduba.am.leg.br"},
            "Câmara de Itacoatiara": {"site": "https://www.itacoatiara.am.leg.br/", "transparencia": "https://www.itacoatiara.am.leg.br"},
            "Câmara de Itamarati": {"site": "https://www.itamarati.am.leg.br/", "transparencia": "https://www.itamarati.am.leg.br"},
            "Câmara de Itapiranga": {"site": "https://www.itapiranga.am.leg.br/", "transparencia": "https://www.itapiranga.am.leg.br"},
            "Câmara de Japurá": {"site": "https://www.japura.am.leg.br/", "transparencia": "https://www.japura.am.leg.br"},
            "Câmara de Juruá": {"site": "https://www.jurua.am.leg.br/", "transparencia": "https://www.jurua.am.leg.br"},
            "Câmara de Jutaí": {"site": "https://www.jutai.am.leg.br/", "transparencia": "https://www.jutai.am.leg.br"},
            "Câmara de Lábrea": {"site": "https://www.labrea.am.leg.br/", "transparencia": "https://www.labrea.am.leg.br"},
            "Câmara de Manacapuru": {"site": "https://www.manacapuru.am.leg.br/", "transparencia": "https://www.manacapuru.am.leg.br"},
            "Câmara de Manaquiri": {"site": "https://www.manaquiri.am.leg.br/", "transparencia": "https://www.manaquiri.am.leg.br"},
            "Câmara de Manaus": {"site": "https://www.cmm.am.gov.br/", "transparencia": "https://transparencia.cmm.am.gov.br/"},
            "Câmara de Manicoré": {"site": "https://www.manicore.am.leg.br/", "transparencia": "https://www.manicore.am.leg.br"},
            "Câmara de Maraã": {"site": "https://www.maraa.am.leg.br/", "transparencia": "https://www.maraa.am.leg.br"},
            "Câmara de Maués": {"site": "https://www.maues.am.leg.br/", "transparencia": "https://www.maues.am.leg.br"},
            "Câmara de Nhamundá": {"site": "https://www.nhamunda.am.leg.br/", "transparencia": "https://www.nhamunda.am.leg.br"},
            "Câmara de Nova Olinda do Norte": {"site": "https://www.novaolindadonorte.am.leg.br/", "transparencia": "https://www.novaolindadonorte.am.leg.br"},
            "Câmara de Novo Airão": {"site": "https://www.novoairao.am.leg.br/", "transparencia": "https://www.novoairao.am.leg.br"},
            "Câmara de Novo Aripuanã": {"site": "https://www.novoaripuana.am.leg.br/", "transparencia": "https://www.novoaripuana.am.leg.br"},
            "Câmara de Parintins": {"site": "https://www.parintins.am.leg.br/", "transparencia": "https://www.parintins.am.leg.br"},
            "Câmara de Pauini": {"site": "https://www.pauini.am.leg.br/", "transparencia": "https://www.pauini.am.leg.br"},
            "Câmara de Presidente Figueiredo": {"site": "https://www.presidentefigueiredo.am.leg.br/", "transparencia": "https://www.presidentefigueiredo.am.leg.br"},
            "Câmara de Rio Preto da Eva": {"site": "https://www.riopretodaeva.am.leg.br/", "transparencia": "https://www.riopretodaeva.am.leg.br"},
            "Câmara de Santa Isabel do Rio Negro": {"site": "https://www.santaisabel.am.leg.br/", "transparencia": "https://www.santaisabel.am.leg.br"},
            "Câmara de Santo Antônio do Içá": {"site": "https://www.santoantoniodoica.am.leg.br/", "transparencia": "https://www.santoantoniodoica.am.leg.br"},
            "Câmara de Silves": {"site": "https://www.silves.am.leg.br/", "transparencia": "https://www.silves.am.leg.br"},
            "Câmara de São Gabriel da Cachoeira": {"site": "https://www.saogabrieldacachoeira.am.leg.br/", "transparencia": "https://www.saogabrieldacachoeira.am.leg.br"},
            "Câmara de São Paulo de Olivença": {"site": "https://www.saopaulodeolivenca.am.leg.br/", "transparencia": "https://www.saopaulodeolivenca.am.leg.br"},
            "Câmara de São Sebastião do Uatumã": {"site": "https://www.saosebastiaodouatuma.am.leg.br/", "transparencia": "https://www.saosebastiaodouatuma.am.leg.br"},
            "Câmara de Tabatinga": {"site": "https://www.tabatinga.am.leg.br/", "transparencia": "https://www.tabatinga.am.leg.br"},
            "Câmara de Tapauá": {"site": "https://www.tapaua.am.leg.br/", "transparencia": "https://www.tapaua.am.leg.br"},
            "Câmara de Tefé": {"site": "https://www.tefe.am.leg.br/", "transparencia": "https://www.tefe.am.leg.br"},
            "Câmara de Tonantins": {"site": "https://www.tonantins.am.leg.br/", "transparencia": "https://www.tonantins.am.leg.br"},
            "Câmara de Uarini": {"site": "https://www.uarini.am.leg.br/", "transparencia": "https://www.uarini.am.leg.br"},
            "Câmara de Urucará": {"site": "https://www.urucara.am.leg.br/", "transparencia": "https://www.urucara.am.leg.br"},
            "Câmara de Urucurituba": {"site": "https://www.urucurituba.am.leg.br/", "transparencia": "https://www.urucurituba.am.leg.br"}
        }
    }
}

def check_website_status(url, timeout=10):
    """Verifica o status de um website"""
    if not url:
        return "N/A", "URL não disponível"
    
    try:
        response = requests.get(url, timeout=timeout, verify=False)
        if response.status_code == 200:
            return "✅ Online", f"Status: {response.status_code}"
        else:
            return "⚠️ Problema", f"Status: {response.status_code}"
    except requests.exceptions.Timeout:
        return "⏱️ Timeout", "Site demorou muito para responder"
    except requests.exceptions.ConnectionError:
        return "❌ Offline", "Não foi possível conectar"
    except Exception as e:
        return "❌ Erro", str(e)[:50]

def analyze_transparency_elements(url, timeout=10):
    """Analisa elementos de transparência em um site"""
    elements = {
        "LAI": False,
        "e-SIC": False,
        "Receitas": False,
        "Despesas": False,
        "Licitações": False,
        "Contratos": False,
        "Servidores": False,
        "Diárias": False,
        "Convênios": False,
        "Obras": False
    }
    
    if not url:
        return elements, []
    
    try:
        response = requests.get(url, timeout=timeout, verify=False)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            text_content = soup.get_text().lower()
            
            # Palavras-chave para cada elemento
            keywords = {
                "LAI": ["lei de acesso", "acesso à informação", "lai", "12.527"],
                "e-SIC": ["e-sic", "esic", "serviço de informação", "sic"],
                "Receitas": ["receita", "arrecadação", "tributos"],
                "Despesas": ["despesa", "gastos", "pagamentos"],
                "Licitações": ["licitação", "licitações", "pregão", "edital"],
                "Contratos": ["contrato", "contratos", "aditivos"],
                "Servidores": ["servidor", "servidores", "folha de pagamento", "pessoal"],
                "Diárias": ["diária", "diárias", "viagens"],
                "Convênios": ["convênio", "convênios", "parceria"],
                "Obras": ["obra", "obras", "construção", "reforma"]
            }
            
            found_elements = []
            for element, words in keywords.items():
                if any(word in text_content for word in words):
                    elements[element] = True
                    found_elements.append(element)
            
            return elements, found_elements
    except:
        return elements, []

def main():
    if "page" not in st.session_state:
        st.session_state.page = "home"
    
    if st.session_state.page == "home":
        # Página inicial
        st.markdown('<h1 class="main-title">Sistema de Avaliação de Portais de Transparência</h1>', unsafe_allow_html=True)
        
        with st.container():
            col1, col2, col3 = st.columns([1, 2, 1])
            
            with col2:
                # Filtro de Esfera
                esfera = st.selectbox(
                    "Esfera:",
                    ["Selecione...", "Estadual", "Municipal"],
                    key="esfera_select"
                )
                
                # Filtro de Poder
                poder_options = ["Selecione..."]
                if esfera == "Estadual":
                    poder_options.extend(list(ORGAOS_DATA["Estadual"].keys()))
                elif esfera == "Municipal":
                    poder_options.extend(list(ORGAOS_DATA["Municipal"].keys()))
                
                poder = st.selectbox(
                    "Poder:",
                    poder_options,
                    key="poder_select"
                )
                
                # Filtro de Órgão
                orgao_options = ["Selecione..."]
                if esfera != "Selecione..." and poder != "Selecione...":
                    if esfera in ORGAOS_DATA and poder in ORGAOS_DATA[esfera]:
                        orgao_options.extend(list(ORGAOS_DATA[esfera][poder].keys()))
                
                orgao = st.selectbox(
                    "Órgão:",
                    orgao_options,
                    key="orgao_select"
                )
                
                # Botão Buscar
                if st.button("Buscar", type="primary", use_container_width=True):
                    if esfera != "Selecione..." and poder != "Selecione..." and orgao != "Selecione...":
                        st.session_state.selected_esfera = esfera
                        st.session_state.selected_poder = poder
                        st.session_state.selected_orgao = orgao
                        st.session_state.page = "analysis"
                        st.rerun()
                    else:
                        st.error("Por favor, selecione todos os filtros antes de buscar.")
    
    elif st.session_state.page == "analysis":
        # Mostra a sidebar na página de análise
        st.markdown("""
        <style>
            [data-testid="stSidebar"] {
                display: block !important;
            }
        </style>
        """, unsafe_allow_html=True)
        
        # Sidebar com opções
        with st.sidebar:
            st.title("Menu")
            
            if st.button("🏠 Voltar ao Início", use_container_width=True):
                st.session_state.page = "home"
                st.rerun()
            
            st.divider()
            
            # Informações da seleção
            st.info(f"""
            **Filtros Selecionados:**
            - Esfera: {st.session_state.selected_esfera}
            - Poder: {st.session_state.selected_poder}
            - Órgão: {st.session_state.selected_orgao}
            """)
        
        # Conteúdo principal
        st.title("Análise de Transparência")
        st.markdown(f"### {st.session_state.selected_orgao}")
        
        # Obtém os dados do órgão selecionado
        orgao_data = ORGAOS_DATA[st.session_state.selected_esfera][st.session_state.selected_poder][st.session_state.selected_orgao]
        
        # Tabs para diferentes análises
        tab1, tab2, tab3, tab4 = st.tabs(["📊 Status dos Sites", "🔍 Análise de Transparência", "📈 Relatório", "💾 Exportar"])
        
        with tab1:
            st.subheader("Status dos Sites")
            
            col1, col2 = st.columns(2)
            
            with col1:
                st.markdown("#### Site Oficial")
                with st.spinner("Verificando site oficial..."):
                    status, details = check_website_status(orgao_data["site"])
                    st.metric("Status", status)
                    st.caption(details)
                    if orgao_data["site"]:
                        st.code(orgao_data["site"])
            
            with col2:
                st.markdown("#### Portal da Transparência")
                with st.spinner("Verificando portal de transparência..."):
                    status, details = check_website_status(orgao_data["transparencia"])
                    st.metric("Status", status)
                    st.caption(details)
                    if orgao_data["transparencia"]:
                        st.code(orgao_data["transparencia"])
        
        with tab2:
            st.subheader("Análise de Elementos de Transparência")
            
            if orgao_data["transparencia"]:
                with st.spinner("Analisando elementos de transparência..."):
                    elements, found = analyze_transparency_elements(orgao_data["transparencia"])
                    
                    # Métricas gerais
                    col1, col2, col3 = st.columns(3)
                    with col1:
                        total_elements = len(elements)
                        st.metric("Total de Elementos", total_elements)
                    with col2:
                        found_count = sum(elements.values())
                        st.metric("Elementos Encontrados", found_count)
                    with col3:
                        compliance = (found_count / total_elements) * 100
                        st.metric("Conformidade", f"{compliance:.1f}%")
                    
                    # Detalhamento dos elementos
                    st.markdown("#### Elementos de Transparência")
                    
                    col1, col2 = st.columns(2)
                    items = list(elements.items())
                    half = len(items) // 2
                    
                    with col1:
                        for element, found in items[:half]:
                            if found:
                                st.success(f"✅ {element}")
                            else:
                                st.error(f"❌ {element}")
                    
                    with col2:
                        for element, found in items[half:]:
                            if found:
                                st.success(f"✅ {element}")
                            else:
                                st.error(f"❌ {element}")
            else:
                st.warning("URL do Portal de Transparência não disponível para análise.")
        
        with tab3:
            st.subheader("Relatório de Conformidade")
            
            # Gera relatório
            report_data = {
                "Órgão": st.session_state.selected_orgao,
                "Esfera": st.session_state.selected_esfera,
                "Poder": st.session_state.selected_poder,
                "Data da Análise": datetime.now().strftime("%d/%m/%Y %H:%M"),
                "Site Oficial": orgao_data["site"] or "Não disponível",
                "Portal Transparência": orgao_data["transparencia"] or "Não disponível"
            }
            
            # Adiciona status dos sites
            site_status, _ = check_website_status(orgao_data["site"])
            transp_status, _ = check_website_status(orgao_data["transparencia"])
            
            report_data["Status Site Oficial"] = site_status
            report_data["Status Portal Transparência"] = transp_status
            
            # Adiciona elementos de transparência
            if orgao_data["transparencia"]:
                elements, _ = analyze_transparency_elements(orgao_data["transparencia"])
                for element, found in elements.items():
                    report_data[f"Elemento - {element}"] = "Sim" if found else "Não"
            
            # Exibe relatório
            for key, value in report_data.items():
                st.write(f"**{key}:** {value}")
        
        with tab4:
            st.subheader("Exportar Dados")
            
            # Prepara dados para exportação
            export_data = []
            
            # Adiciona dados do órgão atual
            site_status, site_details = check_website_status(orgao_data["site"])
            transp_status, transp_details = check_website_status(orgao_data["transparencia"])
            
            row = {
                "Esfera": st.session_state.selected_esfera,
                "Poder": st.session_state.selected_poder,
                "Órgão": st.session_state.selected_orgao,
                "Site Oficial": orgao_data["site"] or "N/A",
                "Status Site": site_status,
                "Portal Transparência": orgao_data["transparencia"] or "N/A",
                "Status Portal": transp_status,
                "Data Análise": datetime.now().strftime("%d/%m/%Y %H:%M")
            }
            
            # Adiciona elementos de transparência
            if orgao_data["transparencia"]:
                elements, _ = analyze_transparency_elements(orgao_data["transparencia"])
                for element, found in elements.items():
                    row[element] = "Sim" if found else "Não"
            
            export_data.append(row)
            
            # Cria DataFrame
            df = pd.DataFrame(export_data)
            
            # Botão de download
            csv = df.to_csv(index=False, encoding='utf-8-sig')
            st.download_button(
                label="📥 Baixar Relatório CSV",
                data=csv,
                file_name=f"analise_transparencia_{st.session_state.selected_orgao.replace(' ', '_')}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv",
                mime="text/csv"
            )
            
            # Mostra preview dos dados
            st.markdown("#### Preview dos Dados")
            st.dataframe(df)

if __name__ == "__main__":
    main()