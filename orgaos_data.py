# orgaos_data.py
# Mapeamento Completo de Órgãos Públicos do Amazonas
# Este arquivo contém todos os órgãos públicos com seus respectivos sites e portais de transparência

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
                "site": "https://www.aleam.gov.br/",
                "transparencia": "https://www.aleam.gov.br/transparencia/"
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
                "site": "https://www2.tce.am.gov.br/",
                "transparencia": "https://transparencia.tce.am.gov.br/"
            }
        },
        "Ministério Público": {
            "Ministério Público MPE": {
                "site": "https://www.mpam.mp.br/",
                "transparencia": "https://www.mpam.mp.br/servicos/transparencia"
            }
        },
        "Defensoria": {
            "Defensoria DPE": {
                "site": "https://defensoria.am.def.br/",
                "transparencia": "https://transparencia.defensoria.am.def.br/"
            }
        },
        "Consórcios Públicos": {
            "Consórcio Interestadual de Desenvolvimento Sustentável da Amazônia Legal (CAL)": {
                "site": "https://www.consorcioamazonialegal.gov.br/",
                "transparencia": ""  # Exemplo de órgão sem portal de transparência listado
            }
        },
        "Estatais": {
            "Companhia de Saneamento do Amazonas – COSAMA": {
                "site": "https://cosama.am.gov.br/",
                "transparencia": "https://cosama.am.gov.br/informacao/"
            },
            "Processamento de Dados Amazonas S/A – PRODAM": {
                "site": "https://www.prodam.am.gov.br/",
                "transparencia": "https://prodam.am.gov.br/transparencia/"
            },
            "Companhia de Gás do Amazonas – CIGÁS": {
                "site": "https://www.cigas-am.com.br/",
                "transparencia": "https://www.cigas-am.com.br/acesso-a-informacao-lai"
            }
        }
    },
    "Municipal": {
        "Poder Executivo": {
            # Prefeituras dos Municípios do Amazonas (LISTA COMPLETA)
            "Prefeitura de Manaus (PMM)": {
                "site": "https://www.manaus.am.gov.br/", 
                "transparencia": "https://transparencia.manaus.am.gov.br/"
            },
            "Prefeitura de Itacoatiara": {
                "site": "https://prefeituradeitacoatiara.com.br/", 
                "transparencia": "https://prefeituradeitacoatiara.com.br/transparencia"
            },
            "Prefeitura de Parintins": {
                "site": "https://parintins.am.gov.br/", 
                "transparencia": "https://transparencia.parintins.am.gov.br/"
            },
            "Prefeitura de Manacapuru": {
                "site": "https://manacapuru.am.gov.br/", 
                "transparencia": "https://transparencia.betha.cloud/#/c__jWVln4DUOYDYfhXSJnA=="
            },
            "Prefeitura de Coari": {
                "site": "https://coari.am.gov.br/", 
                "transparencia": "https://transparencia.coari.am.gov.br/"
            },
            "Prefeitura de Tefé": {
                "site": "https://tefe.am.gov.br/", 
                "transparencia": "https://transparenciamunicipalaam.org.br/p/tefe"
            },
            "Prefeitura de Maués": {
                "site": "https://www.maues.am.gov.br/", 
                "transparencia": "http://sistemasweb.inf.br:8060/transparencia/"
            },
            "Prefeitura de Eirunepé": {
                "site": "Não informado", 
                "transparencia": "https://transparenciamunicipalaam.org.br/p/eirunepe"
            },
            "Prefeitura de Humaitá": {
                "site": "https://humaita.am.gov.br/", 
                "transparencia": "https://humaita.am.gov.br/transparencia/"
            },
            "Prefeitura de Lábrea": {
                "site": "https://labrea.am.gov.br/", 
                "transparencia": "http://transparencia-labrea.org/"
            },
            "Prefeitura de Manicoré": {
                "site": "https://manicore.am.gov.br/", 
                "transparencia": "https://manicore.am.gov.br/portal-da-transparencia/"
            },
            "Prefeitura de Borba": {
                "site": "https://borba.am.gov.br/", 
                "transparencia": "https://borba.am.gov.br/portal-transparencia/"
            },
            "Prefeitura de Presidente Figueiredo": {
                "site": "https://presidentefigueiredo.am.gov.br/", 
                "transparencia": "https://www.presidentefigueiredo.am.gov.br/transparencia/"
            },
            "Prefeitura de Carauari": {
                "site": "https://carauari.am.gov.br/", 
                "transparencia": "https://carauari.am.gov.br/transparencia/"
            },
            "Prefeitura de Benjamin Constant": {
                "site": "https://benjaminconstant.am.gov.br/", 
                "transparencia": "https://benjaminconstant.am.gov.br/transparencia/?transparencia.html"
            },
            "Prefeitura de Boca do Acre": {
                "site": "https://bocadoacre.am.gov.br/", 
                "transparencia": "https://transparenciamunicipalaam.org.br/p/bocadoacre"
            },
            "Prefeitura de Careiro": {
                "site": "Em Manutencão https://careiro.am.gov.br/", 
                "transparencia": "Em Manutencão https://www.careiro.am.gov.br/portal-transparencia/"
            },
            "Prefeitura de Iranduba": {
                "site": "https://www.iranduba.am.gov.br/", 
                "transparencia": "https://transparencia.betha.cloud/#/yVVW6OAco0wQSzK_WdkkFg=="
            },
            "Prefeitura de Rio Preto da Eva": {
                "site": "https://riopretodaeva.am.gov.br/", 
                "transparencia": "https://riopretodaeva.am.gov.br/portal-da-transparencia/"
            },
            "Prefeitura de Autazes": {
                "site": "https://autazes.am.gov.br/", 
                "transparencia": "https://www.perseusdata2.com/pmautazes/"
            },
            "Prefeitura de Barcelos": {
                "site": "Index of https://barcelos.am.gov.br/", 
                "transparencia": "https://transparenciamunicipalaam.org.br/p/barcelos"
            },
            "Prefeitura de Fonte Boa": {
                "site": "Index of https://fonteboa.am.gov.br/", 
                "transparencia": "https://transparenciamunicipalaam.org.br/p/fonte-boa"
            },
            "Prefeitura de Guajará": {
                "site": "https://guajara.am.gov.br/", 
                "transparencia": "https://guajara.am.gov.br/portal-transparencia/"
            },
            "Prefeitura de Jutaí": {
                "site": "https://jutai.am.gov.br/", 
                "transparencia": "https://jutai.am.gov.br/portal-transparencia/"
            },
            "Prefeitura de Novo Airão": {
                "site": "https://novoairao.am.gov.br/", 
                "transparencia": "https://transparenciamunicipalaam.org.br/p/novo-airao"
            },
            "Prefeitura de Santo Antônio do Içá": {
                "site": "Index of https://santoantoniodoica.am.gov.br/", 
                "transparencia": "https://transparenciamunicipalaam.org.br/p/santo-antonio-do-ica"
            },
            "Prefeitura de São Gabriel da Cachoeira": {
                "site": "Não informado ou indisponível", 
                "transparencia": "https://transparenciamunicipalaam.org.br/p/sao-gabriel-da-cachoeira"
            },
            "Prefeitura de Tabatinga": {
                "site": "https://tabatinga.am.gov.br/", 
                "transparencia": "https://www.tabatinga.am.gov.br/transparencia/"
            },
            "Prefeitura de Urucará": {
                "site": "https://urucara.am.gov.br/", 
                "transparencia": "https://urucara.am.gov.br/transparencia/"
            },
            "Prefeitura de Atalaia do Norte": {
                "site": "https://atalaiadonorte.am.gov.br/", 
                "transparencia": "https://atalaiadonorte.am.gov.br/transparencia/"
            },
            "Prefeitura de Barreirinha": {
                "site": "https://barreirinha.am.gov.br/", 
                "transparencia": "https://barreirinha.am.gov.br/transparencia/"
            },
            "Prefeitura de Boa Vista do Ramos": {
                "site": "não informado ou indisponível", 
                "transparencia": "https://transparenciamunicipalaam.org.br/p/boavistadoramos"
            },
            "Prefeitura de Caapiranga": {
                "site": "https://caapiranga.am.gov.br/", 
                "transparencia": "https://transparenciamunicipalaam.org.br/p/caapiranga"
            },
            "Prefeitura de Canutama": {
                "site": "Index of https://canutama.am.gov.br/", 
                "transparencia": "https://transparenciamunicipalaam.org.br/p/canutama"
            },
            "Prefeitura de Careiro da Várzea": {
                "site": "https://careirodavarzea.am.gov.br/", 
                "transparencia": "https://careirodavarzea.am.gov.br/transparencia/"
            },
            "Prefeitura de Codajás": {
                "site": "https://codajas.am.gov.br/", 
                "transparencia": "https://transparenciamunicipalaam.org.br/p/codajas"
            },
            "Prefeitura de Envira": {
                "site": "https://envira.am.gov.br/ Site em Manutenção", 
                "transparencia": "https://transparenciamunicipalaam.org.br/p/envira"
            },
            "Prefeitura de Ipixuna": {
                "site": "https://ipixuna.am.gov.br/", 
                "transparencia": "https://portaldatransparencia.gov.br/localidades/1301803-ipixuna"
            },
            "Prefeitura de Itamarati": {
                "site": "Não informado ou indisponível", 
                "transparencia": "https://transparenciamunicipalaam.org.br/p/itamarati"
            },
            "Prefeitura de Japurá": {
                "site": "Não informado ou indisponível", 
                "transparencia": "https://transparenciamunicipalaam.org.br/p/japura"
            },
            "Prefeitura de Maraã": {
                "site": "https://maraa.am.gov.br/", 
                "transparencia": "https://www.maraa.am.gov.br/transparencia/"
            },
            "Prefeitura de Nhamundá": {
                "site": "https://nhamunda.am.gov.br/", 
                "transparencia": "https://nhamunda.am.gov.br/portal-da-transparencia/"
            },
            "Prefeitura de Nova Olinda do Norte": {
                "site": "https://novaolindadonorte.am.gov.br/", 
                "transparencia": "https://transparenciamunicipalaam.org.br/p/nova-olinda-do-norte"
            },
            "Prefeitura de Pauini": {
                "site": "https://pauini.am.gov.br/", 
                "transparencia": "https://transparenciamunicipalaam.org.br/p/pauini"
            },
            "Prefeitura de São Paulo de Olivença": {
                "site": "Não informado ou indisponível", 
                "transparencia": "https://transparenciamunicipalaam.org.br/p/sao-paulo-de-olivenca"
            },
            "Prefeitura de Silves": {
                "site": "https://silves.am.gov.br/", 
                "transparencia": "https://transparenciamunicipalaam.org.br/p/silves"
            },
            "Prefeitura de Tonantins": {
                "site": "https://tonantins.am.gov.br/", 
                "transparencia": "https://tonantins.am.gov.br/transparencia/"
            },
            "Prefeitura de Urucurituba": {
                "site": "https://urucurituba.am.gov.br/", 
                "transparencia": "https://transparenciamunicipalaam.org.br/p/urucurituba"
            },
            "Prefeitura de Alvarães": {
                "site": "Não informado ou indisponível", 
                "transparencia": "https://transparenciamunicipalaam.org.br/p/alvaraes"
            },
            "Prefeitura de Amaturá": {
                "site": "https://amatura.am.gov.br/", 
                "transparencia": "https://amatura.am.gov.br/transparencia/"
            },
            "Prefeitura de Anamã": {
                "site": "https://anama.am.gov.br/", 
                "transparencia": "https://anama.am.gov.br/transparencia/"
            },
            "Prefeitura de Anori": {
                "site": "Não informado ou indisponível", 
                "transparencia": "https://transparenciamunicipalaam.org.br/p/anori"
            },
            "Prefeitura de Apuí": {
                "site": "https://apui.am.gov.br/", 
                "transparencia": "https://apui.am.gov.br/portal-da-transparencia/"
            },
            "Prefeitura de Beruri": {
                "site": "https://pmberuri.am.gov.br/", 
                "transparencia": "https://pmberuri.am.gov.br/transparencia/"
            }
        },
        "Poder Legislativo": {
            # Câmaras Municipais dos Municípios do Amazonas (LISTA COMPLETA)
            "Câmara de Manaus": {
                "site": "https://www.cmm.am.gov.br/", 
                "transparencia": "https://transparencia.cmm.am.gov.br/"
            },
            "Câmara Municipal de Itacoatiara": {
                "site": "https://www.cmitacoatiara.am.gov.br/", 
                "transparencia": "https://www.cmitacoatiara.am.gov.br/portal-da-transparencia/"
            },
            "Câmara Municipal de Parintins": {
                "site": "https://camaraparintins.am.gov.br/", 
                "transparencia": "https://camaraparintins.am.gov.br/portal-transparencia/"
            },
            "Câmara Municipal de Manacapuru": {
                "site": "https://cmmanacapuru.am.gov.br/", 
                "transparencia": "https://cmmanacapuru.am.gov.br/portal-transparencia/"
            },
            "Câmara Municipal de Coari": {
                "site": "https://cmcoari.am.gov.br/", 
                "transparencia": "https://cmcoari.am.gov.br/portal-transparencia/"
            },
            "Câmara Municipal de Tefé": {
                "site": "https://cmtefe.am.gov.br/", 
                "transparencia": "https://cmtefe.am.gov.br/portal-transparencia/"
            },
            "Câmara Municipal de Maués": {
                "site": "https://cammaues.am.gov.br/", 
                "transparencia": "https://cammaues.am.gov.br/portal-transparencia/"
            },
            "Câmara Municipal de Eirunepé": {
                "site": "https://cmeirunepe.am.gov.br/", 
                "transparencia": "https://cmeirunepe.am.gov.br/portal-transparencia/"
            },
            "Câmara Municipal de Humaitá": {
                "site": "https://cmhumaita.am.gov.br/", 
                "transparencia": "https://cmhumaita.am.gov.br/portal-transparencia/"
            },
            "Câmara Municipal de Lábrea": {
                "site": "https://cmlabrea.am.gov.br/", 
                "transparencia": "https://cmlabrea.am.gov.br/portal-transparencia/"
            },
            "Câmara Municipal de Manicoré": {
                "site": "https://cmmanicore.am.gov.br/", 
                "transparencia": "https://cmmanicore.am.gov.br/portal-transparencia/"
            },
            "Câmara Municipal de Borba": {
                "site": "https://cmborba.am.gov.br/", 
                "transparencia": "https://cmborba.am.gov.br/portal-transparencia/"
            },
            "Câmara Municipal de Presidente Figueiredo": {
                "site": "https://cmpresidentefigueiredo.am.gov.br/", 
                "transparencia": "https://cmpresidentefigueiredo.am.gov.br/portal-transparencia/"
            },
            "Câmara Municipal de Carauari": {
                "site": "https://cmcarauari.am.gov.br/", 
                "transparencia": "https://cmcarauari.am.gov.br/portal-transparencia/"
            },
            "Câmara Municipal de Benjamin Constant": {
                "site": "https://cmbenjaminconstant.am.gov.br/", 
                "transparencia": "https://cmbenjaminconstant.am.gov.br/portal-transparencia/"
            },
            "Câmara Municipal de Boca do Acre": {
                "site": "https://cmbocadoacre.am.gov.br/", 
                "transparencia": "https://cmbocadoacre.am.gov.br/portal-transparencia/"
            },
            "Câmara Municipal de Careiro": {
                "site": "https://cmcareiro.am.gov.br/", 
                "transparencia": "https://cmcareiro.am.gov.br/portal-transparencia/"
            },
            "Câmara Municipal de Iranduba": {
                "site": "https://cmiranduba.am.gov.br/", 
                "transparencia": "https://cmiranduba.am.gov.br/portal-transparencia/"
            },
            "Câmara Municipal de Rio Preto da Eva": {
                "site": "https://cmriopretodaeva.am.gov.br/", 
                "transparencia": "https://cmriopretodaeva.am.gov.br/portal-transparencia/"
            },
            "Câmara Municipal de Autazes": {
                "site": "https://cmautazes.am.gov.br/", 
                "transparencia": "https://cmautazes.am.gov.br/portal-transparencia/"
            },
            "Câmara Municipal de Barcelos": {
                "site": "https://cmbarcelos.am.gov.br/", 
                "transparencia": "https://cmbarcelos.am.gov.br/portal-transparencia/"
            },
            "Câmara Municipal de Fonte Boa": {
                "site": "https://cmfonteboa.am.gov.br/", 
                "transparencia": "https://cmfonteboa.am.gov.br/portal-transparencia/"
            },
            "Câmara Municipal de Guajará": {
                "site": "https://cmguajara.am.gov.br/", 
                "transparencia": "https://cmguajara.am.gov.br/portal-transparencia/"
            },
            "Câmara Municipal de Jutaí": {
                "site": "https://cmjutai.am.gov.br/", 
                "transparencia": "https://cmjutai.am.gov.br/portal-transparencia/"
            },
            "Câmara Municipal de Novo Airão": {
                "site": "https://cmnovoairao.am.gov.br/", 
                "transparencia": "https://cmnovoairao.am.gov.br/portal-transparencia/"
            },
            "Câmara Municipal de Santo Antônio do Içá": {
                "site": "https://cmsantoantoniodoica.am.gov.br/", 
                "transparencia": "https://cmsantoantoniodoica.am.gov.br/portal-transparencia/"
            },
            "Câmara Municipal de São Gabriel da Cachoeira": {
                "site": "https://cmsaogabriel.am.gov.br/", 
                "transparencia": "https://cmsaogabriel.am.gov.br/portal-transparencia/"
            },
            "Câmara Municipal de Tabatinga": {
                "site": "https://cmtabatinga.am.gov.br/", 
                "transparencia": "https://cmtabatinga.am.gov.br/portal-transparencia/"
            },
            "Câmara Municipal de Urucará": {
                "site": "https://cmurucara.am.gov.br/", 
                "transparencia": "https://cmurucara.am.gov.br/portal-transparencia/"
            },
            "Câmara Municipal de Atalaia do Norte": {
                "site": "https://cmatalaiadonorte.am.gov.br/", 
                "transparencia": "https://cmatalaiadonorte.am.gov.br/portal-transparencia/"
            },
            "Câmara Municipal de Barreirinha": {
                "site": "https://cmbarreirinha.am.gov.br/", 
                "transparencia": "https://cmbarreirinha.am.gov.br/portal-transparencia/"
            },
            "Câmara Municipal de Boa Vista do Ramos": {
                "site": "https://cmboavistadoramos.am.gov.br/", 
                "transparencia": "https://cmboavistadoramos.am.gov.br/portal-transparencia/"
            },
            "Câmara Municipal de Caapiranga": {
                "site": "https://cmcaapiranga.am.gov.br/", 
                "transparencia": "https://cmcaapiranga.am.gov.br/portal-transparencia/"
            },
            "Câmara Municipal de Canutama": {
                "site": "https://cmcanutama.am.gov.br/", 
                "transparencia": "https://cmcanutama.am.gov.br/portal-transparencia/"
            },
            "Câmara Municipal de Careiro da Várzea": {
                "site": "https://cmcareirodavazea.am.gov.br/", 
                "transparencia": "https://cmcareirodavazea.am.gov.br/portal-transparencia/"
            },
            "Câmara Municipal de Codajás": {
                "site": "https://cmcodajas.am.gov.br/", 
                "transparencia": "https://cmcodajas.am.gov.br/portal-transparencia/"
            },
            "Câmara Municipal de Envira": {
                "site": "https://cmenvira.am.gov.br/", 
                "transparencia": "https://cmenvira.am.gov.br/portal-transparencia/"
            },
            "Câmara Municipal de Ipixuna": {
                "site": "https://cmipixuna.am.gov.br/", 
                "transparencia": "https://cmipixuna.am.gov.br/portal-transparencia/"
            },
            "Câmara Municipal de Itamarati": {
                "site": "https://cmitamarati.am.gov.br/", 
                "transparencia": "https://cmitamarati.am.gov.br/portal-transparencia/"
            },
            "Câmara Municipal de Japurá": {
                "site": "https://cmjapura.am.gov.br/", 
                "transparencia": "https://cmjapura.am.gov.br/portal-transparencia/"
            },
            "Câmara Municipal de Maraã": {
                "site": "https://cmmaraa.am.gov.br/", 
                "transparencia": "https://cmmaraa.am.gov.br/portal-transparencia/"
            },
            "Câmara Municipal de Nhamundá": {
                "site": "https://cmnhamunda.am.gov.br/", 
                "transparencia": "https://cmnhamunda.am.gov.br/portal-transparencia/"
            },
            "Câmara Municipal de Nova Olinda do Norte": {
                "site": "https://cmnovaolindadonorte.am.gov.br/", 
                "transparencia": "https://cmnovaolindadonorte.am.gov.br/portal-transparencia/"
            },
            "Câmara Municipal de Pauini": {
                "site": "https://cmpauini.am.gov.br/", 
                "transparencia": "https://cmpauini.am.gov.br/portal-transparencia/"
            },
            "Câmara Municipal de São Paulo de Olivença": {
                "site": "https://cmsaopaulodeolivenca.am.gov.br/", 
                "transparencia": "https://cmsaopaulodeolivenca.am.gov.br/portal-transparencia/"
            },
            "Câmara Municipal de Silves": {
                "site": "https://cmsilves.am.gov.br/", 
                "transparencia": "https://cmsilves.am.gov.br/portal-transparencia/"
            },
            "Câmara Municipal de Tonantins": {
                "site": "https://cmtonantins.am.gov.br/", 
                "transparencia": "https://cmtonantins.am.gov.br/portal-transparencia/"
            },
            "Câmara Municipal de Urucurituba": {
                "site": "https://cmurucurituba.am.gov.br/", 
                "transparencia": "https://cmurucurituba.am.gov.br/portal-transparencia/"
            },
            "Câmara Municipal de Alvarães": {
                "site": "https://cmalvaraes.am.gov.br/", 
                "transparencia": "https://cmalvaraes.am.gov.br/portal-transparencia/"
            },
            "Câmara Municipal de Amaturá": {
                "site": "https://cmamatura.am.gov.br/", 
                "transparencia": "https://cmamatura.am.gov.br/portal-transparencia/"
            },
            "Câmara Municipal de Anamã": {
                "site": "https://cmanama.am.gov.br/", 
                "transparencia": "https://cmanama.am.gov.br/portal-transparencia/"
            },
            "Câmara Municipal de Anori": {
                "site": "https://cmanori.am.gov.br/", 
                "transparencia": "https://cmanori.am.gov.br/portal-transparencia/"
            },
            "Câmara Municipal de Apuí": {
                "site": "https://cmapui.am.gov.br/", 
                "transparencia": "https://cmapui.am.gov.br/portal-transparencia/"
            },
            "Câmara Municipal de Beruri": {
                "site": "https://cmberuri.am.gov.br/", 
                "transparencia": "https://cmberuri.am.gov.br/portal-transparencia/"
            }
        }
    }
}

