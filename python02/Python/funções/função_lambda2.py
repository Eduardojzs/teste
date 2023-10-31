"""
    Nomeação

Sem atribuir a função lambda a uma variável, ela permanece anônima. 
Você pode usá-la, por exemplo, em funções como sorted:

Ordenar uma lista de strings pelo comprimento usando função lambda:
"""

#Função lambda com sorted

"""
Exemplo com sorted:

Suponha que você tenha uma lista de tuplas representando 
pessoas e suas idades, e você queira classificá-las pela idade:
"""

pessoas = [("João", 35), ("Maria", 25), ("Pedro", 40)]
pessoas_ordenadas = sorted(pessoas, key=lambda x: x[1])

print(pessoas_ordenadas)  # Saída: [('Maria', 25), ('João', 35), ('Pedro', 40)]

#No exemplo acima, estamos usando a função lambda 
#para especificar que queremos ordenar as tuplas pela idade (índice 1).

"""
    sorted(): É uma função built-in do Python que retorna uma nova 
    lista contendo todos os itens da lista original em ordem crescente.
    
    Uma função built-in é uma função que já vem incluída no 
    núcleo do Python, de modo que você não precisa importar nenhum módulo ou 
    pacote adicional para usá-la. Essas funções estão sempre disponíveis no namespace 
    principal e ajudam a realizar tarefas comuns sem a necessidade de escrever código extra.

    pessoas: É a lista que você deseja ordenar. No exemplo fornecido, 
    pessoas é uma lista de tuplas onde cada tupla contém um nome e uma idade.

    key: É um argumento opcional que você pode passar para a função 
    sorted(). Ele espera uma função que pode aceitar um item da 
    lista (neste caso, uma tupla) e retornar um valor que será usado 
    para ordenar a lista.

    lambda x: x[1]: Esta é uma função lambda que aceita uma 
    tupla x e retorna o segundo item da tupla (ou seja, x[1]). Neste 
    contexto, isso significa que estamos pegando a idade de cada 
    tupla. A função sorted() usará essas idades para ordenar a lista de tuplas.

Então, quando você escreve pessoas_ordenadas = sorted(pessoas, key=lambda x: x[1]), você está dizendo:

    "Eu quero ordenar a lista pessoas."
    
    "Para determinar a ordem, para cada tupla em pessoas, pegue o segundo 
    item da tupla (a idade) e use-o como a chave de ordenação."
    
    "Coloque o resultado ordenado na variável pessoas_ordenadas."

O resultado é uma lista de tuplas ordenadas por idade.
"""