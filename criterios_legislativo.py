# criterios_legislativo.py
# Critérios específicos do Poder Legislativo

CRITERIOS_LEGISLATIVO = {
    # ATIVIDADES FINALÍSTICAS - PL
    "20.1": {
        "dimensao": "Atividades Finalísticas - PL",
        "id": "20.1",
        "criterio": "Divulga a composição da Casa, com a biografia dos parlamentares?",
        "classificacao": "Obrigatória",
        "fundamentacao": "Art. 37, 'caput' da CF e Art. 8º, § 1º, I, da Lei nº 12.527/2011 – LAI.",
        "palavras_chave": [
            "composição casa", "parlamentares", "vereadores", "deputados",
            "biografia parlamentares", "mesa diretora", "legisladores"
        ],
        "sinonimos": [
            "membros casa", "representantes", "edis", "mandatários",
            "eleitos", "mandato", "cadeiras", "bancadas"
        ]
    },
    
    "20.2": {
        "dimensao": "Atividades Finalísticas - PL",
        "id": "20.2",
        "criterio": "Divulga as leis e atos infralegais (resoluções, decretos, etc.) produzidos?",
        "classificacao": "Obrigatória",
        "fundamentacao": "Art. 37, da CF (princípio da publicidade) e arts. 6, inciso I, e 8º da Lei nº 12.527/2011 – LAI.",
        "palavras_chave": [
            "leis", "atos infralegais", "resoluções", "decretos legislativos",
            "normas", "legislação", "produção normativa"
        ],
        "sinonimos": [
            "normativos", "dispositivos legais", "instrumentos normativos",
            "regulamentações", "ordenamentos", "disposições", "regras"
        ]
    },
    
    "20.3": {
        "dimensao": "Atividades Finalísticas - PL",
        "id": "20.3",
        "criterio": "Divulga projetos de leis e de atos infralegais, bem como as respectivas tramitações (contemplando ementa, documentos anexos, situação atual, autor, relator)?",
        "classificacao": "Obrigatória",
        "fundamentacao": "Art. 37, da CF (princípio da publicidade) e arts. 6, inciso I, e 8º da Lei nº 12.527/2011 – LAI.",
        "palavras_chave": [
            "projetos lei", "tramitação", "ementa", "autor projeto",
            "relator", "situação projeto", "andamento", "processo legislativo"
        ],
        "sinonimos": [
            "proposições", "proposituras", "iniciativas", "matérias",
            "andamento legislativo", "fluxo legislativo", "curso legislativo"
        ]
    },
    
    "20.4": {
        "dimensao": "Atividades Finalísticas - PL",
        "id": "20.4",
        "criterio": "Divulga a pauta das sessões do Plenário?",
        "classificacao": "Obrigatória",
        "fundamentacao": "arts. 7º, incisos IV, V e VI, e 8º 'caput' da Lei nº 12.527/2011 – LAI.",
        "palavras_chave": [
            "pauta sessões", "ordem dia", "plenário", "sessões ordinárias",
            "sessões extraordinárias", "agenda plenário", "cronograma sessões"
        ],
        "sinonimos": [
            "programação sessões", "calendário sessões", "agenda legislativa",
            "roteiro sessões", "sequência votações", "itens pauta"
        ]
    },
    
    "20.5": {
        "dimensao": "Atividades Finalísticas - PL",
        "id": "20.5",
        "criterio": "Divulga a pauta das Comissões?",
        "classificacao": "Obrigatória",
        "fundamentacao": "Art. 37, caput, da CF e Art. 3, II, da Lei nº 12.527/2011 – LAI.",
        "palavras_chave": [
            "pauta comissões", "comissões permanentes", "comissões temporárias",
            "reuniões comissões", "agenda comissões", "trabalhos comissões"
        ],
        "sinonimos": [
            "programação comissões", "cronograma comissões", "atividades comissões",
            "calendário comissões", "ordem trabalhos", "sequência trabalhos"
        ]
    },
    
    "20.6": {
        "dimensao": "Atividades Finalísticas - PL",
        "id": "20.6",
        "criterio": "Divulga as atas das sessões, incluindo a lista de presença dos parlamentares em cada sessão?",
        "classificacao": "Obrigatória",
        "fundamentacao": "Art. 37, caput, da CF e Art. 3, II, da Lei nº 12.527/2011 – LAI.",
        "palavras_chave": [
            "atas sessões", "lista presença", "frequência parlamentares",
            "assiduidade", "comparecimento", "registro presença"
        ],
        "sinonimos": [
            "relatório sessões", "registro sessões", "memória sessões",
            "documentação sessões", "controle presença", "chamada nominal"
        ]
    },
    
    "20.7": {
        "dimensao": "Atividades Finalísticas - PL",
        "id": "20.7",
        "criterio": "Divulga lista sobre as votações nominais?",
        "classificacao": "Recomendada",
        "fundamentacao": "Art. 37, caput, da CF e Art. 3, II, da Lei nº 12.527/2011 – LAI.",
        "palavras_chave": [
            "votações nominais", "votações", "resultado votações",
            "posicionamento parlamentares", "voto parlamentares", "escrutínio"
        ],
        "sinonimos": [
            "sufrágio", "deliberações", "decisões", "manifestações voto",
            "posições votação", "registro votos", "apuração votos"
        ]
    },
    
    "20.8": {
        "dimensao": "Atividades Finalísticas - PL",
        "id": "20.8",
        "criterio": "Divulga o ato que aprecia as Contas do Chefe do Poder Executivo (Decreto) e o teor do julgamento (Ata ou Resumo da Sessão que aprovou ou rejeitou as contas)?",
        "classificacao": "Obrigatória",
        "fundamentacao": "Art. 7º, inciso VII, alínea 'b', da Lei nº 12.527/2011 - LAI e art. 56, §3º, da LRF.",
        "palavras_chave": [
            "apreciação contas", "contas chefe executivo", "julgamento contas",
            "decreto legislativo", "aprovação contas", "rejeição contas"
        ],
        "sinonimos": [
            "análise contas", "exame contas", "avaliação contas",
            "parecer contas", "decisão contas", "veredicto contas"
        ]
    },
    
    "20.9": {
        "dimensao": "Atividades Finalísticas - PL",
        "id": "20.9",
        "criterio": "Há transmissão de sessões, audiências públicas, consultas públicas ou outras formas de participação popular via meios de comunicação como rádio, TV, internet, entre outros?",
        "classificacao": "Recomendada",
        "fundamentacao": "Arts. 7, 13 e ss. da Lei 13.460/17, c/c art. 9º, inciso II, da Lei nº 12.527/2011 - LAI e art. 37, 'caput', da CF (princípio da publicidade).",
        "palavras_chave": [
            "transmissão sessões", "audiências públicas", "consultas públicas",
            "participação popular", "rádio", "TV", "internet", "streaming"
        ],
        "sinonimos": [
            "difusão sessões", "broadcast", "webcast", "ao vivo",
            "tempo real", "divulgação sessões", "cobertura sessões"
        ]
    },
    
    "20.10": {
        "dimensao": "Atividades Finalísticas - PL",
        "id": "20.10",
        "criterio": "Divulga a regulamentação e os valores relativos às cotas para exercício da atividade parlamentar/verba indenizatória?",
        "classificacao": "Recomendada",
        "fundamentacao": "Arts. 7º, incisos IV e V, e 8º 'caput' da Lei nº 12.527/2011 – LAI.",
        "palavras_chave": [
            "cotas parlamentares", "verba indenizatória", "auxílio parlamentar",
            "gastos parlamentares", "despesas parlamentares", "ressarcimento"
        ],
        "sinonimos": [
            "ajuda custo", "subsídio", "indenização", "reembolso",
            "compensação", "custeio atividade", "apoio parlamentar"
        ]
    },

    "20.11": {
        "dimensao": "Atividades Finalísticas - PL",
        "id": "20.11",
        "criterio": "Divulga dados sobre as atividades legislativas dos parlamentares?",
        "classificacao": "Recomendada",
        "fundamentacao": "Art. 37, 'caput' da CF e Art. 8º, § 1º, V, da Lei nº 12.527/2011 – LAI.",
        "palavras_chave": [
            "atividades legislativas", "produção legislativa", "atuação parlamentares",
            "projetos apresentados", "participação comissões", "desempenho parlamentar"
        ],
        "sinonimos": [
            "trabalho legislativo", "função legislativa", "exercício mandato",
            "performance parlamentar", "contribuição legislativa", "efetividade parlamentar"
        ]
    }
}