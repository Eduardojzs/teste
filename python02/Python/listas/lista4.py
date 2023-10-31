"""
Métodos de Listas
        sort(): ordena a lista in-place.
        reverse(): inverte a ordem dos elementos in-place.
        count(): conta o número de ocorrências de um elemento.
        index(): retorna o índice da primeira ocorrência de um elemento.
"""

#Métodos de Listas

#Suponhamos que temos uma lista de números e uma lista de frutas:
numeros = [23, 1, 45, 6, 12]
frutas = ["banana", "maçã", "banana", "cereja", "maçã", "damasco"]

#1. sort(): ordena a lista in-place

#O método sort() ordena os itens da lista em uma ordem crescente por 
#padrão. Para números, isso é uma ordem numérica e para strings, é uma ordem alfabética.
print(numeros)
numeros.sort()
print(numeros)  # Saída: [1, 6, 12, 23, 45]

print()

print(frutas)
frutas.sort()
print(frutas)  # Saída: ['banana', 'banana', 'cereja', 'damasco', 'maçã', 'maçã']

print()

#Para ordenar em ordem decrescente, podemos usar o argumento reverse=True:
numeros.sort(reverse=True)
print(numeros)  # Saída: [45, 23, 12, 6, 1]

#2. reverse(): inverte a ordem dos elementos in-place.

print("\n-------------\n")

#O método reverse() simplesmente inverte a ordem dos elementos da lista.
numeros.reverse()
print(numeros)  # Saída: [1, 6, 12, 23, 45] (supondo que estivesse em ordem decrescente antes de chamarmos reverse())

frutas.reverse()
print(frutas)  # Saída: ['maçã', 'maçã', 'damasco', 'cereja', 'banana', 'banana']

#3. count(): conta o número de ocorrências de um elemento.

#O método count() retorna o número de vezes que um elemento aparece na lista.
ocorrencias_banana = frutas.count("banana")
print(ocorrencias_banana) # Saída 2

ocorrencias_numero_6 = numeros.count(6)
print(ocorrencias_numero_6) #Saída 1

#4. index(): retorna o índice da primeira ocorrência de um elemento.

#O método index() retorna o índice da primeira ocorrência do elemento 
#especificado. Se o elemento não estiver presente, ele gerará um erro.
indice_banana = frutas.index("banana")
print(indice_banana)  # Saída: 4 (pois nós invertemos a lista anteriormente com reverse())

indice_23 = numeros.index(23)
print(indice_23) #Saída: 3

"""
Esses são os métodos fundamentais das listas em Python e seus usos 
práticos. Ao trabalhar com listas, é útil estar familiarizado(a) com esses 
métodos, pois eles são frequentemente empregados para manipulação e análise de dados.
"""