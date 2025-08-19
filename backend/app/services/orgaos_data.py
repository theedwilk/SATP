# orgaos_data.py
# Mapeamento Completo de Órgãos Públicos do Amazonas
# Este arquivo contém todos os órgãos públicos com seus respectivos sites, portais de transparência e dados de localização atualizados.

ORGAOS_DATA = {
    "Estadual": {
        "Poder Executivo": {
            "Governo do Estado do Amazonas": {
                "site": "https://www.amazonas.am.gov.br/",
                "transparencia": "https://www.transparencia.am.gov.br/",
                "endereco": "Avenida Brasil, 3925 - Compensa, Manaus - AM",
                "cep": "69036-110",
                "coordenadas": {
                    "latitude": -3.1095,
                    "longitude": -60.0733
                }
            }
        },
        "Poder Legislativo": {
            "Assembleia Legislativa (ALEAM)": {
                "site": "https://www.aleam.gov.br/",
                "transparencia": "https://www.aleam.gov.br/transparencia/",
                "endereco": "Avenida Mário Ypiranga Monteiro, 3950 - Parque 10 de Novembro, Manaus - AM",
                "cep": "69057-002",
                "coordenadas": {
                    "latitude": -3.0861,
                    "longitude": -60.0584
                }
            }
        },
        "Poder Judiciário": {
            "Tribunal de Justiça TJAM": {
                "site": "https://www.tjam.jus.br/",
                "transparencia": "https://www.tjam.jus.br/index.php/transparencia",
                "endereco": "Avenida André Araújo, s/n - Aleixo, Manaus - AM",
                "cep": "69060-000",
                "coordenadas": {
                    "latitude": -3.1118,
                    "longitude": -60.0076
                }
            }
        },
        "Tribunal de Contas": {
            "Tribunal de Contas TCE": {
                "site": "https://www2.tce.am.gov.br/",
                "transparencia": "https://transparencia.tce.am.gov.br/",
                "endereco": "Avenida Efigênio Salles, 1155 - Aleixo, Manaus - AM",
                "cep": "69050-020",
                "coordenadas": {
                    "latitude": -3.0975,
                    "longitude": -60.0163
                }
            }
        },
        "Ministério Público": {
            "Ministério Público MPE": {
                "site": "https://www.mpam.mp.br/",
                "transparencia": "https://www.mpam.mp.br/servicos/transparencia",
                "endereco": "Avenida Coronel Teixeira, 7995 - Nova Esperança, Manaus - AM",
                "cep": "69037-000",
                "coordenadas": {
                    "latitude": -3.0950,
                    "longitude": -60.0725
                }
            }
        },
        "Defensoria": {
            "Defensoria DPE": {
                "site": "https://defensoria.am.def.br/",
                "transparencia": "https://transparencia.defensoria.am.def.br/",
                "endereco": "Avenida André Araújo, 679 - Aleixo, Manaus - AM",
                "cep": "69060-001",
                "coordenadas": {
                    "latitude": -3.1121,
                    "longitude": -60.0117
                }
            }
        },
        "Consórcios Públicos": {
            "Consórcio Interestadual de Desenvolvimento Sustentável da Amazônia Legal (CAL)": {
                "site": "https://www.consorcioamazonialegal.gov.br/",
                "transparencia": "https://www.consorcioamazonialegal.gov.br/transparencia/",
                "endereco": "Avenida Brasil, 3925 - Compensa, Manaus - AM (Sede do Governo do Amazonas)",
                "cep": "69036-110",
                "coordenadas": {
                    "latitude": -3.1095,
                    "longitude": -60.0733
                }
            }
        },
        "Estatais": {
            "Companhia de Saneamento do Amazonas – COSAMA": {
                "site": "https://cosama.am.gov.br/",
                "transparencia": "https://cosama.am.gov.br/informacao/",
                "endereco": "Avenida Governador Danilo de Matos Areosa, 131 - Distrito Industrial I, Manaus - AM",
                "cep": "69075-351",
                "coordenadas": {
                    "latitude": -3.1321,
                    "longitude": -59.9575
                }
            },
            "Processamento de Dados Amazonas S/A – PRODAM": {
                "site": "https://www.prodam.am.gov.br/",
                "transparencia": "https://prodam.am.gov.br/transparencia/",
                "endereco": "Avenida Djalma Batista, 3578 - Flores, Manaus - AM",
                "cep": "69050-010",
                "coordenadas": {
                    "latitude": -3.0789,
                    "longitude": -60.0211
                }
            },
            "Companhia de Gás do Amazonas – CIGÁS": {
                "site": "https://www.cigas-am.com.br/",
                "transparencia": "https://www.cigas-am.com.br/acesso-a-informacao-lai",
                "endereco": "Avenida Djalma Batista, 98 - A - Chapada, Manaus - AM",
                "cep": "69050-010",
                "coordenadas": {
                    "latitude": -3.1042,
                    "longitude": -60.0264
                }
            }
        }
    },
    "Municipal": {
        "Poder Executivo": {
            "Prefeitura de Manaus (PMM)": {
                "site": "https://www.manaus.am.gov.br/",
                "transparencia": "https://transparencia.manaus.am.gov.br/",
                "endereco": "Avenida Brasil, 2971 - Compensa, Manaus - AM",
                "cep": "69036-110",
                "coordenadas": {
                    "latitude": -3.1077,
                    "longitude": -60.0553
                }
            },
            "Prefeitura de Itacoatiara": {
                "site": "https://prefeituradeitacoatiara.com.br/",
                "transparencia": "https://prefeituradeitacoatiara.com.br/transparencia",
                "endereco": "Rua Dr. Luzardo Ferreira de Melo, 2469 - Centro, Itacoatiara - AM",
                "cep": "69100-057",
                "coordenadas": {
                    "latitude": -3.1415,
                    "longitude": -58.4442
                }
            },
            "Prefeitura de Parintins": {
                "site": "https://parintins.am.gov.br/",
                "transparencia": "https://transparencia.parintins.am.gov.br/",
                "endereco": "Rua Jonathas Pedrosa, 170 - Centro, Parintins - AM",
                "cep": "69151-160",
                "coordenadas": {
                    "latitude": -2.6280,
                    "longitude": -56.7358
                }
            },
            "Prefeitura de Manacapuru": {
                "site": "https://manacapuru.am.gov.br/",
                "transparencia": "https://transparencia.betha.cloud/#/c__jWVln4DUOYDYfhXSJnA==",
                "endereco": "Boulevard Pedro Rates, 1216 - Centro, Manacapuru - AM",
                "cep": "69400-245",
                "coordenadas": {
                    "latitude": -3.2999,
                    "longitude": -60.6209
                }
            },
            "Prefeitura de Coari": {
                "site": "https://coari.am.gov.br/",
                "transparencia": "https://transparencia.coari.am.gov.br/",
                "endereco": "Rua 27 de Outubro, s/n - Centro, Coari - AM",
                "cep": "69460-000",
                "coordenadas": {
                    "latitude": -4.0850,
                    "longitude": -63.1414
                }
            },
            "Prefeitura de Tefé": {
                "site": "https://tefe.am.gov.br/",
                "transparencia": "https://transparenciamunicipalaam.org.br/p/tefe",
                "endereco": "Estrada do Bexiga, 1008 - Jerusalém, Tefé - AM",
                "cep": "69553-240",
                "coordenadas": {
                    "latitude": -3.3664,
                    "longitude": -64.7230
                }
            },
            "Prefeitura de Maués": {
                "site": "https://www.maues.am.gov.br/",
                "transparencia": "http://sistemasweb.inf.br:8060/transparencia/",
                "endereco": "Praça Coronel João Verçosa, s/n - Centro, Maués - AM",
                "cep": "69190-000",
                "coordenadas": {
                    "latitude": -3.3860,
                    "longitude": -57.7185
                }
            },
            "Prefeitura de Eirunepé": {
                "site": "https://eirunepe.am.gov.br/",
                "transparencia": "https://transparenciamunicipalaam.org.br/p/eirunepe",
                "endereco": "Avenida Getúlio Vargas, 615 - Centro, Eirunepé - AM",
                "cep": "69880-000",
                "coordenadas": {
                    "latitude": -6.6603,
                    "longitude": -69.8741
                }
            },
            "Prefeitura de Humaitá": {
                "site": "https://humaita.am.gov.br/",
                "transparencia": "https://humaita.am.gov.br/transparencia/",
                "endereco": "Rua Municipal, 276 - Centro, Humaitá - AM",
                "cep": "69800-000",
                "coordenadas": {
                    "latitude": -7.5064,
                    "longitude": -63.0210
                }
            },
            "Prefeitura de Lábrea": {
                "site": "https://labrea.am.gov.br/",
                "transparencia": "https://labrea.am.gov.br/transparencia/",
                "endereco": "Avenida Vinte e Oito de Março, 332 - Centro, Lábrea - AM",
                "cep": "69830-000",
                "coordenadas": {
                    "latitude": -7.2592,
                    "longitude": -64.7977
                }
            },
            "Prefeitura de Manicoré": {
                "site": "https://manicore.am.gov.br/",
                "transparencia": "https://manicore.am.gov.br/portal-da-transparencia/",
                "endereco": "Avenida Getúlio Vargas, 350 - Centro, Manicoré - AM",
                "cep": "69280-000",
                "coordenadas": {
                    "latitude": -5.8092,
                    "longitude": -61.3008
                }
            },
            "Prefeitura de Borba": {
                "site": "https://borba.am.gov.br/",
                "transparencia": "https://borba.am.gov.br/portal-transparencia/",
                "endereco": "Rua Três de Fevereiro, 1 - Centro, Borba - AM",
                "cep": "69200-000",
                "coordenadas": {
                    "latitude": -4.3881,
                    "longitude": -59.5938
                }
            },
            "Prefeitura de Presidente Figueiredo": {
                "site": "https://presidentefigueiredo.am.gov.br/",
                "transparencia": "https://www.presidentefigueiredo.am.gov.br/transparencia/",
                "endereco": "Avenida Acari, s/n - Centro, Presidente Figueiredo - AM",
                "cep": "69735-000",
                "coordenadas": {
                    "latitude": -2.0307,
                    "longitude": -60.0248
                }
            },
            "Prefeitura de Carauari": {
                "site": "https://carauari.am.gov.br/",
                "transparencia": "https://carauari.am.gov.br/transparencia/",
                "endereco": "Praça de São Sebastião, 23 - Centro, Carauari - AM",
                "cep": "69500-000",
                "coordenadas": {
                    "latitude": -4.8833,
                    "longitude": -66.8958
                }
            },
            "Prefeitura de Benjamin Constant": {
                "site": "https://benjaminconstant.am.gov.br/",
                "transparencia": "https://benjaminconstant.am.gov.br/transparencia/",
                "endereco": "Rua General Sampaio, 252 - Centro, Benjamin Constant - AM",
                "cep": "69630-000",
                "coordenadas": {
                    "latitude": -4.3753,
                    "longitude": -70.0321
                }
            },
            "Prefeitura de Boca do Acre": {
                "site": "https://bocadoacre.am.gov.br/",
                "transparencia": "https://transparenciamunicipalaam.org.br/p/bocadoacre",
                "endereco": "Praça Cel. Joseh Machado, 147 - Platô do Piquiá, Boca do Acre - AM",
                "cep": "69850-000",
                "coordenadas": {
                    "latitude": -8.7523,
                    "longitude": -67.3976
                }
            },
            "Prefeitura de Careiro": {
                "site": "https://careiro.am.gov.br/",
                "transparencia": "https://www.careiro.am.gov.br/portal-transparencia/",
                "endereco": "Avenida Mário Guedes, 999 - Centro, Careiro - AM",
                "cep": "69250-000",
                "coordenadas": {
                    "latitude": -3.7661,
                    "longitude": -60.3603
                }
            },
            "Prefeitura de Iranduba": {
                "site": "https://www.iranduba.am.gov.br/",
                "transparencia": "https://transparencia.betha.cloud/#/yVVW6OAco0wQSzK_WdkkFg==",
                "endereco": "Avenida Amazonas, 23 - Centro, Iranduba - AM",
                "cep": "69400-000",
                "coordenadas": {
                    "latitude": -3.2829,
                    "longitude": -60.1873
                }
            },
            "Prefeitura de Rio Preto da Eva": {
                "site": "https://riopretodaeva.am.gov.br/",
                "transparencia": "https://riopretodaeva.am.gov.br/portal-da-transparencia/",
                "endereco": "Rua Gov. Pimenta Bueno, 23 - Centro, Rio Preto da Eva - AM",
                "cep": "69117-000",
                "coordenadas": {
                    "latitude": -2.6994,
                    "longitude": -59.7001
                }
            },
            "Prefeitura de Autazes": {
                "site": "https://autazes.am.gov.br/",
                "transparencia": "https://www.perseusdata2.com/pmautazes/",
                "endereco": "Rua Júlio de Sant'Anna, 1 - Centro, Autazes - AM",
                "cep": "69240-000",
                "coordenadas": {
                    "latitude": -3.5794,
                    "longitude": -59.1317
                }
            },
            "Prefeitura de Barcelos": {
                "site": "https://barcelos.am.gov.br/",
                "transparencia": "https://transparenciamunicipalaam.org.br/p/barcelos",
                "endereco": "Avenida Ajuricaba, 453 - Centro, Barcelos - AM",
                "cep": "69700-000",
                "coordenadas": {
                    "latitude": -0.9751,
                    "longitude": -62.9250
                }
            },
            "Prefeitura de Fonte Boa": {
                "site": "https://fonteboa.am.gov.br/",
                "transparencia": "https://transparenciamunicipalaam.org.br/p/fonte-boa",
                "endereco": "Rua Sete de Setembro, 2 - Centro, Fonte Boa - AM",
                "cep": "69670-000",
                "coordenadas": {
                    "latitude": -2.5143,
                    "longitude": -66.0921
                }
            },
            "Prefeitura de Guajará": {
                "site": "https://guajara.am.gov.br/",
                "transparencia": "https://guajara.am.gov.br/portal-transparencia/",
                "endereco": "Rua 27 de Dezembro, s/n - Centro, Guajará - AM",
                "cep": "69865-000",
                "coordenadas": {
                    "latitude": -7.5028,
                    "longitude": -72.5901
                }
            },
            "Prefeitura de Boa Vista do Ramos": {
                "site": "https://boavistadoramos.am.gov.br/",
                "transparencia": "https://boavistadoramos.am.gov.br/transparencia/",
                "endereco": "Avenida Castelo Branco, 305 - Centro, Boa Vista do Ramos - AM",
                "cep": "69195-000",
                "coordenadas": {
                    "latitude": -2.9739,
                    "longitude": -57.5745
                }
            }
        },
        "Poder Legislativo": {
            "Câmara Municipal de Manaus": {
                "site": "https://www.cmm.am.gov.br/",
                "transparencia": "https://www.cmm.am.gov.br/transparencia/",
                "endereco": "Rua Padre Agostinho Caballero Martin, 850 - Santo Antônio, Manaus - AM",
                "cep": "69029-120",
                "coordenadas": {
                    "latitude": -3.1252,
                    "longitude": -60.0384
                }
            },
            "Câmara Municipal de Itacoatiara": {
                "site": "https://cmitacoatiara.am.gov.br/",
                "transparencia": "https://cmitacoatiara.am.gov.br/transparencia/",
                "endereco": "Rua Acácio Leite, 1339 - Centro, Itacoatiara - AM",
                "cep": "69100-000",
                "coordenadas": {
                    "latitude": -3.1402,
                    "longitude": -58.4419
                }
            },
            "Câmara Municipal de Parintins": {
                "site": "https://cmparintins.am.gov.br/",
                "transparencia": "https://cmparintins.am.gov.br/transparencia/",
                "endereco": "Avenida Nações Unidas, 2122 - Centro, Parintins - AM",
                "cep": "69151-160",
                "coordenadas": {
                    "latitude": -2.6321,
                    "longitude": -56.7380
                }
            },
            "Câmara Municipal de Caapiranga": {
                "site": "https://cmcaapiranga.am.gov.br/",
                "transparencia": "https://cmcaapiranga.am.gov.br/transparencia/",
                "endereco": "Rua Getúlio Vargas, 14 - Centro, Caapiranga - AM",
                "cep": "69410-000",
                "coordenadas": {
                    "latitude": -3.3276,
                    "longitude": -61.2096
                }
            },
            "Câmara Municipal de Careiro da Várzea": {
                "site": "https://cmcareirodavarzea.am.gov.br/",
                "transparencia": "https://cmcareirodavarzea.am.gov.br/transparencia/",
                "endereco": "Rua Zacarias Ribeiro, s/n - Centro, Careiro da Várzea - AM",
                "cep": "69255-000",
                "coordenadas": {
                    "latitude": -3.2045,
                    "longitude": -59.8277
                }
            },
            "Câmara Municipal de Codajás": {
                "site": "https://cmcodajas.am.gov.br/",
                "transparencia": "https://cmcodajas.am.gov.br/transparencia/",
                "endereco": "Rua 15 de Novembro, 255 - Centro, Codajás - AM",
                "cep": "69450-000",
                "coordenadas": {
                    "latitude": -3.8368,
                    "longitude": -62.0577
                }
            },
            "Câmara Municipal de Envira": {
                "site": "https://cmenvira.am.gov.br/",
                "transparencia": "https://cmenvira.am.gov.br/transparencia/",
                "endereco": "Rua D, s/n - Centro, Envira - AM",
                "cep": "69880-000",
                "coordenadas": {
                    "latitude": -7.3005,
                    "longitude": -70.2173
                }
            },
            "Câmara Municipal de Ipixuna": {
                "site": "https://cmipixuna.am.gov.br/",
                "transparencia": "https://cmipixuna.am.gov.br/transparencia/",
                "endereco": "Rua Castelo Branco, 17 - Centro, Ipixuna - AM",
                "cep": "69890-000",
                "coordenadas": {
                    "latitude": -7.0494,
                    "longitude": -71.6963
                }
            },
            "Câmara Municipal de Itapiranga": {
                "site": "https://cmitapiranga.am.gov.br/",
                "transparencia": "https://cmitapiranga.am.gov.br/transparencia/",
                "endereco": "Avenida 24 de Agosto, 100 - Centro, Itapiranga - AM",
                "cep": "69120-000",
                "coordenadas": {
                    "latitude": -2.7485,
                    "longitude": -58.0227
                }
            },
            "Câmara Municipal de Itamarati": {
                "site": "https://cmitamarati.am.gov.br/",
                "transparencia": "https://cmitamarati.am.gov.br/transparencia/",
                "endereco": "Rua Vinte e Um de Junho, s/n - Centro, Itamarati - AM",
                "cep": "69530-000",
                "coordenadas": {
                    "latitude": -6.4258,
                    "longitude": -68.2325
                }
            },
            "Câmara Municipal de Japurá": {
                "site": "https://cmjapura.am.gov.br/",
                "transparencia": "https://cmjapura.am.gov.br/transparencia/",
                "endereco": "Rua Duque de Caxias, s/n - Centro, Japurá - AM",
                "cep": "69495-000",
                "coordenadas": {
                    "latitude": -1.8261,
                    "longitude": -66.5991
                }
            },
            "Câmara Municipal de Juruá": {
                "site": "https://cmjurua.am.gov.br/",
                "transparencia": "https://cmjurua.am.gov.br/transparencia/",
                "endereco": "Rua Álvaro Maia, s/n - Centro, Juruá - AM",
                "cep": "69520-000",
                "coordenadas": {
                    "latitude": -3.4906,
                    "longitude": -66.0717
                }
            },
            "Câmara Municipal de Nhamundá": {
                "site": "https://cmnhamunda.am.gov.br/",
                "transparencia": "https://cmnhamunda.am.gov.br/transparencia/",
                "endereco": "Rua Furtado, s/n - Centro, Nhamundá - AM",
                "cep": "69140-000",
                "coordenadas": {
                    "latitude": -2.1866,
                    "longitude": -56.7147
                }
            },
            "Câmara Municipal de Santa Isabel do Rio Negro": {
                "site": "https://cmsantaisabeldorionegro.am.gov.br/",
                "transparencia": "https://cmsantaisabeldorionegro.am.gov.br/transparencia/",
                "endereco": "Rua João Walter, s/n - Centro, Santa Isabel do Rio Negro - AM",
                "cep": "69740-000",
                "coordenadas": {
                    "latitude": -0.4139,
                    "longitude": -65.0191
                }
            },
            "Câmara Municipal de São Paulo de Olivença": {
                "site": "https://cmsaopaulodeolivenca.am.gov.br/",
                "transparencia": "https://cmsaopaulodeolivenca.am.gov.br/transparencia/",
                "endereco": "Avenida Constantino Nery, 1 - Centro, São Paulo de Olivença - AM",
                "cep": "69600-000",
                "coordenadas": {
                    "latitude": -3.3781,
                    "longitude": -68.8725
                }
            },
            "Câmara Municipal de Silves": {
                "site": "https://cmsilves.am.gov.br/",
                "transparencia": "https://cmsilves.am.gov.br/transparencia/",
                "endereco": "Rua Getúlio Vargas, 67 - Centro, Silves - AM",
                "cep": "69110-000",
                "coordenadas": {
                    "latitude": -2.8398,
                    "longitude": -58.2093
                }
            },
            "Câmara Municipal de Tapauá": {
                "site": "https://cmtapaua.am.gov.br/",
                "transparencia": "https://cmtapaua.am.gov.br/transparencia/",
                "endereco": "Rua Presidente Vargas, s/n - Centro, Tapauá - AM",
                "cep": "69470-000",
                "coordenadas": {
                    "latitude": -5.6323,
                    "longitude": -63.1809
                }
            },
            "Câmara Municipal de Tonantins": {
                "site": "https://cmtonantins.am.gov.br/",
                "transparencia": "https://cmtonantins.am.gov.br/transparencia/",
                "endereco": "Rua Sete de Setembro, s/n - Centro, Tonantins - AM",
                "cep": "69685-000",
                "coordenadas": {
                    "latitude": -2.8732,
                    "longitude": -67.8018
                }
            },
            "Câmara Municipal de Uarini": {
                "site": "https://cmuarini.am.gov.br/",
                "transparencia": "https://cmuarini.am.gov.br/transparencia/",
                "endereco": "Rua Getúlio Vargas, s/n - Centro, Uarini - AM",
                "cep": "69480-000",
                "coordenadas": {
                    "latitude": -2.9906,
                    "longitude": -65.1092
                }
            },
            "Câmara Municipal de Urucurituba": {
                "site": "https://cmurucurituba.am.gov.br/",
                "transparencia": "https://cmurucurituba.am.gov.br/transparencia/",
                "endereco": "Rua José de Anchieta, s/n - Centro, Urucurituba - AM",
                "cep": "69130-000",
                "coordenadas": {
                    "latitude": -3.1166,
                    "longitude": -58.1565
                }
            }
        }
    }
}


