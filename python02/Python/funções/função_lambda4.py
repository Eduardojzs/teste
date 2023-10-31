"""
Vamos criar um exemplo onde filtramos uma lista de strings 
para obter apenas aquelas que começam com a letra "A".

Problema:

Dada uma lista de nomes, filtre-a para obter apenas os nomes 
que começam com a letra "A".
"""

# Lista original de nomes
nomes = ["Alice", "Bob", "Anna", "Charlie", "Alex", "Tom"]

# Usando filter() e lambda para obter apenas nomes que começam com "A"
nomes_com_A = list(filter(lambda nome: nome[0] == "A", nomes))

"""
    list(): Esta função é usada para converter um iterável em uma lista. 
    No contexto desta linha, ela está sendo usada para converter o resultado 
    do filter() de um iterador de volta para uma lista.

    filter(): A função filter() é uma função built-in do Python que é usada 
    para filtrar os itens de um iterável (como uma lista) com base em uma função 
    fornecida. Ela irá retornar um iterador contendo todos os itens do iterável para 
    os quais a função aplicada retorna True.

    lambda nome: nome[0] == "A": Esta é uma função lambda, que é uma pequena função anônima em Python.
    
        nome: é o argumento da função. Para cada string na lista nomes, a string 
        será passada para esta função lambda.
        
        nome[0]: obtém o primeiro caractere da string nome.
        
        nome[0] == "A": verifica se o primeiro caractere da string nome 
        é igual a "A". Se for, a função retorna True; caso contrário, retorna False.

    nomes: É a lista original de nomes que você deseja filtrar.

Quando juntamos tudo, a linha está fazendo o seguinte:

    "Quero filtrar a lista nomes."
    "Para cada nome na lista, quero verificar se ele começa com a letra 'A'."
    "Se começar, inclua-o no resultado."
    "Finalmente, converta o resultado filtrado de volta em uma lista."

Como resultado, nomes_com_A será uma lista contendo apenas os nomes da 
lista original nomes que começam com a letra "A".
"""

print(nomes_com_A)  # Saída: ['Alice', 'Anna', 'Alex']

"""
Explicação:

A função lambda lambda nome: nome[0] == "A" verifica se a 
primeira letra do nome é "A". A função filter() aplica essa função 
lambda a cada item da lista nomes. Os itens que retornam True (aqueles que 
começam com "A") são mantidos no resultado.
"""