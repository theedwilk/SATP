# criterios_comum_exceto_estatais_independentes.py
# Critérios aplicáveis a todos os poderes EXCETO Estatais Independentes

CRITERIOS_COMUM_EXCETO_ESTATAIS_INDEPENDENTES = {
    # RECEITA
    "3.1": {
        "dimensao": "Receita",
        "id": "3.1",
        "criterio": "Divulga as receitas do Poder ou órgão, evidenciando sua previsão e realização?",
        "classificacao": "Essencial",
        "fundamentacao": "Arts. 48, §1º, II e 48-A, inciso II, da LC nº 101/00 e art. 8º, II, do Decreto nº 10.540/20.",
        "palavras_chave": [
            "receitas", "arrecadação", "previsão receita", "realização receita",
            "entrada recursos", "recursos financeiros", "orçamento receita"
        ],
        "sinonimos": [
            "ingressos", "entradas", "recursos", "valores recebidos",
            "captação recursos", "angariação", "obtenção recursos"
        ]
    },

    # DESPESA
    "4.1": {
        "dimensao": "Despesa",
        "id": "4.1",
        "criterio": "Divulga o total das despesas empenhadas, liquidadas e pagas?",
        "classificacao": "Essencial",
        "fundamentacao": "Arts. 7º, VI e 8º, §1º, inciso III, da Lei nº 12.527/2011 - LAI; arts. 48, §1º, inciso II e 48-A, inciso I, da LC nº 101/20; art. 8º, inciso I, do Decreto nº 10.540/20.",
        "palavras_chave": [
            "despesas", "gastos", "empenhadas", "liquidadas", "pagas",
            "execução orçamentária", "despesa pública", "dispêndios"
        ],
        "sinonimos": [
            "custos", "saídas", "desembolsos", "pagamentos", "egresos",
            "aplicação recursos", "utilização recursos", "consumo recursos"
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
            "categorização", "tipificação", "organização despesas",
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
            "empenhos", "beneficiários", "credores", "fornecedores",
            "bens fornecidos", "serviços prestados", "procedimento licitatório"
        ],
        "sinonimos": [
            "compromissos", "obrigações", "contratados", "prestadores",
            "produtos", "atividades", "processo licitação"
        ]
    }
}