# Funções auxiliares para trabalhar com os dados
def obter_orgaos_por_esfera(esfera):
    """
    Obtém todos os órgãos de uma esfera específica
    
    Args:
        esfera (str): "Estadual" ou "Municipal"
        
    Returns:
        dict: Dicionário com os órgãos da esfera
    """
    return ORGAOS_DATA.get(esfera, {})

def obter_orgaos_por_poder(esfera, poder):
    """
    Obtém todos os órgãos de um poder específico
    
    Args:
        esfera (str): "Estadual" ou "Municipal"
        poder (str): Nome do poder
        
    Returns:
        dict: Dicionário com os órgãos do poder
    """
    return ORGAOS_DATA.get(esfera, {}).get(poder, {})

def obter_dados_orgao(esfera, poder, orgao):
    """
    Obtém os dados de um órgão específico
    
    Args:
        esfera (str): "Estadual" ou "Municipal"
        poder (str): Nome do poder
        orgao (str): Nome do órgão
        
    Returns:
        dict: Dicionário com site e transparencia do órgão
    """
    return ORGAOS_DATA.get(esfera, {}).get(poder, {}).get(orgao, {})

def listar_todos_orgaos():
    """
    Lista todos os órgãos cadastrados
    
    Returns:
        list: Lista de dicionários com informações de todos os órgãos
    """
    orgaos = []
    for esfera, poderes in ORGAOS_DATA.items():
        for poder, orgaos_poder in poderes.items():
            for orgao, dados in orgaos_poder.items():
                orgaos.append({
                    'esfera': esfera,
                    'poder': poder,
                    'orgao': orgao,
                    'site': dados.get('site', ''),
                    'transparencia': dados.get('transparencia', '')
                })
    return orgaos

