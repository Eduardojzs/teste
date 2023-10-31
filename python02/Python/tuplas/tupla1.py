"""
Exercício: Armazenando Informações sobre Livros

Contexto: Você administra uma pequena biblioteca e decide 
armazenar informações sobre seus livros usando tuplas para garantir 
que os dados sejam consistentes e imutáveis.

Objetivo: Crie tuplas para representar informações de livros usando 
diferentes métodos de criação de tuplas.

Instruções:

    1. Criar uma tupla usando parênteses:
        Crie uma tupla chamada livro1 para armazenar informações sobre um 
        livro: título, autor e ano de publicação. 
        Use a seguinte informação: "Orgulho e Preconceito", "Jane Austen", 1813.
        

    2. Tupla com um único elemento:
        Você recebeu uma doação de um livro, mas só sabe o título por 
        enquanto. Crie uma tupla chamada livro_indefinido com apenas o título: "O Pequeno Príncipe".

    3. Tupla sem parênteses:
        Para o próximo livro, use uma sintaxe simplificada. Crie uma tupla 
        chamada livro2 para armazenar: "1984", "George Orwell", 1949.

    4. Uso da função tuple():
        Você tem uma lista de informações sobre um novo livro. Converta esta 
        lista em uma tupla para garantir sua imutabilidade. 
        
        A lista é: ["O Senhor dos Anéis", "J.R.R. Tolkien", 1954]. Nomeie a tupla como livro3.

    Teste suas tuplas:
        Mostre cada uma das informações armazenadas usando a função print.

Isso dara a você uma prática valiosa na criação de tuplas usando 
várias técnicas, bem como uma compreensão de por que e quando 
usar tuplas em vez de listas ou outros tipos de dados.
"""

livro1 = "Orguljo e Preconceito", "Jane Austen", "1813"

print(livro1)


livro_indefinido = ("O Pequeno Príncipe")

print(livro_indefinido)

livro2 = "1984", "George Orwell", 1949

print(livro2)

lista =  ["O Senhor dos Anéis", "J.R.R. Tolkien", 1954]

tupla = tuple(lista)

print(tupla)