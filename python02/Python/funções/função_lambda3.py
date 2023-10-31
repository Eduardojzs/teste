#função lambda com filter

"""
Filtramos uma lista para obter apenas números pares 
usando a função filter() junto com uma função lambda.

Problema:
Dada uma lista de números, filtre-a para obter apenas os números pares.
"""

# Lista original de números
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Usando filter() e lambda para obter apenas números pares
numeros_pares = list(filter(lambda x: x % 2 == 0, numeros))

"""
    list(): A função list() é usada para converter um iterável em uma lista. No 
    contexto desta linha, ela está sendo usada para converter o iterador resultante 
    da função filter() de volta em uma lista.

    filter(): A função filter() é uma função built-in do Python que filtra os itens 
    de um iterável (como uma lista) com base em uma função fornecida. Ela retorna um 
    iterador, razão pela qual usamos list() para converter de volta em uma lista.

    lambda x: x % 2 == 0: Esta é uma função lambda. É uma pequena função anônima que pode \
    ter qualquer número de argumentos, mas só pode ter uma expressão. Esta expressão 
    específica retorna True se x for par e False caso contrário.
    
        x % 2 retorna o resto da divisão de x por 2.
        x % 2 == 0 verifica se esse resto é zero (o que indica que x é um número par).

    numeros: É a lista original de números que você deseja filtrar.

Então, quando você combina tudo, esta linha de código está dizendo:

    "Quero filtrar a lista numeros."
    "Para cada número na lista, quero verificar se ele é par."
    "Se for par, inclua-o no resultado."
    "Finalmente, converta o resultado filtrado de volta em uma lista e armazene-o na variável numeros_pares."

Assim, numeros_pares acabará sendo uma lista contendo apenas os números pares da lista original numeros.
"""

print(numeros_pares)  # Saída: [2, 4, 6, 8, 10]

"""
Explicação:
A função lambda lambda x: x % 2 == 0 verifica se um número 
é par (ou seja, se ele é divisível por 2 sem deixar um resto). A função filter() então 
aplica essa função lambda a cada item da lista numeros. Os itens que retornam True são mantidos 
no resultado, que no final são os números pares.
"""