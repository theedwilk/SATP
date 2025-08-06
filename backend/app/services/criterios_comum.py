# criterios_comum.py
# Mapeamento de Critérios de Transparência Pública
# Este arquivo é imutável e serve como base para buscas automatizadas em sites

CRITERIOS_TRANSPARENCIA = {
    # INFORMAÇÕES PRIORITÁRIAS
    "1.1": {
        "dimensao": "Informações Prioritárias",
        "id": "1.1",
        "criterio": "Possui sítio oficial próprio na internet?",
        "classificacao": "Essencial",
        "fundamentacao": "Art. 48, §1º, II, da LC nº 101/00 e arts. 3º, III, 6º, I, e 8º, §2º, da Lei nº 12.527/2011 – LAI.",
        "palavras_chave": [
            "site oficial", "sítio oficial", "portal oficial", "página oficial",
            "website oficial", "endereço eletrônico", "domínio próprio"
        ],
        "sinonimos": [
            "homepage", "portal institucional", "site institucional",
            "página web", "endereço na internet", "presença digital"
        ]
    },
    
    "1.2": {
        "dimensao": "Informações Prioritárias",
        "id": "1.2",
        "criterio": "Possui portal da transparência próprio ou compartilhado na internet?",
        "classificacao": "Essencial",
        "fundamentacao": "Art. 48, §1º, II, da LC nº 101/00 e arts. 3º, III, 6º, I, e 8º, §2º, da Lei nº 12.527/2011 – LAI.",
        "palavras_chave": [
            "portal da transparência", "portal transparência", "transparência pública",
            "acesso à informação", "dados abertos", "informações públicas"
        ],
        "sinonimos": [
            "portal de transparência", "transparência", "acesso informação",
            "dados públicos", "informação pública", "prestação de contas"
        ]
    },
    
    "1.3": {
        "dimensao": "Informações Prioritárias",
        "id": "1.3",
        "criterio": "O acesso ao portal transparência está visível na capa do site?",
        "classificacao": "Obrigatória",
        "fundamentacao": "Art. 8º, caput, da Lei nº 12.527/2011 – LAI.",
        "palavras_chave": [
            "transparência", "acesso transparência", "link transparência",
            "menu transparência", "botão transparência", "capa do site"
        ],
        "sinonimos": [
            "página inicial", "home", "menu principal", "navegação principal",
            "acesso direto", "link visível", "destaque"
        ]
    },
    
    "1.4": {
        "dimensao": "Informações Prioritárias",
        "id": "1.4",
        "criterio": "O site e o portal de transparência contêm ferramenta de pesquisa de conteúdo que permita o acesso à informação?",
        "classificacao": "Obrigatória",
        "fundamentacao": "Art. 8º, § 3º, I, da Lei nº 12.527/2011 – LAI.",
        "palavras_chave": [
            "busca", "pesquisa", "buscar", "pesquisar", "ferramenta de busca",
            "campo de pesquisa", "lupa", "search", "filtro"
        ],
        "sinonimos": [
            "localizar", "encontrar", "procurar", "consultar",
            "mecanismo de busca", "sistema de busca", "buscador"
        ]
    },

    # INFORMAÇÕES INSTITUCIONAIS
    "2.1": {
        "dimensao": "Informações Institucionais",
        "id": "2.1",
        "criterio": "Divulga a sua estrutura organizacional?",
        "classificacao": "Obrigatória",
        "fundamentacao": "Art. 8º, § 3º, I, da Lei nº 12.527/2011 – LAI.",
        "palavras_chave": [
            "estrutura organizacional", "organograma", "estrutura administrativa",
            "hierarquia", "organização", "estrutura interna"
        ],
        "sinonimos": [
            "estrutura funcional", "quadro organizacional", "divisão administrativa",
            "departamentos", "setores", "unidades administrativas"
        ]
    },
    
    "2.2": {
        "dimensao": "Informações Institucionais",
        "id": "2.2",
        "criterio": "Divulga competências e/ou atribuições?",
        "classificacao": "Obrigatória",
        "fundamentacao": "Art. 8º, § 1º, I, da Lei nº 12.527/2011 - LAI e art. 6º, VI, b, da Lei 13.460/2017.",
        "palavras_chave": [
            "competências", "atribuições", "responsabilidades", "funções",
            "atividades", "deveres", "obrigações"
        ],
        "sinonimos": [
            "incumbências", "encargos", "tarefas", "finalidades",
            "objetivos", "missão", "propósito"
        ]
    },
    
    "2.3": {
        "dimensao": "Informações Institucionais",
        "id": "2.3",
        "criterio": "Identifica o nome dos atuais responsáveis pela gestão do Poder/Órgão?",
        "classificacao": "Obrigatória",
        "fundamentacao": "Art. 8º, § 3º, I, da Lei nº 12.527/2011 – LAI.",
        "palavras_chave": [
            "responsáveis", "gestores", "dirigentes", "autoridades",
            "administradores", "diretores", "chefes", "líderes"
        ],
        "sinonimos": [
            "titulares", "ocupantes", "incumbidos", "encarregados",
            "comando", "direção", "chefia", "gerência"
        ]
    },
    
    "2.4": {
        "dimensao": "Informações Institucionais",
        "id": "2.4",
        "criterio": "Divulga os endereços e telefones atuais do Poder ou órgão e e-mails institucionais?",
        "classificacao": "Obrigatória",
        "fundamentacao": "Art. 8º, § 1º, I, da Lei nº 12.527/2011 - LAI e art. 6º, VI, b, da Lei 13.460/2017.",
        "palavras_chave": [
            "contato", "endereço", "telefone", "e-mail", "email",
            "localização", "fale conosco", "contatos"
        ],
        "sinonimos": [
            "comunicação", "correspondência", "informações de contato",
            "dados para contato", "canais de comunicação", "atendimento"
        ]
    },
    
    "2.5": {
        "dimensao": "Informações Institucionais",
        "id": "2.5",
        "criterio": "Divulga o horário de atendimento?",
        "classificacao": "Obrigatória",
        "fundamentacao": "Art. 8º, § 1º, I, da Lei nº 12.527/2011 - LAI e art. 6º, VI, b, da Lei 13.460/2017.",
        "palavras_chave": [
            "horário de atendimento", "horário de funcionamento", "horários",
            "expediente", "funcionamento", "atendimento ao público"
        ],
        "sinonimos": [
            "período de atendimento", "horário de trabalho", "jornada",
            "plantão", "disponibilidade", "tempo de funcionamento"
        ]
    },
    
    "2.6": {
        "dimensao": "Informações Institucionais",
        "id": "2.6",
        "criterio": "Divulga os atos normativos próprios?",
        "classificacao": "Obrigatória",
        "fundamentacao": "Art. 37 da CF (princípio da publicidade) e arts. 3º, II; 6°, inciso I; 7º, incisos II, V e VI e 8º da Lei nº 12.527/2011 – LAI.",
        "palavras_chave": [
            "atos normativos", "legislação", "normas", "regulamentos",
            "portarias", "decretos", "resoluções", "instruções normativas"
        ],
        "sinonimos": [
            "documentos normativos", "atos administrativos", "normativas",
            "disposições", "diretrizes", "ordenamentos", "regulamentações"
        ]
    },
    
    "2.7": {
        "dimensao": "Informações Institucionais",
        "id": "2.7",
        "criterio": "Divulga as perguntas e respostas mais frequentes relacionadas às atividades desenvolvidas pelo Poder/Órgão?",
        "classificacao": "Obrigatória",
        "fundamentacao": "Art. 8º, § 1º, I, da Lei nº 12.527/2011 – LAI.",
        "palavras_chave": [
            "FAQ", "perguntas frequentes", "dúvidas frequentes",
            "perguntas e respostas", "questões frequentes", "esclarecimentos"
        ],
        "sinonimos": [
            "dúvidas comuns", "questionamentos", "consultas frequentes",
            "orientações", "informações úteis", "ajuda"
        ]
    },
    
    "2.8": {
        "dimensao": "Informações Institucionais",
        "id": "2.8",
        "criterio": "Participa em redes sociais e apresenta, no seu sítio institucional, link de acesso ao seu perfil?",
        "classificacao": "Recomendada",
        "fundamentacao": "Arts. 3º, III, 6º, I, e 8º, §2º, da Lei nº 12.527/2011 – LAI.",
        "palavras_chave": [
            "redes sociais", "facebook", "twitter", "instagram", "youtube",
            "linkedin", "whatsapp", "telegram", "mídias sociais"
        ],
        "sinonimos": [
            "plataformas sociais", "canais digitais", "perfis sociais",
            "comunicação digital", "interação social", "presença nas redes"
        ]
    },
    
    "2.9": {
        "dimensao": "Informações Institucionais",
        "id": "2.9",
        "criterio": "Inclui botão do Radar da Transparência Pública no site institucional ou portal transparência?",
        "classificacao": "Recomendada",
        "fundamentacao": "Art. 37 da CF (princípio da publicidade) e art. 3º da Lei nº 12.527/2011 – LAI.",
        "palavras_chave": [
            "radar da transparência", "radar transparência", "botão radar",
            "link radar", "acesso radar", "transparência radar"
        ],
        "sinonimos": [
            "sistema radar", "ferramenta radar", "portal radar",
            "monitoramento transparência", "avaliação transparência"
        ]
    },

    # CONVÊNIOS E TRANSFERÊNCIAS
    "5.1": {
        "dimensao": "Convênios e Transferências",
        "id": "5.1",
        "criterio": "Identifica as transferências recebidas a partir da celebração de convênios/acordos com indicação, no mínimo, do valor total previsto dos recursos envolvidos, do valor recebido, do objeto e da origem (órgão repassador/concedente)?",
        "classificacao": "Obrigatória",
        "fundamentacao": "Art. 8º, § 1º, inciso II, da Lei nº 12.527/2011 – LAI.",
        "palavras_chave": [
            "convênios", "transferências", "acordos", "repasses",
            "recursos recebidos", "valores recebidos", "origem recursos"
        ],
        "sinonimos": [
            "ajustes", "parcerias", "cooperação", "financiamentos",
            "subsídios", "auxílios", "subvenções", "aportes"
        ]
    },
    
    "5.2": {
        "dimensao": "Convênios e Transferências",
        "id": "5.2",
        "criterio": "Identifica as transferências realizadas a partir da celebração de convênios/acordos/ajustes, com indicação, no mínimo, do beneficiário, do objeto, do valor total previsto para repasse e do valor concedido?",
        "classificacao": "Obrigatória",
        "fundamentacao": "Art. 8º, §1º, inciso II, da Lei nº 12.527/2011 - LAI e art. 8º, inciso I, "f" do Decreto nº 10.540/20.",
        "palavras_chave": [
            "transferências realizadas", "repasses efetuados", "valores repassados",
            "beneficiários", "convênios celebrados", "recursos transferidos"
        ],
        "sinonimos": [
            "concessões", "destinações", "liberações", "pagamentos",
            "desembolsos", "entregas", "remessas", "envios"
        ]
    },
    
    "5.3": {
        "dimensao": "Convênios e Transferências",
        "id": "5.3",
        "criterio": "Identifica os acordos firmados que não envolvam transferência de recursos financeiros, identificando as partes, o objeto e as obrigações ajustadas?",
        "classificacao": "Obrigatória",
        "fundamentacao": "Art. 37, caput da CF e Art. 8º, § 1º, V, da Lei nº 12.527/2011 – LAI.",
        "palavras_chave": [
            "acordos", "parcerias", "cooperação técnica", "termos de cooperação",
            "memorandos", "protocolos", "ajustes não financeiros"
        ],
        "sinonimos": [
            "entendimentos", "pactos", "alianças", "colaborações",
            "articulações", "vínculos", "relacionamentos", "compromissos"
        ]
    },

    # RECURSOS HUMANOS
    "6.1": {
        "dimensao": "Recursos Humanos",
        "id": "6.1",
        "criterio": "Divulga a relação nominal dos servidores/autoridades/membros, seus cargos/funções, as respectivas lotações, as suas datas de admissão/exoneração/inativação e a carga horária do cargo/função ocupada/desempenhada?",
        "classificacao": "Obrigatória",
        "fundamentacao": "Arts. 37, caput (princípios da publicidade e moralidade) e 39, § 6º, da CF; arts. 3º, incisos I, II, III, IV e V, e 8º da Lei nº 12.527/2011 – LAI.",
        "palavras_chave": [
            "servidores", "funcionários", "pessoal", "quadro de pessoal",
            "relação nominal", "cargos", "funções", "lotação"
        ],
        "sinonimos": [
            "colaboradores", "agentes públicos", "empregados", "trabalhadores",
            "corpo funcional", "recursos humanos", "staff", "equipe"
        ]
    },
    
    "6.2": {
        "dimensao": "Recursos Humanos",
        "id": "6.2",
        "criterio": "Identifica a remuneração nominal de cada servidor/autoridade/Membro e a tabela com o padrão remuneratório dos cargos e funções?",
        "classificacao": "Obrigatória",
        "fundamentacao": "Arts. 37, caput (princípios da publicidade e moralidade) e 39, § 6º, da CF; arts. 3º, incisos I, II, III, IV e V, e 8º da Lei nº 12.527/2011 – LAI.",
        "palavras_chave": [
            "remuneração", "salários", "vencimentos", "subsídios",
            "tabela salarial", "padrão remuneratório", "proventos"
        ],
        "sinonimos": [
            "pagamentos", "soldos", "ordenados", "estipêndios",
            "gratificações", "adicionais", "benefícios", "verbas"
        ]
    },
    
    "6.3": {
        "dimensao": "Recursos Humanos",
        "id": "6.3",
        "criterio": "Divulga a lista de seus estagiários?",
        "classificacao": "Recomendada",
        "fundamentacao": "Arts. 37, caput (princípios da publicidade e moralidade) e 39, § 6º, da CF; arts. 3º, incisos I, II, III, IV e V, e 8º da Lei nº 12.527/2011 – LAI.",
        "palavras_chave": [
            "estagiários", "estágio", "estudantes", "aprendizes",
            "bolsistas", "trainee", "programa de estágio"
        ],
        "sinonimos": [
            "estagiários", "estudantes em formação", "aprendizes",
            "jovens aprendizes", "estudantes universitários", "acadêmicos"
        ]
    },
    
    "6.4": {
        "dimensao": "Recursos Humanos",
        "id": "6.4",
        "criterio": "Publica lista dos terceirizados que prestam serviços para o Poder ou órgão/entidades, contendo, em relação a cada um deles: nome completo, função ou atividade exercida e nome da empresa empregadora?",
        "classificacao": "Recomendada",
        "fundamentacao": "Art. 3º, I-III, combinado com art. 6º, I, combinado com art. 7º, II e VI, combinado com art. 8º, caput e § 1º, III e § 2º da Lei 12.527/2011 – LAI.",
        "palavras_chave": [
            "terceirizados", "terceirização", "prestadores de serviço",
            "empresas contratadas", "serviços terceirizados", "contratados"
        ],
        "sinonimos": [
            "fornecedores", "prestadores", "contratadas", "parceiros",
            "subcontratados", "outsourcing", "empresas parceiras"
        ]
    },
    
    "6.5": {
        "dimensao": "Recursos Humanos",
        "id": "6.5",
        "criterio": "Divulga a íntegra dos editais de concursos e seleções públicas realizados pelo Poder ou órgão para provimento de cargos e empregos públicos?",
        "classificacao": "Obrigatória",
        "fundamentacao": "Art. 3º, I-III, combinado com art. 6º, I, combinado com art. 7º, II e VI, combinado com art. 8º, caput e § 1º, IV (por analogia) e § 2º da Lei 12.527/2011 – LAI.",
        "palavras_chave": [
            "concursos públicos", "seleções públicas", "editais",
            "provimento", "cargos públicos", "empregos públicos"
        ],
        "sinonimos": [
            "certames", "processos seletivos", "chamadas públicas",
            "recrutamento", "admissão", "ingresso", "contratação"
        ]
    },
    
    "6.6": {
        "dimensao": "Recursos Humanos",
        "id": "6.6",
        "criterio": "Divulga informações sobre os demais atos dos concursos públicos e processos seletivos do Poder ou órgão, contendo no mínimo a lista de aprovados com as classificações e as nomeações?",
        "classificacao": "Obrigatória",
        "fundamentacao": "Art. 3º, I-III, combinado com art. 6º, I, combinado com art. 7º, II e VI, combinado com art. 8º, caput e § 1º, IV (por analogia) e § 2º da Lei 12.527/2011 – LAI.",
        "palavras_chave": [
            "resultados concursos", "aprovados", "classificação",
            "nomeações", "homologação", "lista de aprovados"
        ],
        "sinonimos": [
            "classificados", "habilitados", "selecionados", "convocados",
            "designados", "empossados", "investidos", "admitidos"
        ]
    },

    # DIÁRIAS
    "7.1": {
        "dimensao": "Diárias",
        "id": "7.1",
        "criterio": "Divulga o nome e o cargo/função do beneficiário, além do valor total recebido, número de diárias usufruídas por afastamento, período de afastamento, motivo do afastamento e local de destino?",
        "classificacao": "Obrigatória",
        "fundamentacao": "Art. 48-A, I, da LC nº 101/00; arts. 3º, incisos I, II, III, IV e V, 7º, incisos VI, e 8º da Lei nº 12.527/2011 - LAI.",
        "palavras_chave": [
            "diárias", "afastamentos", "viagens", "deslocamentos",
            "beneficiários diárias", "valores diárias", "destinos"
        ],
        "sinonimos": [
            "ajudas de custo", "auxílios viagem", "ressarcimentos",
            "indenizações", "compensações", "reembolsos", "custeios"
        ]
    },
    
    "7.2": {
        "dimensao": "Diárias",
        "id": "7.2",
        "criterio": "Divulga tabela ou relação que explicite os valores das diárias dentro do Estado, fora do Estado e fora do país, conforme legislação local?",
        "classificacao": "Obrigatória",
        "fundamentacao": "Art. 48-A, I, da LC nº 101/00; arts. 3º, incisos I, II, III, IV e V, 7º, incisos VI, e 8º da Lei nº 12.527/2011 - LAI.",
        "palavras_chave": [
            "tabela diárias", "valores diárias", "diárias estado",
            "diárias país", "legislação diárias", "regulamento diárias"
        ],
        "sinonimos": [
            "escala valores", "padrões diárias", "critérios diárias",
            "normas diárias", "parâmetros", "diretrizes", "regras"
        ]
    },

    # LICITAÇÕES
    "8.1": {
        "dimensao": "Licitações",
        "id": "8.1",
        "criterio": "Divulga a relação das licitações em ordem sequencial, informando o número e modalidade licitatória, o objeto, a data, o valor estimado/homologado e a situação?",
        "classificacao": "Obrigatória",
        "fundamentacao": "Arts. 7º, VI, e 8º, § 1º, IV, da Lei nº 12.527/2011 – LAI.",
        "palavras_chave": [
            "licitações", "pregões", "tomada de preços", "concorrência",
            "modalidade licitatória", "processos licitatórios", "certames"
        ],
        "sinonimos": [
            "procedimentos licitatórios", "chamadas públicas", "seleções",
            "disputas", "competições", "concursos", "disputas comerciais"
        ]
    },
    
    "8.2": {
        "dimensao": "Licitações",
        "id": "8.2",
        "criterio": "Divulga a íntegra dos editais de licitação?",
        "classificacao": "Obrigatória",
        "fundamentacao": "Arts. 7º, VI, e 8º, §1º, IV, da Lei nº 12.527/2011 – LAI c/c art. 25, § 3º, da Lei 14.133/2021.",
        "palavras_chave": [
            "editais licitação", "editais pregão", "documentos licitação",
            "íntegra editais", "textos editais", "conteúdo editais"
        ],
        "sinonimos": [
            "instrumentos convocatórios", "chamamentos", "convocações",
            "avisos", "publicações", "anúncios", "comunicados"
        ]
    },
    
    "8.3": {
        "dimensao": "Licitações",
        "id": "8.3",
        "criterio": "Divulga a íntegra dos demais documentos das fases interna e externa das licitações?",
        "classificacao": "Obrigatória",
        "fundamentacao": "Arts. 7º, VI, e 8º, § 1º, IV, da Lei nº 12.527/2011 – LAI c/c art. 25, § 3º, da Lei 14.133/2022.",
        "palavras_chave": [
            "documentos licitação", "fases licitação", "procedimentos licitação",
            "atas licitação", "relatórios licitação", "pareceres licitação"
        ],
        "sinonimos": [
            "peças processuais", "documentação", "registros", "arquivos",
            "papéis", "formulários", "instrumentos", "comprovantes"
        ]
    },
    
    "8.4": {
        "dimensao": "Licitações",
        "id": "8.4",
        "criterio": "Divulga a íntegra dos principais documentos dos processos de dispensa e inexigibilidade de licitação?",
        "classificacao": "Obrigatória",
        "fundamentacao": "Arts. 7º, VI, e 8º, §1º, IV, da Lei nº 12.527/2011 – LAI e art. 72, parágrafo único, da Lei nº 14.133/2021.",
        "palavras_chave": [
            "dispensa licitação", "inexigibilidade", "contratação direta",
            "justificativas dispensa", "processos dispensa", "documentos dispensa"
        ],
        "sinonimos": [
            "exceções licitatórias", "contratações emergenciais", "urgências",
            "emergências", "exclusividades", "singularidades", "especialidades"
        ]
    },
    
    "8.5": {
        "dimensao": "Licitações",
        "id": "8.5",
        "criterio": "Divulga a íntegra das Atas de Adesão – SRP?",
        "classificacao": "Obrigatória",
        "fundamentacao": "Arts. 7º, VI, e 8º, §1º, IV, da Lei nº 12.527/2011 – LAI; art. 11, III, do Decreto nº 7.892/2013 e art. 18, §4º, do Decreto nº 11.462/2023.",
        "palavras_chave": [
            "atas adesão", "SRP", "sistema registro preços", "adesões",
            "registro preços", "carona", "participação SRP"
        ],
        "sinonimos": [
            "aproveitamento", "utilização", "compartilhamento", "participação",
            "ingresso", "inclusão", "vinculação", "associação"
        ]
    },
    
    "8.7": {
        "dimensao": "Licitações",
        "id": "8.7",
        "criterio": "Divulga a relação dos licitantes e/ou contratados sancionados administrativamente pelo Poder ou órgão?",
        "classificacao": "Recomendada",
        "fundamentacao": "Art. 156 e 161 da Lei 14.133/2022, e para as estatais: Art. 83 da Lei 13.303/2016.",
        "palavras_chave": [
            "sanções", "penalidades", "punições", "licitantes sancionados",
            "empresas sancionadas", "impedimentos", "suspensões"
        ],
        "sinonimos": [
            "restrições", "proibições", "vedações", "inabilitações",
            "desqualificações", "exclusões", "banimentos", "cassações"
        ]
    },

    # CONTRATOS
    "9.1": {
        "dimensao": "Contratos",
        "id": "9.1",
        "criterio": "Divulga a relação dos contratos celebrados em ordem sequencial, com o seu respectivo resumo, contendo, no mínimo, indicação do contratado(a), do valor, do objeto e da vigência, bem como dos aditivos deles decorrentes?",
        "classificacao": "Obrigatória",
        "fundamentacao": "Arts. 7º, VI e 8º, §1º, inciso IV, da Lei nº 12.527/2011 – LAI.",
        "palavras_chave": [
            "contratos", "contratações", "contratados", "fornecedores",
            "prestadores serviços", "valores contratos", "vigência contratos"
        ],
        "sinonimos": [
            "ajustes", "acordos comerciais", "instrumentos contratuais",
            "pactos", "compromissos", "obrigações", "vínculos"
        ]
    },
    
    "9.2": {
        "dimensao": "Contratos",
        "id": "9.2",
        "criterio": "Divulga o inteiro teor dos contratos e dos respectivos termos aditivos?",
        "classificacao": "Obrigatória",
        "fundamentacao": "Arts. 7º, VI e 8º, §1º, inciso IV, da Lei nº 12.527/2011 – LAI.",
        "palavras_chave": [
            "inteiro teor", "texto completo", "íntegra contratos",
            "termos aditivos", "aditivos contratuais", "alterações contratuais"
        ],
        "sinonimos": [
            "conteúdo integral", "documentos completos", "versão completa",
            "modificações", "emendas", "revisões", "ajustes", "correções"
        ]
    },
    
    "9.3": {
        "dimensao": "Contratos",
        "id": "9.3",
        "criterio": "Divulga a relação/lista dos fiscais de cada contrato vigente e encerrado?",
        "classificacao": "Obrigatória",
        "fundamentacao": "Arts. 7º, VI e 8º, §1º, inciso IV, da Lei nº 12.527/2011 – LAI.",
        "palavras_chave": [
            "fiscais contratos", "gestores contratos", "responsáveis contratos",
            "fiscalização", "acompanhamento", "supervisão contratos"
        ],
        "sinonimos": [
            "supervisores", "monitores", "controladores", "inspetores",
            "acompanhantes", "verificadores", "observadores", "auditores"
        ]
    },

    # OBRAS
    "10.2": {
        "dimensao": "Obras",
        "id": "10.2",
        "criterio": "Divulga os quantitativos, os preços unitários e totais contratados?",
        "classificacao": "Obrigatória",
        "fundamentacao": "Art. 8º, §1º, V da Lei nº 12.527/2011; art. 94, § 3º, da Lei 14.133/2021.",
        "palavras_chave": [
            "obras", "construções", "reformas", "quantitativos obras",
            "preços unitários", "valores obras", "planilhas orçamentárias"
        ],
        "sinonimos": [
            "edificações", "construções civis", "empreendimentos", "projetos",
            "intervenções", "melhorias", "ampliações", "modernizações"
        ]
    },

    # PLANEJAMENTO E PRESTAÇÃO DE CONTAS
    "11.3": {
        "dimensao": "Planejamento e Prestação de contas",
        "id": "11.3",
        "criterio": "Divulga a íntegra da decisão da apreciação ou julgamento das contas pelo Tribunal de Contas?",
        "classificacao": "Obrigatória",
        "fundamentacao": "Art. 48, caput, da LRF.",
        "palavras_chave": [
            "tribunal de contas", "prestação contas", "julgamento contas",
            "decisões tribunal", "pareceres tribunal", "apreciação contas"
        ],
        "sinonimos": [
            "corte de contas", "órgão fiscalizador", "controle externo",
            "auditoria externa", "verificação contas", "análise contas"
        ]
    },
    
    "11.7": {
        "dimensao": "Planejamento e Prestação de contas",
        "id": "11.7",
        "criterio": "Divulga o plano estratégico institucional?",
        "classificacao": "Recomendada",
        "fundamentacao": "Art. 3º, I-III, combinado com art. 7º, VII, a, combinado com art. 8º, § 1º, V, da Lei 12.527/2011.",
        "palavras_chave": [
            "plano estratégico", "planejamento estratégico", "estratégia institucional",
            "metas institucionais", "objetivos estratégicos", "diretrizes estratégicas"
        ],
        "sinonimos": [
            "plano diretor", "plano institucional", "roadmap", "direcionamento",
            "orientação estratégica", "visão institucional", "missão", "valores"
        ]
    },

    # SERVIÇO DE INFORMAÇÃO AO CIDADÃO - SIC
    "12.1": {
        "dimensao": "Serviço de Informação ao Cidadão - SIC",
        "id": "12.1",
        "criterio": "Existe o SIC no site e indica a unidade/setor responsável?",
        "classificacao": "Obrigatória",
        "fundamentacao": "Arts. 8º, §3º, VII e 9º, I, da Lei nº 12.527/2011 – LAI.",
        "palavras_chave": [
            "SIC", "serviço informação cidadão", "acesso informação",
            "LAI", "lei acesso informação", "informações públicas"
        ],
        "sinonimos": [
            "atendimento cidadão", "central informações", "balcão informações",
            "setor informações", "departamento informações", "núcleo informações"
        ]
    },
    
    "12.2": {
        "dimensao": "Serviço de Informação ao Cidadão - SIC",
        "id": "12.2",
        "criterio": "Indica o endereço físico, o telefone e o e-mail da unidade responsável pelo SIC, além do horário de funcionamento?",
        "classificacao": "Obrigatória",
        "fundamentacao": "Arts. 8º, §1º, I, da Lei nº 12.527/2011 – LAI e art. 6º, VI, b, da Lei nº 13.460/2017.",
        "palavras_chave": [
            "contato SIC", "endereço SIC", "telefone SIC", "email SIC",
            "horário SIC", "localização SIC", "atendimento SIC"
        ],
        "sinonimos": [
            "dados contato", "informações contato", "canais comunicação",
            "formas contato", "meios comunicação", "acesso SIC"
        ]
    },
    
    "12.3": {
        "dimensao": "Serviço de Informação ao Cidadão - SIC",
        "id": "12.3",
        "criterio": "Há possibilidade de envio de pedidos de informação de forma eletrônica (e-SIC)?",
        "classificacao": "Obrigatória",
        "fundamentacao": "Art. 10, §2º, da Lei nº 12.527/2011 – LAI.",
        "palavras_chave": [
            "e-SIC", "eSIC", "pedidos eletrônicos", "solicitações online",
            "formulário eletrônico", "sistema eletrônico", "portal eletrônico"
        ],
        "sinonimos": [
            "sistema digital", "plataforma digital", "canal digital",
            "meio eletrônico", "ferramenta online", "acesso digital"
        ]
    },
    
    "12.4": {
        "dimensao": "Serviço de Informação ao Cidadão - SIC",
        "id": "12.4",
        "criterio": "A solicitação por meio de eSic é simples, ou seja, sem a exigência de itens de identificação do requerente que dificultem ou impossibilitem o acesso à informação?",
        "classificacao": "Obrigatória",
        "fundamentacao": "Art. 10, §1º, da Lei nº 12.527/2011 – LAI.",
        "palavras_chave": [
            "facilidade acesso", "simplicidade", "desburocratização",
            "acesso simplificado", "procedimento simples", "sem complicações"
        ],
        "sinonimos": [
            "acessibilidade", "praticidade", "facilidade", "comodidade",
            "descomplicação", "agilidade", "rapidez", "eficiência"
        ]
    },
    
    "12.5": {
        "dimensao": "Serviço de Informação ao Cidadão - SIC",
        "id": "12.5",
        "criterio": "Divulga nesta seção, instrumento normativo local que regulamente a Lei nº 12.527/2011 – LAI?",
        "classificacao": "Obrigatória",
        "fundamentacao": "Art. 45 da Lei nº 12.527/2011 – LAI.",
        "palavras_chave": [
            "regulamentação LAI", "norma local", "decreto regulamentador",
            "instrumento normativo", "legislação local", "regulamento LAI"
        ],
        "sinonimos": [
            "normatização", "disciplinamento", "ordenamento", "disposições",
            "diretrizes locais", "regramento", "normativa", "regulação"
        ]
    },
    
    "12.6": {
        "dimensao": "Serviço de Informação ao Cidadão - SIC",
        "id": "12.6",
        "criterio": "Divulga, na seção relativa ao e-SIC, os prazos de resposta ao cidadão, incluindo o recursal, e as autoridades competentes para o exame dos pedidos?",
        "classificacao": "Recomendada",
        "fundamentacao": "Art. 7, 15 da Lei nº 12.527/2011 – LAI.",
        "palavras_chave": [
            "prazos resposta", "prazos SIC", "autoridades competentes",
            "recursos SIC", "procedimentos SIC", "tramitação pedidos"
        ],
        "sinonimos": [
            "tempos resposta", "cronogramas", "fluxos", "rotinas",
            "responsáveis", "competências", "atribuições", "instâncias"
        ]
    },
    
    "12.7": {
        "dimensao": "Serviço de Informação ao Cidadão - SIC",
        "id": "12.7",
        "criterio": "Divulga relatório anual estatístico contendo a quantidade de pedidos de acesso recebidos, atendidos, indeferidos, bem como informações genéricas sobre os solicitantes?",
        "classificacao": "Obrigatória",
        "fundamentacao": "Art. 30, inciso III, da Lei nº 12.527/2011 – LAI.",
        "palavras_chave": [
            "relatório estatístico", "estatísticas SIC", "dados SIC",
            "pedidos recebidos", "pedidos atendidos", "pedidos indeferidos"
        ],
        "sinonimos": [
            "levantamento dados", "balanço", "consolidação", "resumo",
            "compilação", "síntese", "demonstrativo", "panorama"
        ]
    },
    
    "12.8": {
        "dimensao": "Serviço de Informação ao Cidadão - SIC",
        "id": "12.8",
        "criterio": "Divulga lista de documentos classificados em cada grau de sigilo, contendo pelo menos o assunto sobre o qual versa a informação?",
        "classificacao": "Obrigatória",
        "fundamentacao": "Art. 30, II, c/c art. 24, §1º) da Lei 12.527/2011.",
        "palavras_chave": [
            "documentos classificados", "sigilo", "informações sigilosas",
            "graus sigilo", "classificação informações", "documentos reservados"
        ],
        "sinonimos": [
            "informações restritas", "dados confidenciais", "material sigiloso",
            "documentos protegidos", "informações sensíveis", "dados reservados"
        ]
    },
    
    "12.9": {
        "dimensao": "Serviço de Informação ao Cidadão - SIC",
        "id": "12.9",
        "criterio": "Divulga lista das informações que tenham sido desclassificadas nos últimos 12 (doze) meses?",
        "classificacao": "Obrigatória",
        "fundamentacao": "Art. 30, I, da Lei 12.527/2011.",
        "palavras_chave": [
            "desclassificação", "informações desclassificadas", "documentos desclassificados",
            "liberação informações", "fim sigilo", "publicização"
        ],
        "sinonimos": [
            "abertura", "disponibilização", "liberação", "divulgação",
            "tornar público", "retirada sigilo", "acesso liberado"
        ]
    },

    # ACESSIBILIDADE
    "13.1": {
        "dimensao": "Acessibilidade",
        "id": "13.1",
        "criterio": "O site oficial e o portal de transparência contêm símbolo de acessibilidade em destaque?",
        "classificacao": "Obrigatória",
        "fundamentacao": "Art. 63, § 1º, da Lei nº 13.146/2015.",
        "palavras_chave": [
            "acessibilidade", "símbolo acessibilidade", "ícone acessibilidade",
            "acesso universal", "inclusão digital", "pessoas deficiência"
        ],
        "sinonimos": [
            "inclusão", "universalização", "democratização", "facilidades",
            "adaptações", "recursos assistivos", "tecnologia assistiva"
        ]
    },
    
    "13.2": {
        "dimensao": "Acessibilidade",
        "id": "13.2",
        "criterio": "O site e o portal de transparência contêm exibição do caminho de páginas percorridas pelo usuário?",
        "classificacao": "Obrigatória",
        "fundamentacao": "Art. 8º, §3º, inciso VIII, da Lei nº 12.527/2011 – LAI e art. 63, caput e § 1º, da Lei nº 13.146/15.",
        "palavras_chave": [
            "breadcrumb", "caminho páginas", "navegação", "trilha navegação",
            "histórico navegação", "localização usuário", "mapa navegação"
        ],
        "sinonimos": [
            "rastro", "percurso", "roteiro", "itinerário",
            "sequência", "trajetória", "rota", "direcionamento"
        ]
    },
    
    "13.3": {
        "dimensao": "Acessibilidade",
        "id": "13.3",
        "criterio": "O site e o portal de transparência contêm opção de alto contraste?",
        "classificacao": "Obrigatória",
        "fundamentacao": "Art. 8º, §3º, VIII, da Lei nº 12.527/2011 - LAI; art. 63, da Lei nº 13.146/2015 e art. 3º, XIX, da Lei nº 14.129/2022.",
        "palavras_chave": [
            "alto contraste", "contraste", "cores", "visualização",
            "acessibilidade visual", "deficiência visual", "baixa visão"
        ],
        "sinonimos": [
            "contraste elevado", "inversão cores", "modo escuro", "tema escuro",
            "facilitação visual", "melhoria visualização", "adaptação visual"
        ]
    },
    
    "13.4": {
        "dimensao": "Acessibilidade",
        "id": "13.4",
        "criterio": "O site e o portal de transparência contêm ferramenta de redimensionamento de texto?",
        "classificacao": "Obrigatória",
        "fundamentacao": "Art. 8º, §3º, VIII, da Lei nº 12.527/2011 – LAI; art. 63, da Lei nº 13.146/2015 e art. 3º, XIX, da Lei nº 14.129/2022.",
        "palavras_chave": [
            "redimensionamento texto", "tamanho fonte", "aumentar texto",
            "diminuir texto", "zoom texto", "ajuste fonte"
        ],
        "sinonimos": [
            "ampliação texto", "redução texto", "modificação fonte",
            "alteração tamanho", "escalabilidade", "flexibilidade visual"
        ]
    },
    
    "13.5": {
        "dimensao": "Acessibilidade",
        "id": "13.5",
        "criterio": "Contém mapa do site institucional?",
        "classificacao": "Recomendada",
        "fundamentacao": "Art. 8º, § 3º, VIII, da Lei nº 12.527/2011 – LAI; art. 63, da Lei nº 13.146/2015 e art. 3º, XIX, da Lei nº 14.129/2022.",
        "palavras_chave": [
            "mapa do site", "sitemap", "estrutura site", "organização site",
            "índice site", "navegação site", "arquitetura informação"
        ],
        "sinonimos": [
            "índice páginas", "estrutura navegação", "organização conteúdo",
            "hierarquia páginas", "esquema site", "layout site"
        ]
    },

    # OUVIDORIAS
    "14.1": {
        "dimensao": "Ouvidorias",
        "id": "14.1",
        "criterio": "Há informações sobre o atendimento presencial pela Ouvidoria (Indicação de endereço físico e telefone, além do horário de funcionamento)?",
        "classificacao": "Obrigatória",
        "fundamentacao": "Arts. 8º, §1º, I, e 9º, da Lei nº 12.527/2011 – LAI c/c arts. 6º, VI, b, 7º, § 2º, VI, e 10, § 4º, da Lei nº 13.460/2017.",
        "palavras_chave": [
            "ouvidoria", "ouvidor", "atendimento presencial", "endereço ouvidoria",
            "telefone ouvidoria", "horário ouvidoria", "contato ouvidoria"
        ],
        "sinonimos": [
            "canal reclamações", "setor reclamações", "atendimento cidadão",
            "mediação conflitos", "resolução problemas", "intermediação"
        ]
    },
    
    "14.2": {
        "dimensao": "Ouvidorias",
        "id": "14.2",
        "criterio": "Há canal eletrônico de acesso/interação com a ouvidoria?",
        "classificacao": "Obrigatória",
        "fundamentacao": "Art. 8º,§3º, VII, Art. 10, §2º, da Lei nº 12.527/2011 – LAI c/c Art. 10, § 4º, da Lei nº 13.460/2017.",
        "palavras_chave": [
            "canal eletrônico", "ouvidoria online", "e-ouvidoria",
            "formulário ouvidoria", "sistema ouvidoria", "plataforma ouvidoria"
        ],
        "sinonimos": [
            "meio digital", "acesso digital", "ferramenta digital",
            "canal virtual", "sistema online", "portal ouvidoria"
        ]
    },
    
    "14.3": {
        "dimensao": "Ouvidorias",
        "id": "14.3",
        "criterio": "Divulga Carta de Serviços ao Usuário?",
        "classificacao": "Obrigatória",
        "fundamentacao": "Art. 7º, §4º, da Lei nº 13.460/2017.",
        "palavras_chave": [
            "carta serviços", "carta usuário", "serviços públicos",
            "compromissos atendimento", "padrões atendimento", "qualidade serviços"
        ],
        "sinonimos": [
            "manual serviços", "guia serviços", "catálogo serviços",
            "relação serviços", "portfólio serviços", "oferta serviços"
        ]
    },

    # LEI GERAL DE PROTEÇÃO DE DADOS (LGPD) E GOVERNO DIGITAL
    "15.1": {
        "dimensao": "Lei Geral de Proteção de Dados (LGPD) e Governo Digital",
        "id": "15.1",
        "criterio": "Identifica o encarregado/responsável pelo tratamento de dados pessoais e disponibiliza Canal de Comunicação (telefone e/ou e-mail)?",
        "classificacao": "Obrigatória",
        "fundamentacao": "Arts. 5º, inciso VIII e 23, inciso III, 41, § 1º da LGPD (Lei 13.709/ 2018) + Art. 3º, incisos XVII, da Lei 14.129/2021.",
        "palavras_chave": [
            "LGPD", "proteção dados", "encarregado dados", "DPO",
            "dados pessoais", "privacidade", "tratamento dados"
        ],
        "sinonimos": [
            "responsável privacidade", "gestor dados", "controlador dados",
            "oficial privacidade", "proteção informações", "segurança dados"
        ]
    },
    
    "15.2": {
        "dimensao": "Lei Geral de Proteção de Dados (LGPD) e Governo Digital",
        "id": "15.2",
        "criterio": "Publica a sua Política de Privacidade e Proteção de Dados?",
        "classificacao": "Recomendada",
        "fundamentacao": "Art. 50, inciso I, da LGPD (Lei 13.709/ 2018); Art. 3º, incisos XVII, da Lei 14.129/2021.",
        "palavras_chave": [
            "política privacidade", "política proteção dados", "termos privacidade",
            "uso dados", "coleta dados", "compartilhamento dados"
        ],
        "sinonimos": [
            "diretrizes privacidade", "normas privacidade", "regras privacidade",
            "procedimentos dados", "tratamento informações", "gestão dados"
        ]
    },
    
    "15.3": {
        "dimensao": "Lei Geral de Proteção de Dados (LGPD) e Governo Digital",
        "id": "15.3",
        "criterio": "Possibilita a demanda e o acesso a serviços públicos por meio digital, sem necessidade de solicitação presencial?",
        "classificacao": "Obrigatória",
        "fundamentacao": "Arts. 3º, incisos II, III e X, e 14 da Lei 14.129/2021.",
        "palavras_chave": [
            "serviços digitais", "governo digital", "atendimento digital",
            "serviços online", "digitalização", "transformação digital"
        ],
        "sinonimos": [
            "e-gov", "governo eletrônico", "administração digital",
            "serviços eletrônicos", "plataforma digital", "portal serviços"
        ]
    },
    
    "15.4": {
        "dimensao": "Lei Geral de Proteção de Dados (LGPD) e Governo Digital",
        "id": "15.4",
        "criterio": "Possibilita o acesso automatizado por sistemas externos em dados abertos (estruturados e legíveis por máquina), e a página contém as regras de utilização?",
        "classificacao": "Obrigatória",
        "fundamentacao": "Art. 8º, §3º, III da Lei nº 12.527/2011 - LAI e Art. 3º, XXV e 24, V da Lei 14.129/2021.",
        "palavras_chave": [
            "dados abertos", "API", "acesso automatizado", "sistemas externos",
            "interoperabilidade", "integração sistemas", "dados estruturados"
        ],
        "sinonimos": [
            "open data", "interface programação", "web services",
            "conectividade", "integração", "compartilhamento dados"
        ]
    },
    
    "15.5": {
        "dimensao": "Lei Geral de Proteção de Dados (LGPD) e Governo Digital",
        "id": "15.5",
        "criterio": "Regulamenta a Lei Federal nº 14.129/2021 (Governo Digital) e divulga a normativa em seu portal?",
        "classificacao": "Recomendada",
        "fundamentacao": "NR Conjunta Atricon nº 02/2022.",
        "palavras_chave": [
            "lei governo digital", "regulamentação digital", "normativa digital",
            "decreto digital", "lei 14.129", "marco legal digital"
        ],
        "sinonimos": [
            "legislação digital", "normas digitais", "regulamento digital",
            "disciplinamento digital", "ordenamento digital", "diretrizes digitais"
        ]
    },
    
    "15.6": {
        "dimensao": "Lei Geral de Proteção de Dados (LGPD) e Governo Digital",
        "id": "15.6",
        "criterio": "Realiza e divulga resultados de pesquisas de satisfação?",
        "classificacao": "Obrigatória",
        "fundamentacao": "Art. 23, § 1º e 2º, da Lei nº 13.460/2017 c/c Art. 3º, inciso IV, e 24, inciso II, da Lei 14.129/2021.",
        "palavras_chave": [
            "pesquisa satisfação", "avaliação serviços", "satisfação usuário",
            "qualidade atendimento", "feedback", "opinião usuário"
        ],
        "sinonimos": [
            "enquete", "questionário", "sondagem", "levantamento",
            "consulta pública", "avaliação qualidade", "medição satisfação"
        ]
    }
}

