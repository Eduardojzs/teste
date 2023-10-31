
#Função lambda com map
"""
Vamos a um exemplo em que utilizaremos a função map() com uma 
função lambda para transformar uma lista de números, elevando cada número ao quadrado.

Problema:
Dada uma lista de números, retorne uma nova lista onde cada número é elevado ao quadrado.
"""

# Lista original de números
numeros = [1, 2, 3, 4, 5]

# Usando map() e lambda para elevar cada número ao quadrado
numeros_ao_quadrado = list(map(lambda x: x**2, numeros))

"""
    lambda x: x2:
        Uma função lambda é uma pequena função anônima.
        A função lambda pode ter qualquer número de argumentos, mas só pode ter uma expressão.
        Aqui, a expressão lambda x: x**2 define uma função que aceita um argumento x e retorna x ao quadrado.

    map():
        A função map() aplica uma função a todos os itens de um objeto de entrada (como uma lista ou tupla).
        No caso acima, map() aplica a função lambda definida anteriormente a cada item da lista numeros.

    list():
        A função list() converte o resultado de map() em uma lista. Isso é necessário porque 
        a função map() retorna um objeto iterável de tipo map, e se você deseja uma lista como 
        saída, você deve convertê-lo em uma lista.

    Então, se você tiver a lista numeros = [1, 2, 3, 4, 5]:

    A função map() aplica a função lambda a cada elemento da lista, resultando nos quadrados 
    de cada número: 1, 4, 9, 16 e 25.

    Finalmente, a função list() converte esses resultados em uma lista, dando o resultado final 
    para numeros_ao_quadrado como [1, 4, 9, 16, 25].
"""

print(numeros_ao_quadrado)  # Saída: [1, 4, 9, 16, 25]


"""
Explicação:

A função lambda lambda x: x**2 pega cada número x e retorna seu 
quadrado. A função map() aplica essa função lambda a cada item da lista 
numeros. 

O resultado é um iterador com os números elevados ao quadrado, então 
usamos list() para convertê-lo de volta em uma lista.
"""

"""
Vamos criar um exemplo onde usaremos a função map() juntamente 
com uma função lambda para transformar uma lista de palavras em uma lista 
que contém o comprimento de cada palavra.

Problema:

Dada uma lista de palavras, retorne uma nova lista contendo o 
comprimento de cada palavra.
"""

# Lista original de palavras
palavras = ["maça", "banana", "arroz", "abacate"]

# Usando map() e lambda para obter o comprimento de cada palavra
comprimentos = list(map(lambda palavra: len(palavra), palavras))

"""
    list(): Esta função é utilizada para converter um iterável (como o resultado 
    do map()) em uma lista. A função map(), por padrão, retorna um iterador, e ao envolvê-lo 
    com list(), estamos convertendo esse iterador em uma lista real.

    map(): A função map() é uma função built-in do Python que aplica uma função a 
    todos os itens em um iterável (neste caso, a lista palavras). A ideia principal 
    aqui é transformar cada item da lista original (cada palavra) em um novo 
    valor (neste caso, o comprimento de cada palavra).

    lambda palavra: len(palavra): Isso é uma função lambda (uma função anônima de uma única linha).

        palavra: É a variável que recebe cada item da lista palavras um de cada vez.

        len(palavra): Esta parte da função lambda retorna o comprimento da palavra 
        atual. len() é uma função built-in do Python que retorna o número de itens em um 
        objeto, neste contexto, o número de caracteres em uma string.

    palavras: Este é o iterável original (a lista de palavras) que você deseja transformar.

Quando você combina tudo, o que esta linha faz é:

    Para cada palavra na lista palavras, obtenha o comprimento dessa palavra.
    Crie uma nova lista, comprimentos, contendo os comprimentos de todas as palavras da lista original.

Então, se a lista palavras contém ["maça", "banana"], a lista resultante 
comprimentos será [4, 6], porque "arroz" tem 5 letras e "abacate" tem 7 letras.
"""