def obter_estatisticas_orgaos():
    """
    Obtém estatísticas dos órgãos cadastrados
    
    Returns:
        dict: Estatísticas dos órgãos
    """
    stats = {
        'total_orgaos': 0,
        'por_esfera': {},
        'por_poder': {},
        'com_transparencia': 0,
        'sem_transparencia': 0
    }
    
    for esfera, poderes in ORGAOS_DATA.items():
        stats['por_esfera'][esfera] = 0
        for poder, orgaos_poder in poderes.items():
            if poder not in stats['por_poder']:
                stats['por_poder'][poder] = 0
            
            count_poder = len(orgaos_poder)
            stats['por_esfera'][esfera] += count_poder
            stats['por_poder'][poder] += count_poder
            stats['total_orgaos'] += count_poder
            
            # Conta órgãos com/sem transparência
            for dados in orgaos_poder.values():
                if dados.get('transparencia'):
                    stats['com_transparencia'] += 1
                else:
                    stats['sem_transparencia'] += 1
    
    return stats

def buscar_orgaos_por_nome(termo_busca):
    """
    Busca órgãos por nome
    
    Args:
        termo_busca (str): Termo para buscar nos nomes dos órgãos
        
    Returns:
        list: Lista de órgãos que contêm o termo
    """
    resultados = []
    termo_lower = termo_busca.lower()
    
    for esfera, poderes in ORGAOS_DATA.items():
        for poder, orgaos_poder in poderes.items():
            for orgao, dados in orgaos_poder.items():
                if termo_lower in orgao.lower():
                    resultados.append({
                        'esfera': esfera,
                        'poder': poder,
                        'orgao': orgao,
                        'site': dados.get('site', ''),
                        'transparencia': dados.get('transparencia', '')
                    })
    
    return resultados