# Função auxiliar para buscar critérios por palavras-chave
def buscar_criterios_por_palavra_chave(palavra_busca):
    """
    Busca critérios que contenham a palavra-chave especificada
    
    Args:
        palavra_busca (str): Palavra ou termo a ser buscado
        
    Returns:
        list: Lista de critérios que contêm a palavra-chave
    """
    palavra_busca = palavra_busca.lower()
    criterios_encontrados = []
    
    for id_criterio, dados in CRITERIOS_TRANSPARENCIA.items():
        # Busca nas palavras-chave
        for palavra in dados['palavras_chave']:
            if palavra_busca in palavra.lower():
                criterios_encontrados.append({
                    'id': id_criterio,
                    'criterio': dados['criterio'],
                    'dimensao': dados['dimensao'],
                    'classificacao': dados['classificacao']
                })
                break
        
        # Busca nos sinônimos se não encontrou nas palavras-chave
        if not any(criterio['id'] == id_criterio for criterio in criterios_encontrados):
            for sinonimo in dados['sinonimos']:
                if palavra_busca in sinonimo.lower():
                    criterios_encontrados.append({
                        'id': id_criterio,
                        'criterio': dados['criterio'],
                        'dimensao': dados['dimensao'],
                        'classificacao': dados['classificacao']
                    })
                    break
    
    return criterios_encontrados

