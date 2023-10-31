"""
Exercício: Gerenciamento de Estoque

Contexto: Você trabalha no controle de estoque de uma empresa de 
eletrônicos. A empresa vende dois produtos populares: smartphones e smartwatches. 

Diariamente, você precisa calcular o total de produtos vendidos, identificar 
qual produto foi mais vendido e reorganizar os números caso haja algum erro nas entradas.

Instruções:

    1. Retornando múltiplos valores de uma função usando tuplas.
        - Crie uma função chamada resumo_vendas que aceite 
        dois argumentos: vendas_smartphones e vendas_smartwatches.
        
        - A função deve retornar o total de vendas e o nome do produto 
        mais vendido (seja "smartphone" ou "smartwatch").
        
        - Exemplo de entrada: 80 smartphones vendidos e 70 smartwatches vendidos.
        - Pergunta: Qual é o total de vendas e qual produto foi mais vendido?

    2. Uso de tuplas em loops for.
        - Dada a lista vendas_semana = [(70, 65), (80, 82), (90, 88)], onde 
        cada tupla representa as vendas de smartphones e smartwatches em um dia, respectivamente.
        
        - Use um loop for para imprimir as vendas de smartphones e smartwatches para cada dia.
        - Pergunta: Quais foram as vendas de smartphones e smartwatches para cada dia?

    3. Trocando valores entre duas variáveis.
        - Suponha que você cometeu um erro e registrou as vendas de segunda-feira 
        de forma invertida: vendas_segunda = (65, 70), onde o primeiro valor é para 
        smartwatches e o segundo para smartphones.
        
        - Corrija essa entrada invertendo os valores.
        - Pergunta: Qual é a entrada corrigida para as vendas de segunda-feira?

Nota: Este exercício visa ajudar a compreenderem a versatilidade e aplicabilidade 
das tuplas em diferentes cenários de programação. 

Ao final, você será capaz de usar tuplas para múltiplas finalidades e manipular dados de forma eficiente.
"""
def resume_de_venda (vendas_smartphones, vendas_smartwatches ):
    total_vendas = vendas_smartphones + vendas_smartphones

    produto_mais_vendido = 'smartphone vendeu mais' if vendas_smartphones > vendas_smartwatches else 'smartwatch vendeu mais'
    return total_vendas, produto_mais_vendido
total, vendidos = resume_de_venda(80,70)

print(f'Total de Vendas de ambos {total}')

print(f'mais vendido {vendidos}')
print()
vendas_semana = [(70, 65), (80, 82), (90, 88)]

for venda_A, vendas_b in vendas_semana:

    print(f'Vendas A {venda_A} e vendas B {vendas_b}')
print()    

vendas_segunda = (65, 70)
vendas_A = 65
vendas_B = 70

venda1, venda2 = vendas_B, vendas_A

print(f'Vendas A {venda1}, Venda B {venda2}')