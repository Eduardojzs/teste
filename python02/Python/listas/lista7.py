"""
Exercício: Slicing de Listas

Objetivo: Familiarizar-se com o conceito de "slicing" em listas, acessando 
subconjuntos de listas e utilizando passos para selecionar elementos específicos.

Instruções:

    1. Crie uma lista chamada cores com os seguintes 
    elementos: "vermelho", "verde", "azul", "amarelo", "laranja", "roxo", "marrom", "cinza".

    2. Acesse e imprima as cores "verde" e "azul" usando slicing.

    3. Imprima as duas primeiras cores da lista utilizando slicing.

    4. Imprima todas as cores a partir da cor "amarelo" usando slicing.

    5. Imprima todas as cores em posições ímpares na 
    lista (ou seja, "vermelho", "azul", "laranja", "marrom") usando slicing com passos.

    6. Inverta a ordem das cores na lista usando slicing e imprima o resultado.
"""

#Solução:

#1. Crie uma lista chamada cores com os seguintes 
#elementos: "vermelho", "verde", "azul", "amarelo", "laranja", "roxo", "marrom", "cinza".
cores = ["vermelho", "verde", "azul", "amarelo", "laranja", "roxo", "marrom", "cinza"]
print(f"Lista de cores: {cores}")

#2. Acesse e imprima as cores "verde" e "azul" usando slicing.
subconjunto = cores[1:3]

print(f"Cores entre verde e azul: {subconjunto}")

#3. Imprima as duas primeiras cores da lista utilizando slicing.
primeiras = cores[:2]

print(f"As duas primeiras cores são: {primeiras}")

#4. Imprima todas as cores a partir da cor "amarelo" usando slicing.
a_partir_amarelo = cores[3:]

print(f"Cores a partir do amarelo: {a_partir_amarelo}")

#5. Imprima todas as cores em posições ímpares na 
#lista (ou seja, "vermelho", "azul", "laranja", "marrom") usando slicing com passos.

cores_impares = cores[::2]

print(f"Cores em posição impares: {cores_impares}")

#6. Inverta a ordem das cores na lista usando slicing e imprima o resultado.

inverso = cores[::-1]
print(f"Cores na ordem inversa: {inverso}")