# Função para obter todas as palavras-chave de um critério específico
def obter_palavras_chave_criterio(id_criterio):
    """
    Obtém todas as palavras-chave e sinônimos de um critério específico
    
    Args:
        id_criterio (str): ID do critério (ex: "1.1", "2.3")
        
    Returns:
        dict: Dicionário com palavras-chave e sinônimos do critério
    """
    if id_criterio in CRITERIOS_TRANSPARENCIA:
        criterio = CRITERIOS_TRANSPARENCIA[id_criterio]
        return {
            'palavras_chave': criterio['palavras_chave'],
            'sinonimos': criterio['sinonimos'],
            'todas_palavras': criterio['palavras_chave'] + criterio['sinonimos']
        }
    return None

# Função para listar critérios por dimensão
def listar_criterios_por_dimensao(dimensao):
    """
    Lista todos os critérios de uma dimensão específica
    
    Args:
        dimensao (str): Nome da dimensão
        
    Returns:
        list: Lista de critérios da dimensão especificada
    """
    criterios_dimensao = []
    
    for id_criterio, dados in CRITERIOS_TRANSPARENCIA.items():
        if dados['dimensao'].lower() == dimensao.lower():
            criterios_dimensao.append({
                'id': id_criterio,
                'criterio': dados['criterio'],
                'classificacao': dados['classificacao'],
                'fundamentacao': dados['fundamentacao']
            })
    
    return criterios_dimensao

