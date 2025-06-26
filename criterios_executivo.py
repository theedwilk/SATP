# criterios_executivo.py
# Critérios específicos do Poder Executivo

CRITERIOS_EXECUTIVO = {
    # RECEITA
    "3.2": {
        "dimensao": "Receita",
        "id": "3.2",
        "criterio": "Divulga a classificação orçamentária por natureza da receita (categoria econômica, origem, espécie)?",
        "classificacao": "Essencial",
        "fundamentacao": "Art. 8º, II, 'e', do Decreto nº 10.540/2020.",
        "palavras_chave": [
            "classificação receita", "natureza receita", "categoria econômica receita",
            "origem receita", "espécie receita", "tipologia receita"
        ],
        "sinonimos": [
            "categorização receita", "tipificação receita", "estrutura receita",
            "organização receita", "divisão receita", "agrupamento receita"
        ]
    },
    
    "3.3": {
        "dimensao": "Receita",
        "id": "3.3",
        "criterio": "Divulga a lista dos inscritos em dívida ativa, contendo, no mínimo, dados referentes ao nome do inscrito e o valor total da dívida?",
        "classificacao": "Obrigatória",
        "fundamentacao": "Art. 198, § 3º, II da Lei 5.172/1966.",
        "palavras_chave": [
            "dívida ativa", "inscritos dívida", "devedores", "inadimplentes",
            "débitos tributários", "cobrança administrativa", "créditos tributários"
        ],
        "sinonimos": [
            "pendências tributárias", "débitos pendentes", "valores devidos",
            "obrigações tributárias", "passivos tributários", "créditos vencidos"
        ]
    },

    # PLANEJAMENTO E PRESTAÇÃO DE CONTAS
    "11.4": {
        "dimensao": "Planejamento e Prestação de contas",
        "id": "11.4",
        "criterio": "Divulga o resultado do julgamento das Contas do Chefe do Poder Executivo pelo Poder Legislativo?",
        "classificacao": "Obrigatória",
        "fundamentacao": "Art. 56, §3º, da LC nº 101/00.",
        "palavras_chave": [
            "julgamento contas", "contas chefe executivo", "poder legislativo",
            "aprovação contas", "rejeição contas", "parecer contas"
        ],
        "sinonimos": [
            "apreciação contas", "análise contas", "decisão contas",
            "veredicto contas", "resultado julgamento", "conclusão análise"
        ]
    },
    
    "11.8": {
        "dimensao": "Planejamento e Prestação de contas",
        "id": "11.8",
        "criterio": "Divulga a Lei do Plano Plurianual (PPA) e seus anexos?",
        "classificacao": "Essencial",
        "fundamentacao": "Art. 48, 'caput', da LC nº 101/00.",
        "palavras_chave": [
            "PPA", "plano plurianual", "planejamento plurianual",
            "programas governo", "objetivos estratégicos", "metas plurianuais"
        ],
        "sinonimos": [
            "plano quadrienal", "planejamento estratégico", "diretrizes governo",
            "programação plurianual", "plano médio prazo", "estratégia governamental"
        ]
    },
    
    "11.9": {
        "dimensao": "Planejamento e Prestação de contas",
        "id": "11.9",
        "criterio": "Divulga a Lei de Diretrizes Orçamentárias (LDO) e seus anexos?",
        "classificacao": "Essencial",
        "fundamentacao": "Art. 48, 'caput', da LC nº 101/00.",
        "palavras_chave": [
            "LDO", "diretrizes orçamentárias", "orientações orçamentárias",
            "metas fiscais", "prioridades orçamentárias", "política fiscal"
        ],
        "sinonimos": [
            "direcionamento orçamentário", "norteamento orçamentário", "guia orçamentário",
            "orientação fiscal", "parâmetros orçamentários", "balizamento orçamentário"
        ]
    },
    
    "11.10": {
        "dimensao": "Planejamento e Prestação de contas",
        "id": "11.10",
        "criterio": "Divulga a Lei Orçamentária (LOA) e seus anexos?",
        "classificacao": "Essencial",
        "fundamentacao": "Art. 48, 'caput', da LC nº 101/00.",
        "palavras_chave": [
            "LOA", "lei orçamentária", "orçamento anual",
            "peça orçamentária", "proposta orçamentária", "dotações orçamentárias"
        ],
        "sinonimos": [
            "orçamento público", "lei orçamento", "previsão orçamentária",
            "programação orçamentária", "alocação recursos", "distribuição recursos"
        ]
    },

    # RENÚNCIAS DE RECEITAS
    "16.1": {
        "dimensao": "Renúncias de Receitas",
        "id": "16.1",
        "criterio": "Divulga as desonerações tributárias concedidas e a fundamentação legal individualizada?",
        "classificacao": "Recomendada",
        "fundamentacao": "Art. 7º, inciso VI, da Lei nº 12.527/2011 - LAI e art. 198, §3º, III, do Código Tributário Nacional.",
        "palavras_chave": [
            "desonerações tributárias", "renúncia fiscal", "benefícios fiscais",
            "incentivos fiscais", "isenções", "fundamentação legal"
        ],
        "sinonimos": [
            "descontos tributários", "reduções tributárias", "abatimentos fiscais",
            "vantagens fiscais", "privilégios fiscais", "favores fiscais"
        ]
    },
    
    "16.2": {
        "dimensao": "Renúncias de Receitas",
        "id": "16.2",
        "criterio": "Divulga os valores da renúncia fiscal prevista e realizada, por tipo ou espécie de benefício ou incentivo fiscal?",
        "classificacao": "Recomendada",
        "fundamentacao": "Art. 37, caput, da CF, Arts. 14, 48, §1º, II e 48-A, inciso II, da LC nº 101/00 e art. 8º, II, do Decreto nº 10.540/20.",
        "palavras_chave": [
            "valores renúncia", "renúncia prevista", "renúncia realizada",
            "tipos benefícios", "espécies incentivos", "quantificação renúncia"
        ],
        "sinonimos": [
            "montantes renúncia", "valores benefícios", "quantias incentivos",
            "estimativas renúncia", "realização renúncia", "efetivação benefícios"
        ]
    },
    
    "16.3": {
        "dimensao": "Renúncias de Receitas",
        "id": "16.3",
        "criterio": "Identifica os beneficiários das desonerações tributárias (benefícios ou incentivos fiscais)?",
        "classificacao": "Recomendada",
        "fundamentacao": "Art. 37, caput, da CF, Arts. 14, 48, §1º, II e 48-A, inciso II, da LC nº 101/00 e art. 8º, II, do Decreto nº 10.540/20.",
        "palavras_chave": [
            "beneficiários", "contemplados", "favorecidos", "agraciados",
            "empresas beneficiadas", "pessoas beneficiadas", "entidades beneficiadas"
        ],
        "sinonimos": [
            "destinatários", "receptores", "usufrutuários", "aproveitadores",
            "gozadores benefícios", "detentores vantagens", "portadores incentivos"
        ]
    },
    
    "16.4": {
        "dimensao": "Renúncias de Receitas",
        "id": "16.4",
        "criterio": "Divulga informações sobre projetos de incentivo à cultura (incluindo esportivos), identificando os projetos aprovados, o respectivo beneficiário e o valor aprovado?",
        "classificacao": "Recomendada",
        "fundamentacao": "Art. 37, caput, da CF, Arts. 14, 48, §1º, II e 48-A, inciso II, da LC nº 101/00 e art. 8º, II, do Decreto nº 10.540/20.",
        "palavras_chave": [
            "incentivo cultura", "projetos culturais", "projetos esportivos",
            "lei rouanet", "lei incentivo", "patrocínio cultural"
        ],
        "sinonimos": [
            "fomento cultural", "apoio cultura", "estímulo cultura",
            "promoção cultural", "desenvolvimento cultural", "mecenato"
        ]
    },

    # EMENDAS PARLAMENTARES
    "17.1": {
        "dimensao": "Emendas Parlamentares",
        "id": "17.1",
        "criterio": "Identifica as emendas parlamentares recebidas, contendo informações sobre a origem, a forma de repasse, o tipo de emenda, o número da emenda, a autoria, o valor previsto e realizado, o objeto e função de governo?",
        "classificacao": "Recomendada",
        "fundamentacao": "Emenda à Constituição nº 105/2019, Portaria Interministerial ME/SEGOV nº 6.411/2021, art. 19; Nota Recomendatória Atricon nº 01/2022; Acórdão nº 518/2023 - TCU-Plenário.",
        "palavras_chave": [
            "emendas parlamentares", "emendas individuais", "emendas bancada",
            "emendas comissão", "recursos parlamentares", "indicações parlamentares"
        ],
        "sinonimos": [
            "destinações parlamentares", "alocações parlamentares", "direcionamentos parlamentares",
            "indicações deputados", "indicações senadores", "recursos destinados"
        ]
    },
    
    "17.2": {
        "dimensao": "Emendas Parlamentares",
        "id": "17.2",
        "criterio": "Demonstra a execução orçamentária e financeira oriunda das 'emendas pix'?",
        "classificacao": "Recomendada",
        "fundamentacao": "Art. 166-A, I (Emenda à Constituição nº 105/2019), Portaria Interministerial ME/SEGOV nº 6.411/2021, art. 19; Nota Recomendatória Atricon nº 01/2022; Acórdão nº 518/2023 - TCU-Plenário, Portaria Conjunta MF/MPO/MGI/SRI-PR nº 1, de 1º de abril de 2024",
        "palavras_chave": [
            "emendas pix", "transferências especiais", "repasses diretos",
            "execução emendas", "transferências automáticas", "recursos diretos"
        ],
        "sinonimos": [
            "transferências imediatas", "repasses automáticos", "envios diretos",
            "remessas especiais", "destinações diretas", "alocações automáticas"
        ]
    },

    # SAÚDE
    "18.1": {
        "dimensao": "Saúde",
        "id": "18.1",
        "criterio": "Divulga o plano de saúde, a programação anual e o relatório de gestão?",
        "classificacao": "Obrigatória",
        "fundamentacao": "Art. 8º, § 1º, V e art. 9º, II, da Lei nº 12.527/2011 - LAI e art. 37, 'caput', da CF (princípio da publicidade).",
        "palavras_chave": [
            "plano saúde", "programação saúde", "relatório gestão saúde",
            "SUS", "sistema saúde", "política saúde"
        ],
        "sinonimos": [
            "planejamento saúde", "programa saúde", "estratégia saúde",
            "diretrizes saúde", "ações saúde", "serviços saúde"
        ]
    },
    
    "18.2": {
        "dimensao": "Saúde",
        "id": "18.2",
        "criterio": "Divulga informações relacionadas aos serviços de saúde, indicando os horários, os profissionais prestadores de serviços, as especialidades e local?",
        "classificacao": "Obrigatória",
        "fundamentacao": "Art. 7º, VI, da Lei nº 8.080/1990.",
        "palavras_chave": [
            "serviços saúde", "horários atendimento", "profissionais saúde",
            "especialidades médicas", "unidades saúde", "postos saúde"
        ],
        "sinonimos": [
            "atendimento médico", "assistência saúde", "cuidados saúde",
            "prestação serviços", "oferta saúde", "disponibilidade serviços"
        ]
    },
    
    "18.3": {
        "dimensao": "Saúde",
        "id": "18.3",
        "criterio": "Divulga a lista de espera de regulação para acesso às consultas, exames e serviços médicos?",
        "classificacao": "Recomendada",
        "fundamentacao": "Portaria nº 1.559, de 1º de agosto de 2008.",
        "palavras_chave": [
            "lista espera", "fila espera", "regulação", "agendamento",
            "consultas médicas", "exames médicos", "serviços médicos"
        ],
        "sinonimos": [
            "aguardo atendimento", "ordem atendimento", "sequência atendimento",
            "prioridade atendimento", "cronologia atendimento", "marcação consultas"
        ]
    },
    
    "18.4": {
        "dimensao": "Saúde",
        "id": "18.4",
        "criterio": "Divulga lista dos medicamentos a serem fornecidos pelo SUS e informações de como obter medicamentos, incluindo os de alto custo?",
        "classificacao": "Recomendada",
        "fundamentacao": "Art. 26, parágrafo único, inciso I, do Decreto n. 7.508, de 28 de junho de 2011 (redação dada pelo Decreto n. 11.161, de 2022).",
        "palavras_chave": [
            "medicamentos SUS", "lista medicamentos", "farmácia básica",
            "medicamentos alto custo", "assistência farmacêutica", "RENAME"
        ],
        "sinonimos": [
            "remédios SUS", "fármacos", "drogas", "produtos farmacêuticos",
            "medicação", "terapêutica medicamentosa", "arsenal terapêutico"
        ]
    },
    
    "18.5": {
        "dimensao": "Saúde",
        "id": "18.5",
        "criterio": "Divulga os estoques de medicamentos das farmácias públicas?",
        "classificacao": "Obrigatória",
        "fundamentacao": "Art. 6º-A da Lei nº 8.080/1990 (alterada pela Lei nº 14.654/2023)",
        "palavras_chave": [
            "estoque medicamentos", "disponibilidade medicamentos", "farmácias públicas",
            "inventário medicamentos", "controle estoque", "medicamentos disponíveis"
        ],
        "sinonimos": [
            "reserva medicamentos", "quantidade medicamentos", "saldo medicamentos",
            "provisão medicamentos", "suprimento medicamentos", "acervo medicamentos"
        ]
    },

    # EDUCAÇÃO
    "19.1": {
        "dimensao": "Educação",
        "id": "19.1",
        "criterio": "Divulga o plano de educação e o respectivo relatório de resultados?",
        "classificacao": "Recomendada",
        "fundamentacao": "Art. 37, 'caput' da CF; Art. 8º, § 1º, V, da Lei nº 12.527/2011 – LAI e Art. 8º da Lei nº 13.005/2014.",
        "palavras_chave": [
            "plano educação", "PME", "plano municipal educação",
            "metas educação", "relatório educação", "política educacional"
        ],
        "sinonimos": [
            "planejamento educacional", "estratégia educação", "programa educação",
            "diretrizes educação", "objetivos educação", "resultados educação"
        ]
    },
    
    "19.2": {
        "dimensao": "Educação",
        "id": "19.2",
        "criterio": "Divulga a lista de espera em creches públicas e os critérios de priorização de acesso a elas?",
        "classificacao": "Obrigatória",
        "fundamentacao": "Art. 37, 'caput' da CF e Art. 8º, § 1º, V, da Lei nº 12.527/2011 – LAI; Art. 5º, §1º, IV da Lei nº 9.394/96 (LDB, alterada pela Lei nº 14.685/23)",
        "palavras_chave": [
            "lista espera creches", "fila creches", "vagas creches",
            "critérios priorização", "acesso creches", "educação infantil"
        ],
        "sinonimos": [
            "aguardo vagas", "ordem matrícula", "prioridade matrícula",
            "sequência atendimento", "critérios seleção", "regras acesso"
        ]
    }
}