# Coordenadas de Manaus (capital) para cálculo de distâncias
COORDENADAS_MANAUS = {
    "latitude": -3.1190,
    "longitude": -60.0217
}

# Funções auxiliares atualizadas
def calcular_distancia_coordenadas(coord1, coord2):
    """
    Calcula a distância entre duas coordenadas (em km)
    Args:
        coord1 (dict): {'latitude': float, 'longitude': float}
        coord2 (dict): {'latitude': float, 'longitude': float}
    Returns:
        float: Distância em quilômetros
    """
    from math import radians, cos, sin, asin, sqrt
    
    lat1, lon1 = radians(coord1['latitude']), radians(coord1['longitude'])
    lat2, lon2 = radians(coord2['latitude']), radians(coord2['longitude'])
    
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a))
    r = 6371  # Raio da Terra em km
    return c * r

def obter_distancia_de_manaus(municipio_coordenadas):
    """
    Calcula a distância de um município até Manaus
    Args:
        municipio_coordenadas (dict): Coordenadas do município
    Returns:
        float: Distância em km de Manaus
    """
    return calcular_distancia_coordenadas(COORDENADAS_MANAUS, municipio_coordenadas)

def obter_dados_completos_orgao_com_distancia(esfera, poder, orgao):
    """
    Obtém todos os dados de um órgão específico incluindo distância de Manaus
    Args:
        esfera (str): "Estadual" ou "Municipal"
        poder (str): Nome do poder
        orgao (str): Nome do órgão
    Returns:
        dict: Dicionário completo com todos os dados do órgão incluindo distância
    """
    dados = ORGAOS_DATA.get(esfera, {}).get(poder, {}).get(orgao, {})
    if dados and dados.get('coordenadas'):
        endereco = dados.get('endereco', '')
        if 'Manaus' not in endereco and esfera == 'Municipal':
            distancia = obter_distancia_de_manaus(dados['coordenadas'])
            dados['distancia_manaus_km'] = round(distancia, 1)
            dados['descricao_localizacao'] = f"Município a {round(distancia, 1)} km da capital Manaus"
        elif 'Manaus' in endereco:
            dados['descricao_localizacao'] = "Capital do Estado do Amazonas"
        else:
            dados['descricao_localizacao'] = "Órgão Estadual localizado em Manaus"
    return dados

