"""
Exercício: Filtrando e Transformando Dados com Lambda

Objetivo: Familiarizar-se com o uso de funções lambda 
juntamente com funções built-in como filter e map.

Instruções:

    1. Dada uma lista de números: numeros = [2, 5, 8, 10, 12, 15, 18, 20, 23, 25, 28].
    
    2. Use a função filter() e uma função lambda para criar uma nova 
    lista que contém apenas os números ímpares da lista original.
    
    3. Em seguida, use a função map() e uma função lambda para 
    criar uma nova lista que contém o quadrado de cada número da lista de números ímpares.
    
    4. Imprima ambas as listas.
    
    Dicas:

    Use filter() para filtrar itens de uma lista.
    Use map() para aplicar uma função a cada item de uma lista.
"""

# Lista inicial de números
numeros = [2, 5, 8, 10, 12, 15, 18, 20, 23, 25, 28]

numeros_impar = list(filter(lambda x: x % 2 == 1, numeros ))


print(numeros_impar)

numeros_ao_quadrado = list(map(lambda x: x**2, numeros_impar))

print(numeros_ao_quadrado)