# Função para obter estatísticas dos critérios
def obter_estatisticas_criterios():
    """
    Obtém estatísticas gerais dos critérios mapeados
    
    Returns:
        dict: Estatísticas dos critérios
    """
    total_criterios = len(CRITERIOS_TRANSPARENCIA)
    
    # Contagem por classificação
    classificacoes = {}
    dimensoes = {}
    
    for dados in CRITERIOS_TRANSPARENCIA.values():
        # Contagem por classificação
        classificacao = dados['classificacao']
        classificacoes[classificacao] = classificacoes.get(classificacao, 0) + 1
        
        # Contagem por dimensão
        dimensao = dados['dimensao']
        dimensoes[dimensao] = dimensoes.get(dimensao, 0) + 1
    
    return {
        'total_criterios': total_criterios,
        'por_classificacao': classificacoes,
        'por_dimensao': dimensoes,
        'dimensoes_disponiveis': list(dimensoes.keys())
    }

# Constantes para facilitar o uso
DIMENSOES_DISPONIVEIS = [
    "Informações Prioritárias",
    "Informações Institucionais", 
    "Convênios e Transferências",
    "Recursos Humanos",
    "Diárias",
    "Licitações",
    "Contratos",
    "Obras",
    "Planejamento e Prestação de contas",
    "Serviço de Informação ao Cidadão - SIC",
    "Acessibilidade",
    "Ouvidorias",
    "Lei Geral de Proteção de Dados (LGPD) e Governo Digital"
]

CLASSIFICACOES_DISPONIVEIS = [
    "Essencial",
    "Obrigatória", 
    "Recomendada"
]

# Exemplo de uso das funções
if __name__ == "__main__":
    # Exemplo 1: Buscar critérios relacionados a "transparência"
    print("=== Critérios relacionados a 'transparência' ===")
    resultados = buscar_criterios_por_palavra_chave("transparência")
    for resultado in resultados[:3]:  # Mostra apenas os 3 primeiros
        print(f"ID: {resultado['id']} - {resultado['criterio']}")
    
    # Exemplo 2: Obter palavras-chave de um critério específico
    print("\n=== Palavras-chave do critério 1.1 ===")
    palavras = obter_palavras_chave_criterio("1.1")
    if palavras:
        print("Palavras-chave:", palavras['palavras_chave'][:3])
        print("Sinônimos:", palavras['sinonimos'][:3])
    
    # Exemplo 3: Estatísticas gerais
    print("\n=== Estatísticas Gerais ===")
    stats = obter_estatisticas_criterios()
    print(f"Total de critérios: {stats['total_criterios']}")
    print(f"Por classificação: {stats['por_classificacao']}")
    print(f"Total de dimensões: {len(stats['dimensoes_disponiveis'])}")