def obter_resumo_camaras_municipais():
    """
    Obtém resumo de todas as câmaras municipais com distâncias
    Returns:
        dict: Resumo das câmaras municipais
    """
    camaras = []
    total_camaras = 0
    poder_legislativo = ORGAOS_DATA.get('Municipal', {}).get('Poder Legislativo', {})
    
    for nome_camara, dados in poder_legislativo.items():
        total_camaras += 1
        endereco = dados.get('endereco', '')
        if dados.get('coordenadas') and 'Manaus' not in endereco:
            distancia = obter_distancia_de_manaus(dados['coordenadas'])
            camaras.append({
                'nome': nome_camara,
                'endereco': endereco,
                'site': dados.get('site', ''),
                'transparencia': dados.get('transparencia', ''),
                'distancia_km': round(distancia, 1),
                'descricao': f"Município a {round(distancia, 1)} km da capital Manaus"
            })
        elif 'Manaus' in endereco:
            camaras.append({
                'nome': nome_camara,
                'endereco': endereco,
                'site': dados.get('site', ''),
                'transparencia': dados.get('transparencia', ''),
                'distancia_km': 0,
                'descricao': "Capital do Estado do Amazonas"
            })
    
    # Ordenar por distância
    camaras_ordenadas = sorted(camaras, key=lambda x: x['distancia_km'])
    
    return {
        'total_camaras': total_camaras,
        'camaras_ordenadas_por_distancia': camaras_ordenadas,
        'camara_mais_proxima': camaras_ordenadas[1] if len(camaras_ordenadas) > 1 else None,  # Exclui Manaus
        'camara_mais_distante': camaras_ordenadas[-1] if camaras_ordenadas else None
    }