def validar_urls_orgaos():
    """
    Valida se todas as URLs estão preenchidas corretamente
    
    Returns:
        dict: Relatório de validação
    """
    relatorio = {
        'total_orgaos': 0,
        'urls_site_ok': 0,
        'urls_site_vazias': 0,
        'urls_transparencia_ok': 0,
        'urls_transparencia_vazias': 0,
        'orgaos_sem_transparencia': []
    }
    
    for esfera, poderes in ORGAOS_DATA.items():
        for poder, orgaos_poder in poderes.items():
            for orgao, dados in orgaos_poder.items():
                relatorio['total_orgaos'] += 1
                
                # Verifica site
                if dados.get('site'):
                    relatorio['urls_site_ok'] += 1
                else:
                    relatorio['urls_site_vazias'] += 1
                
                # Verifica transparência
                if dados.get('transparencia'):
                    relatorio['urls_transparencia_ok'] += 1
                else:
                    relatorio['urls_transparencia_vazias'] += 1
                    relatorio['orgaos_sem_transparencia'].append({
                        'esfera': esfera,
                        'poder': poder,
                        'orgao': orgao
                    })
    
    return relatorio

# Constantes úteis
ESFERAS_DISPONIVEIS = list(ORGAOS_DATA.keys())
PODERES_ESTADUAIS = list(ORGAOS_DATA.get('Estadual', {}).keys())
PODERES_MUNICIPAIS = list(ORGAOS_DATA.get('Municipal', {}).keys())

