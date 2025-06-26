# criterios_estatais.py
# Critérios específicos para Estatais (Dependentes)
# Aplicável aos órgãos classificados como "Estatais"

CRITERIOS_ESTATAIS = {
    # ===== DESPESA =====
    "4.4": {
        "dimensao": "Despesa",
        "id": "4.4",
        "criterio": "Publica relação das despesas com aquisições de bens efetuadas pela instituição contendo: identificação do bem, preço unitário, quantidade, nome do fornecedor e valor total de cada aquisição?",
        "classificacao": "Recomendada",
        "fundamentacao": "Estatais Dependentes: Art. 3º c/c art. 6º, I, c/c art. 7º, II e VI, c/c art. 8º, caput e § 1º, III-IV e § 2º da Lei 12.527/2011 (LAI); Art. 48 da Lei 13.303/2016. Estatais Independentes: Arts. 3º, III, 6º, I, e 8º, §2º, da Lei nº 12.527/2011(LAI).",
        "palavras_chave": [
            "despesas aquisições", "aquisições bens", "relação despesas", "compras bens",
            "fornecedores", "preço unitário", "valor aquisição", "identificação bem"
        ],
        "sinonimos": [
            "gastos aquisições", "compras materiais", "despesas compras",
            "aquisição produtos", "fornecimento bens", "custos aquisições"
        ]
    },
    
    "4.5": {
        "dimensao": "Despesa",
        "id": "4.5",
        "criterio": "Publica informações sobre despesas de patrocínio?",
        "classificacao": "Recomendada",
        "fundamentacao": "Art. 3º c/c art. 6º, I, c/c art. 7º, II e VI, c/c art. 8º, caput e § 1º, III-IV e § 2º da Lei 12.527/2011 (LAI); Art. 93 da Lei 13.303/2016",
        "palavras_chave": [
            "despesas patrocínio", "patrocínio", "gastos patrocínio", "investimento patrocínio",
            "apoio eventos", "sponsorship", "patrocinios", "patrocinio"
        ],
        "sinonimos": [
            "custos patrocínio", "verbas patrocínio", "recursos patrocínio",
            "financiamento eventos", "apoio financeiro", "investimentos marketing"
        ]
    },
    
    "4.6": {
        "dimensao": "Despesa",
        "id": "4.6",
        "criterio": "Publica informações detalhadas sobre a execução dos contratos de publicidade, com nomes dos fornecedores de serviços especializados e veículos, bem como informações sobre os totais de valores pagos para cada tipo de serviço e meio de divulgação?",
        "classificacao": "Recomendada",
        "fundamentacao": "Art. 3º c/c art. 6º, I, c/c art. 7º, II e VI, c/c art. 8º, caput e § 1º, III-IV e § 2º da Lei 12.527/2011 (LAI); Art. 93 da Lei 13.303/2016; Art. 10 da Lei 12.232/2010.",
        "palavras_chave": [
            "contratos publicidade", "despesas publicidade", "fornecedores publicidade",
            "veículos comunicação", "serviços especializados", "meio divulgação", "gastos marketing"
        ],
        "sinonimos": [
            "gastos propaganda", "custos comunicação", "investimento marketing",
            "despesas propaganda", "contratos marketing", "publicidade institucional"
        ]
    },
    
    # ===== LICITAÇÕES =====
    "8.8": {
        "dimensao": "Licitações",
        "id": "8.8",
        "criterio": "Divulga regulamento interno de licitações e contratos?",
        "classificacao": "Obrigatória",
        "fundamentacao": "Art. 3º combinado com art. 6º, I, combinado com art. 7º, II, V e VI, combinado com art. 8º, caput e § 2º da Lei 12.527/2011 (LAI); Art. 40 da Lei 13.303/2016.",
        "palavras_chave": [
            "regulamento interno", "regulamento licitações", "normas licitações",
            "procedimentos licitações", "regras licitações", "manual licitações"
        ],
        "sinonimos": [
            "normas internas", "diretrizes licitações", "política licitações",
            "instrução normativa", "procedimento interno", "regimento licitações"
        ]
    },
    
    # ===== PLANEJAMENTO E PRESTAÇÃO DE CONTAS =====
    "11.12": {
        "dimensao": "Planejamento e Prestação de contas",
        "id": "11.12",
        "criterio": "Divulga as demonstrações financeiras trimestrais?",
        "classificacao": "Recomendada",
        "fundamentacao": "Art. 3º combinado com art. 6º, I, combinado com art. 7º, II, V e VI, combinado com art. 8º, caput e § 2º da Lei 12.527/2011 (LAI);",
        "palavras_chave": [
            "demonstrações financeiras", "demonstrações trimestrais", "balanços trimestrais",
            "relatórios financeiros", "demonstrativos financeiros", "balancetes trimestrais"
        ],
        "sinonimos": [
            "relatórios contábeis", "demonstrativos contábeis", "balanços periódicos",
            "informações financeiras", "dados financeiros", "resultados trimestrais"
        ]
    },
    
    "11.13": {
        "dimensao": "Planejamento e Prestação de contas",
        "id": "11.13",
        "criterio": "Divulga as demonstrações financeiras (contábeis) acompanhadas dos pareceres do Conselho Fiscal e da auditoria independente?",
        "classificacao": "Recomendada",
        "fundamentacao": "Art. 3º combinado com art. 6º, I, combinado com art. 7º, II, V e VI, combinado com art. 8º, caput e § 2º da Lei 12.527/2011 (LAI).",
        "palavras_chave": [
            "demonstrações contábeis", "pareceres conselho fiscal", "auditoria independente",
            "relatório auditores", "parecer auditoria", "demonstrações auditadas"
        ],
        "sinonimos": [
            "balanços auditados", "relatórios contábeis", "demonstrativos auditados",
            "opinião auditores", "certificação contábil", "validação financeira"
        ]
    },
    
    "11.15": {
        "dimensao": "Planejamento e Prestação de contas",
        "id": "11.15",
        "criterio": "Divulga as demonstrações contábeis auditadas em formato eletrônico editável?",
        "classificacao": "Obrigatória",
        "fundamentacao": "Art. 3º combinado com art. 6º, I, combinado com art. 7º, II, V e VI, combinado com art. 8º, caput e § 2º da Lei 12.527/2011 (LAI); Art. 46, § 1º, do Decreto 8.945/2016",
        "palavras_chave": [
            "formato eletrônico", "formato editável", "demonstrações editáveis",
            "arquivo editável", "planilhas eletrônicas", "dados abertos", "formato digital"
        ],
        "sinonimos": [
            "formato digital", "arquivo manipulável", "dados estruturados",
            "planilhas abertas", "formato processável", "dados reutilizáveis"
        ]
    },
    
    "11.16": {
        "dimensao": "Planejamento e Prestação de contas",
        "id": "11.16",
        "criterio": "Divulga o relatório anual elaborado pelo Comitê de Auditoria Estatutário com informações sobre as atividades e os resultados e suas conclusões e recomendações?",
        "classificacao": "Obrigatória",
        "fundamentacao": "Art. 3º combinado com art. 6º, I, combinado com art. 7º, II, V e VI, combinado com art. 8º, caput e § 2º da Lei 12.527/2011 (LAI); Art. 24, § 1º, VII, da Lei 13.303/2016",
        "palavras_chave": [
            "comitê auditoria", "relatório anual auditoria", "comitê estatutário",
            "conclusões auditoria", "recomendações auditoria", "atividades auditoria"
        ],
        "sinonimos": [
            "comissão auditoria", "relatório auditoria interna", "comitê fiscalização",
            "parecer auditoria", "avaliação auditoria", "controle interno"
        ]
    },
    
    "11.17": {
        "dimensao": "Planejamento e Prestação de contas",
        "id": "11.17",
        "criterio": "Divulga as atas das reuniões do Comitê de Auditoria Estatutário?",
        "classificacao": "Obrigatória",
        "fundamentacao": "Art. 3º combinado com art. 6º, I, combinado com art. 7º, II, V e VI, combinado com art. 8º, caput e § 2º da Lei 12.527/2011 (LAI); Art. 24, § 4º da Lei 13.303/2016",
        "palavras_chave": [
            "atas reuniões", "atas comitê auditoria", "reuniões auditoria",
            "deliberações auditoria", "decisões comitê", "registros reuniões"
        ],
        "sinonimos": [
            "memórias reuniões", "relatórios reuniões", "documentação reuniões",
            "registros comitê", "documentos auditoria", "histórico reuniões"
        ]
    },
    
    "11.18": {
        "dimensao": "Planejamento e Prestação de contas",
        "id": "11.18",
        "criterio": "Divulga as atas das reuniões do Comitê de Elegibilidade Estatutário ou Comitê de Pessoas, Elegibilidade, Sucessão e Remuneração a partir de 2022, na forma de sumário dos fatos ocorridos, inclusive das dissidências e protestos?",
        "classificacao": "Obrigatória",
        "fundamentacao": "Art. 3º combinado com art. 6º, I, combinado com art. 7º, II, V e VI, combinado com art. 8º, caput e § 2º da Lei 12.527/2011 (LAI); Art. 24, § 4º da Lei 13.303/2016",
        "palavras_chave": [
            "comitê elegibilidade", "comitê pessoas", "sucessão remuneração",
            "atas elegibilidade", "sumário fatos", "dissidências protestos"
        ],
        "sinonimos": [
            "comissão elegibilidade", "comitê recursos humanos", "comitê nomeações",
            "reuniões elegibilidade", "deliberações pessoas", "decisões sucessão"
        ]
    },
    
    "11.19": {
        "dimensao": "Planejamento e Prestação de contas",
        "id": "11.19",
        "criterio": "Divulga anualmente relatório integrado ou de sustentabilidade?",
        "classificacao": "Obrigatória",
        "fundamentacao": "Art. 3º combinado com art. 6º, I, combinado com art. 7º, II, V e VI, combinado com art. 8º, caput e § 2º da Lei 12.527/2011 (LAI); Art. 8º, IX, e § 4º da Lei 13.303/2016.",
        "palavras_chave": [
            "relatório integrado", "relatório sustentabilidade", "sustentabilidade",
            "responsabilidade social", "impacto ambiental", "ESG", "governança"
        ],
        "sinonimos": [
            "relatório anual", "relatório corporativo", "balanço social",
            "relatório responsabilidade", "relatório ESG", "relatório gestão"
        ]
    },
    
    # ===== ATIVIDADES FINALÍSTICAS =====
    "26.1": {
        "dimensao": "Atividades Finalísticas",
        "id": "26.1",
        "criterio": "Divulga o plano de negócios para o exercício anual seguinte?",
        "classificacao": "Recomendada",
        "fundamentacao": "Art. 23, §1º, I, da Lei 13.303/2016.",
        "palavras_chave": [
            "plano negócios", "planejamento anual", "estratégia empresarial",
            "plano estratégico", "objetivos anuais", "metas negócios"
        ],
        "sinonimos": [
            "plano empresarial", "estratégia corporativa", "planejamento estratégico",
            "diretrizes anuais", "plano operacional", "programa anual"
        ]
    },
    
    "26.2": {
        "dimensao": "Atividades Finalísticas",
        "id": "26.2",
        "criterio": "Divulga o ato ou lei de criação?",
        "classificacao": "Recomendada",
        "fundamentacao": "Art. 3º c/c art. 6º, I, c/c art. 7º, II, V e VI, c/c art. 8º, caput e § 2º da Lei 12.527/2011 (LAI)",
        "palavras_chave": [
            "ato criação", "lei criação", "decreto criação", "autorização criação",
            "constituição empresa", "fundação empresa", "criação estatal"
        ],
        "sinonimos": [
            "norma criação", "instrumento criação", "documento constitutivo",
            "base legal", "origem legal", "fundamento legal"
        ]
    },
    
    "26.3": {
        "dimensao": "Atividades Finalísticas",
        "id": "26.3",
        "criterio": "Divulga o estatuto social?",
        "classificacao": "Recomendada",
        "fundamentacao": "Art. 3º c/c art. 6º, I, c/c art. 7º, II, V e VI, c/c art. 8º, caput e § 2º da Lei 12.527/2011 (LAI); art. 8º, II da Lei 13.303/2016.",
        "palavras_chave": [
            "estatuto social", "estatuto", "regimento interno", "normas internas",
            "regulamento interno", "carta constitutiva", "documento constitutivo"
        ],
        "sinonimos": [
            "contrato social", "ato constitutivo", "normas societárias",
            "regras internas", "organização interna", "estrutura societária"
        ]
    },
    
    "26.4": {
        "dimensao": "Atividades Finalísticas",
        "id": "26.4",
        "criterio": "Divulga a missão, princípios e valores da instituição?",
        "classificacao": "Recomendada",
        "fundamentacao": "7º, II e VI, c/c art. 8º, caput e § 2º da Lei 12.527/2011 (LAI)",
        "palavras_chave": [
            "missão", "princípios", "valores", "visão", "propósito",
            "filosofia institucional", "cultura organizacional", "identidade corporativa"
        ],
        "sinonimos": [
            "objetivos institucionais", "diretrizes institucionais", "fundamentos",
            "crenças organizacionais", "pilares institucionais", "essência corporativa"
        ]
    },
    
    "26.5": {
        "dimensao": "Atividades Finalísticas",
        "id": "26.5",
        "criterio": "Código de Conduta e Integridade?",
        "classificacao": "Obrigatória",
        "fundamentacao": "Art. 3º c/c art. 6º, I, c/c art. 7º, II, V e VI, c/c art. 8º, caput e § 2º da Lei 12.527/2011 (LAI); Art. 9º, § 1º, Lei 13.303/2016; Art. 18 do do Decreto 8.945/2016.",
        "palavras_chave": [
            "código conduta", "código integridade", "código ética", "normas conduta",
            "padrões éticos", "compliance", "integridade", "ética empresarial"
        ],
        "sinonimos": [
            "manual conduta", "diretrizes éticas", "normas éticas",
            "regulamento ético", "política integridade", "padrões comportamentais"
        ]
    },
    
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
    
    # Critérios 26.15 a 26.29 (Carta Anual e outros)
    "26.15": {
        "dimensao": "Atividades Finalísticas",
        "id": "26.15",
        "criterio": "Publica, no sítio eletrônico da instituição, carta anual subscrita pelos membros do Conselho de Administração contendo: Explicitação dos compromissos de consecução de objetivos de políticas públicas pela empresa estatal e por suas subsidiárias, em atendimento ao interesse coletivo ou ao imperativo de segurança nacional que justificou a autorização de sua criação?",
        "classificacao": "Obrigatória",
        "fundamentacao": "Art. 3º c/a art. 6º, I, c/c art. 7º, II e V-VII, c/c art. 8º, caput e § 1º, I-V e § 2º, da Lei 12.527/2011 (LAI); Art. 8º, I, III, VIII e § 4º, c/c art. 16, parágrafo único, da Lei 13.303/2016; Art. 13, I, III, VIII, § 1º e § 5º do Decreto 8.945/2016.",
        "palavras_chave": [
            "carta anual", "políticas públicas", "objetivos públicos", "interesse coletivo",
            "segurança nacional", "compromissos públicos", "finalidade pública"
        ],
        "sinonimos": [
            "relatório anual", "comunicação anual", "declaração anual",
            "manifestação anual", "pronunciamento anual", "compromisso público"
        ]
    },
    
    "26.24": {
        "dimensao": "Atividades Finalísticas",
        "id": "26.24",
        "criterio": "Divulga, de forma detalhada e individual, toda e qualquer remuneração dos dirigentes (administradores) e membros do Conselho Fiscal?",
        "classificacao": "Obrigatória",
        "fundamentacao": "Art. 3º c/a art. 6º, I, c/c art. 7º, II e V-VII, c/c art. 8º, caput e § 1º, I-V e § 2º, da Lei 12.527/2011 (LAI); Art. 12, I, c/c art. 16, parágrafo único, da Lei 13.303/2016; Art. 2º, VII, c/c art. 13, III e § 5º , c/c art. 19 do Decreto 8.945/2016.",
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

# Funções auxiliares para Estatais
def obter_criterios_estatais():
    """
    Obtém todos os critérios aplicáveis às Estatais (Dependentes)
    
    Returns:
        dict: Dicionário com todos os critérios aplicáveis
    """
    from criterios_comum import CRITERIOS_TRANSPARENCIA
    from criterios_comum_exceto_estatais_independentes import CRITERIOS_COMUM_EXCETO_ESTATAIS_INDEPENDENTES
    
    criterios_aplicaveis = {}
    
    # Adiciona critérios comuns a todos
    criterios_aplicaveis.update(CRITERIOS_TRANSPARENCIA)
    
    # Adiciona critérios comuns exceto estatais independentes
    criterios_aplicaveis.update(CRITERIOS_COMUM_EXCETO_ESTATAIS_INDEPENDENTES)
    
    # Adiciona critérios específicos de estatais
    criterios_aplicaveis.update(CRITERIOS_ESTATAIS)
    
    return criterios_aplicaveis

# Constantes específicas para Estatais
DIMENSOES_ESTATAIS = [
    "Despesa",
    "Licitações", 
    "Planejamento e Prestação de contas",
    "Atividades Finalísticas"
]

CRITERIOS_OBRIGATORIOS_ESTATAIS = [
    "8.8", "11.15", "11.16", "11.17", "11.18", "11.19",
    "26.5", "26.7", "26.12", "26.13", "26.14", "26.15", "26.24", "26.29"
]

CRITERIOS_RECOMENDADOS_ESTATAIS = [
    "4.4", "4.5", "4.6", "11.12", "11.13",
    "26.1", "26.2", "26.3", "26.4", "26.6", "26.8", "26.9", "26.10", "26.11"
]

# Exemplo de uso
if __name__ == "__main__":
    print("=== Critérios Específicos de Estatais ===")
    
    # Lista critérios específicos
    for id_criterio, dados in CRITERIOS_ESTATAIS.items():
        print(f"ID: {id_criterio} - {dados['classificacao']}")
        print(f"Critério: {dados['criterio'][:80]}...")
        print(f"Palavras-chave: {', '.join(dados['palavras_chave'][:3])}...")
        print("-" * 50)
    
    # Estatísticas
    total_criterios = len(CRITERIOS_ESTATAIS)
    obrigatorios = len([c for c in CRITERIOS_ESTATAIS.values() 
                       if c['classificacao'] == 'Obrigatória'])
    recomendados = len([c for c in CRITERIOS_ESTATAIS.values() 
                       if c['classificacao'] == 'Recomendada'])
    
    print(f"\n=== Estatísticas Estatais ===")
    print(f"Total de critérios específicos: {total_criterios}")
    print(f"Obrigatórios: {obrigatorios}")
    print(f"Recomendados: {recomendados}")