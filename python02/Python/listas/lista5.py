"""
Exercício: Métodos de Listas

Objetivo: Aprofundar a compreensão sobre os métodos específicos das listas em Python.

Instruções:

    1. Crie uma lista chamada números contendo os 
    valores: 23, 11, 89, 34, 11, 56, 78, 90, 23, 45.

    2. Ordene a lista em ordem crescente usando o 
    método sort() e imprima o resultado.

    3. Use o método reverse() para inverter a ordem dos elementos 
    da lista e imprima o resultado.

    4. Conte quantas vezes o número 11 aparece na lista usando o 
    método count() e imprima o resultado.

    5. Encontre o índice da primeira ocorrência do número 78 usando o 
    método index() e imprima o resultado.

    6. Tente encontrar o índice de um número que não está na 
    lista (por exemplo, 100) e capture a exceção usando um 
    bloco try-except para exibir uma mensagem amigável.
"""
numeros = [23, 11, 89, 34, 11, 56, 78, 90, 23, 45]
print(numeros)
numeros.sort()
print(numeros)
numeros.reverse()
print(numeros)
numeros_contado11 = numeros.count(11)

print(f'numeros 11 apareceu {numeros_contado11}')
index_78 = numeros.index(78)
print(f'Numéro 78 apareceu no index {index_78}')



try:
    
    indice_nao_existente = numeros.index(100)
    
    print(indice_nao_existente)
    
except ValueError:
    
    print("O número 100 não está na lista.")
    
