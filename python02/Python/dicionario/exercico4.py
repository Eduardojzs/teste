"""
Exercício sobre Iterando Sobre Dicionários

Objetivo: Você tem um dicionário que representa o número de livros vendidos 
em uma livraria em diferentes meses. Sua tarefa é iterar sobre esse dicionário 
para realizar diferentes análises.

Dicionário fornecido:

vendas = {
    "Janeiro": 120,
    "Fevereiro": 150,
    "Março": 80,
    "Abril": 190,
    "Maio": 210
}

Instruções:

    1. Iterando sobre as chaves (meses):
        - Imprima todos os meses em que a livraria registrou vendas.

    2. Iterando apenas sobre os valores (número de livros vendidos):
        - Calcule e imprima a venda total nos 5 meses.
        - Determine e imprima o mês com as vendas mais baixas.

    3. Iterando sobre chaves e valores simultaneamente (itens):
        - Para cada mês, imprima uma mensagem no seguinte 
        formato: "Em [mês], [número] livros foram vendidos".
        
"""

# Definindo um dicionário 'vendas' para armazenar as vendas mensais
vendas = {
    "Janeiro": 120,    # Vendas de Janeiro
    "Fevereiro": 150,  # Vendas de Fevereiro
    "Março": 80,       # Vendas de Março
    "Abril": 190,      # Vendas de Abril
    "Maio": 210        # Vendas de Maio
}


# 1. Iterando sobre chaves

# Imprime um cabeçalho informativo para a seção de saída
print("Meses de vendas registradas:")

# Itera através das chaves do dicionário 'vendas' (que são os meses)
for mes in vendas:
    
    # Imprime o nome do mês
    print(mes)


# 2. Iterando sobre valores

#- Calcule e imprima a venda total nos 5 meses.
#- Determine e imprima o mês com as vendas mais baixas.

print("\n2. Iterando sobre valores")

total_vendas = 0
vendas_mais_baixas = float('inf')

mes_vendas_mais_baixas = ""

# Para cada 'venda' dentro dos valores do dicionário 'vendas'
for venda in vendas.values():
    
    # Adiciona o valor da venda atual ao total de vendas
    total_vendas += venda
    
    # Verifica se a venda atual é menor do que o valor armazenado em 'vendas_mais_baixas'
    if venda < vendas_mais_baixas:
        
        # Se for, atualiza 'vendas_mais_baixas' com o valor da venda atual
        vendas_mais_baixas = venda

# Para cada par 'mes' e 'venda' no dicionário 'vendas'
for mes, venda in vendas.items():
    
    # Verifica se a venda atual é igual ao valor mais baixo registrado
    if venda == vendas_mais_baixas:
        
        # Se for, armazena o mês correspondente em 'mes_vendas_mais_baixas'
        mes_vendas_mais_baixas = mes
        
        # Encerra o loop (não precisa continuar a busca)
        break


print("\nTotal de livros vendidos:", total_vendas)
print(f"Mês com as vendas mais baixas: {mes_vendas_mais_baixas} com {vendas_mais_baixas} livros vendidos.") 


# 3. Iterando sobre chaves e valores simultaneamente
print("\n3. Iterando sobre chaves e valores simultaneamente")
print("\nResumo das vendas:")

# Para cada par 'mes' e 'venda' no dicionário 'vendas'
for mes, venda in vendas.items():
    
    # Imprime uma mensagem formatada com o mês e a quantidade de livros vendidos
    print(f"Em {mes}, {venda} livros foram vendidos.")