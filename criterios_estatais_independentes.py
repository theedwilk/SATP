# criterios_estatais_independentes.py
# Critérios específicos para Estatais Independentes
# Aplicável aos órgãos classificados como "Estatais Independentes"

CRITERIOS_ESTATAIS_INDEPENDENTES = {
    # ===== PLANEJAMENTO E PRESTAÇÃO DE CONTAS =====
    "11.14": {
        "dimensao": "Planejamento e Prestação de contas",
        "id": "11.14",
        "criterio": "Pública o Orçamento de Investimentos da instituição que compõe a Lei Orçamentária Anual?",
        "classificacao": "Obrigatória",
        "fundamentacao": "Art. 3º combinado com art. 6º, I, combinado com art. 7º, II, VI e VII, combinado com art. 8º, caput e § 1º, III e V, e § 2º da Lei 12.527/2011 (LAI); Art. 7º, § 3º, II-IV, do Decreto 7.724/2012;",
        "palavras_chave": [
            "orçamento investimentos", "lei orçamentária anual", "LOA", "investimentos",
            "orçamento público", "planejamento orçamentário", "recursos investimentos"
        ],
        "sinonimos": [
            "plano investimentos", "programa investimentos", "dotação investimentos",
            "previsão investimentos", "alocação recursos", "destinação recursos"
        ]
    }
}

# Funções auxiliares para Estatais Independentes
def obter_criterios_estatais_independentes():
    """
    Obtém todos os critérios aplicáveis às Estatais Independentes
    
    Returns:
        dict: Dicionário com todos os critérios aplicáveis
    """
    from criterios_comum import CRITERIOS_TRANSPARENCIA
    
    criterios_aplicaveis = {}
    
    # Adiciona critérios comuns a todos
    criterios_aplicaveis.update(CRITERIOS_TRANSPARENCIA)
    
    # Adiciona critérios específicos de estatais independentes
    criterios_aplicaveis.update(CRITERIOS_ESTATAIS_INDEPENDENTES)
    
    return criterios_aplicaveis

# Constantes específicas para Estatais Independentes
DIMENSOES_ESTATAIS_INDEPENDENTES = [
    "Planejamento e Prestação de contas"
]

CRITERIOS_OBRIGATORIOS_ESTATAIS_INDEPENDENTES = [
    "11.14"
]

CRITERIOS_RECOMENDADOS_ESTATAIS_INDEPENDENTES = []

# Exemplo de uso
if __name__ == "__main__":
    print("=== Critérios Específicos de Estatais Independentes ===")
    
    # Lista critérios específicos
    for id_criterio, dados in CRITERIOS_ESTATAIS_INDEPENDENTES.items():
        print(f"ID: {id_criterio} - {dados['classificacao']}")
        print(f"Critério: {dados['criterio']}")
        print(f"Palavras-chave: {', '.join(dados['palavras_chave'])}")
        print("-" * 50)
    
    # Estatísticas
    total_criterios = len(CRITERIOS_ESTATAIS_INDEPENDENTES)
    obrigatorios = len([c for c in CRITERIOS_ESTATAIS_INDEPENDENTES.values() 
                       if c['classificacao'] == 'Obrigatória'])
    recomendados = len([c for c in CRITERIOS_ESTATAIS_INDEPENDENTES.values() 
                       if c['classificacao'] == 'Recomendada'])
    
    print(f"\n=== Estatísticas Estatais Independentes ===")
    print(f"Total de critérios específicos: {total_criterios}")
    print(f"Obrigatórios: {obrigatorios}")
    print(f"Recomendados: {recomendados}")