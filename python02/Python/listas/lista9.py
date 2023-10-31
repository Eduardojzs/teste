"""
Exercício: List Comprehensions

Objetivo: Familiarizar-se com a criação de listas usando a notação 
concisa de "List Comprehensions" em Python.

Instruções:

    1. Use uma list comprehension para criar uma lista dos dez primeiros 
    números elevados ao cubo e imprima o resultado.

    2. Use uma list comprehension para criar uma lista contendo todos os números 
    de 1 a 20 que são divisíveis por 3. Imprima o resultado.

    3. Dada a lista de palavras frutas = ["maçã", "banana", "manga", "uva", "abacaxi", "laranja"], 
    use uma list comprehension para criar uma lista com as frutas que possuem mais de 5 caracteres. 
    Imprima o resultado.

    4. Dada a lista notas = [89, 92, 56, 78, 45, 34, 90, 99, 65, 76, 80, 82], use 
    uma list comprehension para obter todas as notas acima de 75 e imprima o resultado.
"""
cubo = [ x**3 for x in range(10)]

print(cubo)

divisíveis_por3 = [ x for x in range(1, 21) if x % 3 == 0]

print(divisíveis_por3)

frutas = ["maçã", "banana", "manga", "uva", "abacaxi", "laranja"]


frutas_longas = [frutas for frutas in frutas if len(frutas) > 5]

print(frutas_longas)

notas = [89, 92, 56, 78, 45, 34, 90, 99, 65, 76, 80, 82]

notas_acima_de75 = []

for notas in notas:

    if notas > 75:

            notas_acima_de75.append(notas)
            notas_acima_de75.sort()
print(notas_acima_de75)            