def listar_todos_municipios_completo():
    """
    Lista todos os municípios com prefeituras e câmaras
    Returns:
        dict: Dicionário completo com todos os municípios
    """
    municipios_completo = {}
    
    # Obter prefeituras
    prefeituras = ORGAOS_DATA.get('Municipal', {}).get('Poder Executivo', {})
    camaras = ORGAOS_DATA.get('Municipal', {}).get('Poder Legislativo', {})
    
    for nome_prefeitura, dados_prefeitura in prefeituras.items():
        # Extrair nome do município
        municipio = nome_prefeitura.replace('Prefeitura de ', '')
        endereco_prefeitura = dados_prefeitura.get('endereco', '')
        distancia = 0
        descricao = "Capital do Estado do Amazonas"
        
        if dados_prefeitura.get('coordenadas') and 'Manaus' not in endereco_prefeitura:
            distancia = obter_distancia_de_manaus(dados_prefeitura['coordenadas'])
            descricao = f"Município a {round(distancia, 1)} km da capital Manaus"
        
        # Buscar câmara correspondente
        nome_camara = f"Câmara Municipal de {municipio}"
        dados_camara = camaras.get(nome_camara, {})
        
        municipios_completo[municipio] = {
            'distancia_manaus_km': round(distancia, 1),
            'descricao_localizacao': descricao,
            'prefeitura': {
                'nome': nome_prefeitura,
                'site': dados_prefeitura.get('site', ''),
                'transparencia': dados_prefeitura.get('transparencia', ''),
                'endereco': endereco_prefeitura,
                'cep': dados_prefeitura.get('cep', ''),
                'coordenadas': dados_prefeitura.get('coordenadas', {})
            },
            'camara': {
                'nome': nome_camara,
                'site': dados_camara.get('site', ''),
                'transparencia': dados_camara.get('transparencia', ''),
                'endereco': dados_camara.get('endereco', ''),
                'cep': dados_camara.get('cep', ''),
                'coordenadas': dados_camara.get('coordenadas', {})
            }
        }
    
    return municipios_completo

# Exemplo de uso
if __name__ == "__main__":
    # Exemplo 1: Resumo das câmaras municipais
    resumo_camaras = obter_resumo_camaras_municipais()
    print("=== Resumo das Câmaras Municipais ===")
    print(f"Total de câmaras: {resumo_camaras['total_camaras']}")
    if resumo_camaras['camara_mais_proxima']:
        print(f"Câmara mais próxima de Manaus: {resumo_camaras['camara_mais_proxima']['nome']} ({resumo_camaras['camara_mais_proxima']['distancia_km']} km)")
    if resumo_camaras['camara_mais_distante']:
        print(f"Câmara mais distante de Manaus: {resumo_camaras['camara_mais_distante']['nome']} ({resumo_camaras['camara_mais_distante']['distancia_km']} km)")
    
    # Exemplo 2: Dados completos de um município
    municipios_completo = listar_todos_municipios_completo()
    print("\n=== Dados Completos do Município de Itacoatiara ===")
    print(municipios_completo.get('Itacoatiara'))