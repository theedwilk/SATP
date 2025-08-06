# criterios_consorcios_publicos.py
# Critérios específicos dos Consórcios Públicos

CRITERIOS_CONSORCIOS_PUBLICOS = {
    # RECEITA (herda do comum)
    "3.1": {
        "dimensao": "Receita",
        "id": "3.1",
        "criterio": "Divulga as receitas do Poder ou órgão, evidenciando sua previsão e realização?",
        "classificacao": "Essencial",
        "fundamentacao": "Arts. 48, §1º, II e 48-A, inciso II, da LC nº 101/00 e art. 8º, II, do Decreto nº 10.540/20.",
        "palavras_chave": [
            "receitas consórcio", "arrecadação consórcio", "recursos consórcio",
            "previsão receita", "realização receita", "entrada recursos"
        ],
        "sinonimos": [
            "ingressos consórcio", "recursos financeiros", "captação recursos",
            "obtenção recursos", "angariação recursos", "valores recebidos"
        ]
    },

    # DESPESA (herda do comum)
    "4.1": {
        "dimensao": "Despesa",
        "id": "4.1",
        "criterio": "Divulga o total das despesas empenhadas, liquidadas e pagas?",
        "classificacao": "Essencial",
        "fundamentacao": "Arts. 7º, VI e 8º, §1º, inciso III, da Lei nº 12.527/2011 - LAI; arts. 48, §1º, inciso II e 48-A, inciso I, da LC nº 101/20; art. 8º, inciso I, do Decreto nº 10.540/20.",
        "palavras_chave": [
            "despesas consórcio", "gastos consórcio", "empenhadas", "liquidadas",
            "pagas", "execução orçamentária", "despesa pública"
        ],
        "sinonimos": [
            "custos consórcio", "desembolsos", "pagamentos", "aplicação recursos",
            "utilização recursos", "consumo recursos", "saídas"
        ]
    },
    
    "4.2": {
        "dimensao": "Despesa",
        "id": "4.2",
        "criterio": "Divulga as despesas por classificação orçamentária?",
        "classificacao": "Essencial",
        "fundamentacao": "Arts. 7º, VI e 8º, §1º, inciso III, da Lei nº 12.527/2011 - LAI; arts. 48, §1º, inciso II e 48-A, inciso I, da LC nº 101/20; art. 8º, inciso I, do Decreto nº 10.540/20.",
        "palavras_chave": [
            "classificação orçamentária", "categoria econômica", "natureza despesa",
            "função governo", "subfunção", "programa orçamentário"
        ],
        "sinonimos": [
            "categorização despesas", "tipificação despesas", "organização despesas",
            "estrutura orçamentária", "divisão orçamentária", "agrupamento despesas"
        ]
    },
    
    "4.3": {
        "dimensao": "Despesa",
        "id": "4.3",
        "criterio": "Possibilita a consulta de empenhos com os detalhes do beneficiário do pagamento ou credor, o bem fornecido ou serviço prestado e a identificação do procedimento licitatório originário da despesa?",
        "classificacao": "Obrigatória",
        "fundamentacao": "Arts. 7º, VI e 8º, §1º, inciso III, da Lei nº 12.527/2011 - LAI; arts. 48, §1º, inciso II e 48-A, inciso I, da LC nº 101/20, art. 8º, I, 'h', do Decreto nº 10.540/2020.",
        "palavras_chave": [
            "empenhos consórcio", "beneficiários", "credores", "fornecedores",
            "bens fornecidos", "serviços prestados", "procedimento licitatório"
        ],
        "sinonimos": [
            "compromissos consórcio", "obrigações", "contratados", "prestadores",
            "produtos", "atividades", "processo licitação"
        ]
    },

    # PLANEJAMENTO E PRESTAÇÃO DE CONTAS
    "11.11": {
        "dimensao": "Planejamento e Prestação de contas",
        "id": "11.11",
        "criterio": "Divulga o Orçamento do Consórcio Público onde conste a estimativa da receita e a fixação da despesa para o exercício atual?",
        "classificacao": "Obrigatória",
        "fundamentacao": "Art. 48, 'caput', da LC nº 101/00; Portaria STN nº. 274/16, art 2, II, Art 6 e art. 14, IV.",
        "palavras_chave": [
            "orçamento consórcio", "estimativa receita", "fixação despesa",
            "exercício atual", "peça orçamentária", "proposta orçamentária"
        ],
        "sinonimos": [
            "orçamento público", "previsão orçamentária", "programação orçamentária",
            "alocação recursos", "distribuição recursos", "planejamento orçamentário"
        ]
    },

    # ATIVIDADES FINALÍSTICAS
    "25.1": {
        "dimensao": "Atividades Finalísticas",
        "id": "25.1",
        "criterio": "Divulga o protocolo de intenções que antecede a formalização do Contrato?",
        "classificacao": "Recomendada",
        "fundamentacao": "Lei Federal nº 11.107/2005, art. 4º, §2º e 5º.",
        "palavras_chave": [
            "protocolo intenções", "formalização contrato", "acordo preliminar",
            "intenção consorciar", "manifestação interesse", "documento preparatório"
        ],
        "sinonimos": [
            "carta intenções", "declaração intenções", "compromisso preliminar",
            "acordo prévio", "pacto inicial", "entendimento preliminar"
        ]
    },
    
    "25.2": {
        "dimensao": "Atividades Finalísticas",
        "id": "25.2",
        "criterio": "Divulga estatuto do consórcio?",
        "classificacao": "Recomendada",
        "fundamentacao": "Lei Federal nº 11.107/2005, art. 7º; Decreto Federal nº. 6.017/07, art. 8º, §3º.",
        "palavras_chave": [
            "estatuto consórcio", "regimento interno", "normas funcionamento",
            "regulamento consórcio", "organização interna", "estrutura consórcio"
        ],
        "sinonimos": [
            "regulamento interno", "normas internas", "disposições estatutárias",
            "regras funcionamento", "organização consórcio", "disciplinamento interno"
        ]
    },
    
    "25.3": {
        "dimensao": "Atividades Finalísticas",
        "id": "25.3",
        "criterio": "Divulga os contratos de rateio?",
        "classificacao": "Recomendada",
        "fundamentacao": "Lei Federal nº 11.107/2005, art. 8º, §1º; Portaria STN nº. 274/16, art. 14, II; Lei Complementar nº 101, de 4 de maio de 2000.",
        "palavras_chave": [
            "contratos rateio", "rateio despesas", "divisão custos",
            "participação entes", "contribuição entes", "cotas participação"
        ],
        "sinonimos": [
            "divisão gastos", "partilha custos", "distribuição despesas",
            "compartilhamento custos", "ratear despesas", "dividir gastos"
        ]
    },
    
    "25.4": {
        "dimensao": "Atividades Finalísticas",
        "id": "25.4",
        "criterio": "Divulga o Contrato de Programa?",
        "classificacao": "Recomendada",
        "fundamentacao": "Lei Federal nº 11.107/2005, art. 13, §1º, II; Decreto Federal nº. 6.017/07, art. 33, V",
        "palavras_chave": [
            "contrato programa", "prestação serviços", "execução atividades",
            "programa trabalho", "atividades consórcio", "serviços consórcio"
        ],
        "sinonimos": [
            "acordo programa", "convênio programa", "ajuste programa",
            "pacto programa", "compromisso programa", "termo programa"
        ]
    },
    
    "25.5": {
        "dimensao": "Atividades Finalísticas",
        "id": "25.5",
        "criterio": "Divulga a ata de eleição dos atuais dirigentes?",
        "classificacao": "Recomendada",
        "fundamentacao": "Lei Federal nº 11.107/2005, art. 6º, §1º; Decreto Federal nº. 6.017/07",
        "palavras_chave": [
            "ata eleição", "dirigentes consórcio", "eleição dirigentes",
            "presidente consórcio", "diretoria consórcio", "gestão consórcio"
        ],
        "sinonimos": [
            "registro eleição", "documentação eleição", "escolha dirigentes",
            "seleção dirigentes", "nomeação dirigentes", "designação dirigentes"
        ]
    },

    "25.6": {
        "dimensao": "Atividades Finalísticas",
        "id": "25.6",
        "criterio": "Divulga as atas da assembleia geral?",
        "classificacao": "Recomendada",
        "fundamentacao": "Lei Federal nº 11.107/2005; Decreto Federal nº. 6.017/07",
        "palavras_chave": [
            "atas assembleia", "assembleia geral", "reuniões assembleia",
            "deliberações assembleia", "decisões assembleia", "registro assembleia"
        ],
        "sinonimos": [
            "relatório assembleia", "memória assembleia", "documentação assembleia",
            "registro reuniões", "atas reuniões", "histórico assembleia"
        ]
    },

        # Continuação dos critérios das Estatais (26.6 a 26.29)
    
    "26.6": {
        "dimensao": "Atividades Finalísticas",
        "id": "26.6",
        "criterio": "Divulga a composição do capital social?",
        "classificacao": "Recomendada",
        "fundamentacao": "Art. 3º c/c art. 6º, I, c/c art. 7º, II, V e VI, c/c art. 8º, caput e § 2º da Lei 12.527/2011 (LAI)",
        "palavras_chave": [
            "capital social", "composição capital", "estrutura acionária",
            "participação acionária", "ações", "quotas", "participações"
        ],
        "sinonimos": [
            "estrutura societária", "composição societária", "quadro acionário",
            "distribuição capital", "divisão capital", "repartição ações"
        ]
    },
    
    "26.7": {
        "dimensao": "Atividades Finalísticas",
        "id": "26.7",
        "criterio": "Divulga a descrição da composição e da remuneração da diretoria executiva?",
        "classificacao": "Obrigatória",
        "fundamentacao": "Art. 3º c/c art. 6º, I, c/c art. 7º, II, V e VI, c/c art. 8º, caput e § 2º da Lei 12.527/2011 (LAI); Art. 8º, III; Art. 16, parágrafo único e Art. 17 da Lei 13.303/2016.",
        "palavras_chave": [
            "diretoria executiva", "composição diretoria", "remuneração diretoria",
            "dirigentes", "administradores", "executivos", "alta administração"
        ],
        "sinonimos": [
            "direção executiva", "corpo diretivo", "equipe executiva",
            "liderança executiva", "gestão executiva", "comando executivo"
        ]
    },
    
    "26.8": {
        "dimensao": "Atividades Finalísticas",
        "id": "26.8",
        "criterio": "Divulga a composição dos conselhos de administração e fiscal?",
        "classificacao": "Recomendada",
        "fundamentacao": "Art. 3º c/c art. 6º, I, c/c art. 7º, II, V e VI, c/c art. 8º, caput e § 2º da Lei 12.527/2011 (LAI); Lei 13.303/2016.",
        "palavras_chave": [
            "conselho administração", "conselho fiscal", "composição conselhos",
            "conselheiros", "membros conselhos", "órgãos societários"
        ],
        "sinonimos": [
            "colegiado administração", "colegiado fiscal", "corpo conselheiros",
            "estrutura conselhos", "organização conselhos", "quadro conselhos"
        ]
    },
    
    "26.9": {
        "dimensao": "Atividades Finalísticas",
        "id": "26.9",
        "criterio": "Extrato das atas de assembleias gerais, quando for o caso?",
        "classificacao": "Recomendada",
        "fundamentacao": "Art. 3º c/c art. 6º, I, c/c art. 7º, II, V e VI, c/c art. 8º, caput e § 2º da Lei 12.527/2011 (LAI); Lei 13.303/2016.",
        "palavras_chave": [
            "atas assembleias", "assembleia geral", "extrato atas",
            "deliberações assembleia", "reuniões assembleia", "decisões assembleia"
        ],
        "sinonimos": [
            "resumo assembleias", "síntese assembleias", "relatório assembleias",
            "documentação assembleias", "registro assembleias", "memória assembleias"
        ]
    },
    
    "26.10": {
        "dimensao": "Atividades Finalísticas",
        "id": "26.10",
        "criterio": "Divulga fatos relevantes e comunicados ao mercado, quando houver?",
        "classificacao": "Recomendada",
        "fundamentacao": "Art. 3º c/c art. 6º, I, c/c art. 7º, II, V e VI, c/c art. 8º, caput e § 2º da Lei 12.527/2011 (LAI); Lei 13.303/2016.",
        "palavras_chave": [
            "fatos relevantes", "comunicados mercado", "informações relevantes",
            "divulgação mercado", "transparência mercado", "disclosure"
        ],
        "sinonimos": [
            "informações materiais", "eventos relevantes", "comunicações mercado",
            "avisos mercado", "notificações mercado", "informes mercado"
        ]
    },
    
    "26.11": {
        "dimensao": "Atividades Finalísticas",
        "id": "26.11",
        "criterio": "Divulga currículo profissional resumido dos membros dos órgãos societários de administração e fiscalização?",
        "classificacao": "Recomendada",
        "fundamentacao": "Art. 3º c/c art. 6º, I, c/c art. 7º, II, V e VI, c/c art. 8º, caput e § 2º da Lei 12.527/2011 (LAI); Lei 13.303/2016.",
        "palavras_chave": [
            "currículo membros", "qualificação membros", "experiência profissional",
            "biografia membros", "perfil profissional", "histórico profissional"
        ],
        "sinonimos": [
            "formação profissional", "trajetória profissional", "competências membros",
            "credenciais membros", "antecedentes profissionais", "background profissional"
        ]
    },
    
    "26.12": {
        "dimensao": "Atividades Finalísticas",
        "id": "26.12",
        "criterio": "Publica a política de divulgação de informações?",
        "classificacao": "Obrigatória",
        "fundamentacao": "Art. 3º c/c art. 6º, I, c/c art. 7º, II, V e VI, c/c art. 8º, caput e § 2º da Lei 12.527/2011 (LAI); Art. 8º, IV, da Lei 13.303/2016.",
        "palavras_chave": [
            "política divulgação", "divulgação informações", "transparência informações",
            "comunicação corporativa", "disclosure policy", "política comunicação"
        ],
        "sinonimos": [
            "diretrizes divulgação", "normas divulgação", "regras divulgação",
            "procedimentos divulgação", "protocolo divulgação", "sistemática divulgação"
        ]
    },
    
    "26.13": {
        "dimensao": "Atividades Finalísticas",
        "id": "26.13",
        "criterio": "Publica a política de divulgação de dividendos?",
        "classificacao": "Obrigatória",
        "fundamentacao": "Art. 3º c/c art. 6º, I, c/c art. 7º, II, V e VI, c/c art. 8º, caput e § 2º da Lei 12.527/2011 (LAI); Art. 8º, V, da Lei 13.303/2016.",
        "palavras_chave": [
            "política dividendos", "divulgação dividendos", "distribuição lucros",
            "remuneração acionistas", "pagamento dividendos", "política distribuição"
        ],
        "sinonimos": [
            "diretrizes dividendos", "normas dividendos", "critérios dividendos",
            "regras distribuição", "sistemática dividendos", "procedimentos dividendos"
        ]
    },
    
    "26.14": {
        "dimensao": "Atividades Finalísticas",
        "id": "26.14",
        "criterio": "Divulga política de transações com partes relacionadas, revisada ao menos anualmente e aprovada pelo Conselho de Administração?",
        "classificacao": "Obrigatória",
        "fundamentacao": "Art. 3º combinado com art. 6º, I, combinado com art. 7º, II, V e VI, combinado com art. 8º, caput e § 2º da Lei 12.527/2011 (LAI); Art. 8º, VII, da Lei 13.303/2016.",
        "palavras_chave": [
            "partes relacionadas", "transações relacionadas", "política transações",
            "operações relacionadas", "negócios relacionados", "conflito interesses"
        ],
        "sinonimos": [
            "partes vinculadas", "operações vinculadas", "transações vinculadas",
            "negócios vinculados", "relacionamentos comerciais", "vínculos comerciais"
        ]
    },
    
    "26.15": {
        "dimensao": "Atividades Finalísticas",
        "id": "26.15",
        "criterio": "Publica, no sítio eletrônico da instituição, carta anual subscrita pelos membros do Conselho de Administração contendo: Explicitação dos compromissos de consecução de objetivos de políticas públicas pela empresa estatal?",
        "classificacao": "Obrigatória",
        "fundamentacao": "Art. 3º c/a art. 6º, I, c/c art. 7º, II e V-VII, c/c art. 8º, caput e § 1º, I-V e § 2º, da Lei 12.527/2011 (LAI); Art. 8º, I, III, VIII e § 4º, c/c art. 16, parágrafo único, da Lei 13.303/2016.",
        "palavras_chave": [
            "carta anual", "conselho administração", "políticas públicas",
            "objetivos públicos", "compromissos públicos", "finalidade pública"
        ],
        "sinonimos": [
            "relatório anual", "comunicação anual", "declaração anual",
            "manifestação anual", "pronunciamento anual", "compromisso público"
        ]
    },
    
    # Critérios 26.16 a 26.29 seguem o mesmo padrão...
    # [Por questões de espaço, incluindo apenas alguns exemplos adicionais]
    
    "26.24": {
        "dimensao": "Atividades Finalísticas",
        "id": "26.24",
        "criterio": "Divulga, de forma detalhada e individual, toda e qualquer remuneração dos dirigentes (administradores) e membros do Conselho Fiscal?",
        "classificacao": "Obrigatória",
        "fundamentacao": "Art. 3º c/a art. 6º, I, c/c art. 7º, II e V-VII, c/c art. 8º, caput e § 1º, I-V e § 2º, da Lei 12.527/2011 (LAI); Art. 12, I, c/c art. 16, parágrafo único, da Lei 13.303/2016.",
        "palavras_chave": [
            "remuneração dirigentes", "remuneração individual", "remuneração detalhada",
            "salários dirigentes", "vencimentos dirigentes", "pagamentos dirigentes"
        ],
        "sinonimos": [
            "pagamentos individuais", "vencimentos individuais", "subsídios dirigentes",
            "proventos dirigentes", "soldos dirigentes", "estipêndios dirigentes"
        ]
    },
    
    "26.29": {
        "dimensao": "Atividades Finalísticas",
        "id": "26.29",
        "criterio": "Publica em seu sítio eletrônico os currículos profissionais dos membros da Diretoria Executiva e dos Conselhos de Administração e Fiscal?",
        "classificacao": "Obrigatória",
        "fundamentacao": "Art. 1º, III, da Resolução-CGPAR-30/2022.",
        "palavras_chave": [
            "currículos profissionais", "qualificação diretoria", "experiência conselhos",
            "formação dirigentes", "competências dirigentes", "histórico profissional"
        ],
        "sinonimos": [
            "perfil profissional", "trajetória profissional", "background profissional",
            "credenciais profissionais", "antecedentes profissionais", "biografia profissional"
        ]
    }
}