# Exemplo de uso
if __name__ == "__main__":
    # Exemplo 1: Obter estatísticas
    stats = obter_estatisticas_orgaos()
    print("=== Estatísticas dos Órgãos ===")
    print(f"Total de órgãos: {stats['total_orgaos']}")
    print(f"Por esfera: {stats['por_esfera']}")
    print(f"Com portal de transparência: {stats['com_transparencia']}")
    print(f"Sem portal de transparência: {stats['sem_transparencia']}")
    
    # Exemplo 2: Buscar órgãos
    resultados_manaus = buscar_orgaos_por_nome("Manaus")
    print(f"\n=== Órgãos de Manaus: {len(resultados_manaus)} encontrados ===")
    for resultado in resultados_manaus:
        print(f"- {resultado['orgao']} ({resultado['poder']})")
    
    # Exemplo 3: Validar URLs
    validacao = validar_urls_orgaos()
    print(f"\n=== Validação de URLs ===")
    print(f"Órgãos sem portal de transparência: {validacao['urls_transparencia_vazias']}")
    if validacao['orgaos_sem_transparencia']:
        print("Órgãos sem transparência:")
        for org in validacao['orgaos_sem_transparencia'][:3]:  # Mostra apenas os 3 primeiros
            print(f"  - {org['orgao']} ({org['poder']})")