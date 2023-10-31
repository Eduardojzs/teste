"""
Exercício: Classificação de Números

Seu desafio é escrever um programa que faça o seguinte:

    Peça ao usuário para inserir 5 números inteiros, um por um.
    Armazene esses números em uma lista.
    Classifique os números na lista em ordem crescente.
    Imprima a lista classificada.

Requisitos:

    Utilize um loop (como um for ou while) para coletar os números do usuário.
    Utilize o método append da lista para adicionar cada número à lista.
    Utilize o método sort da lista para classificar os números.

Dicas:

    Você pode utilizar um loop for com range(5) para repetir um bloco de 
    código 5 vezes, uma vez para cada número a ser inserido.

Exemplo de Saída:

Digite um número: 4
Digite um número: 2
Digite um número: 5
Digite um número: 1
Digite um número: 3
Números em ordem crescente: [1, 2, 3, 4, 5]
"""

# Inicializa uma lista vazia para armazenar os números
numeros = []

# Usa um loop for para repetir o bloco de código 5 vezes
for i in range(5):
    
    # Pede ao usuário para inserir um número
    numero = int(input("Digite um número: "))
    
    # Adiciona o número inserido pelo usuário à lista de números
    numeros.append(numero)

# Classifica os números na lista em ordem crescente
numeros.sort()

# Imprime a lista classificada
print("Números em ordem crescente:", numeros)