"""
Listas e Strings
        Conversão de strings para listas: list(), split().
        Conversão de listas para strings: join().
"""

#Exemplo prático

#Conversão de strings para listas

#A) Usando list():

#Ao usar a função list() em uma string, cada caractere da string 
#será um elemento da lista resultante.
s = "olá"
lista_s = list(s)
print(lista_s)  # Saída: ['o', 'l', 'á']

#B) split():

#A função split() é usada para dividir uma string em uma lista com 
#base em um delimitador especificado. Se nenhum delimitador for especificado, ela 
#dividirá a string nos espaços em branco.
frase = "Python é divertido"
print('split')
palavras = frase.split()
print(palavras)  # Saída: ['Python', 'é', 'divertido']

data = "12/10/2023"
elementos_data = data.split("/")
print('split')
print(elementos_data)

#Conversão de listas para strings

#Usando join():

print()

#A função join() é usada para converter uma lista em uma string. Ela une 
#os elementos de uma lista em uma única string com base em um delimitador especificado.
lista_palavras = ['Python', 'é', 'incrível']

frase_juntada = ' '.join(lista_palavras)
print(frase_juntada)  # Saída: "Python é incrível"

lista_data = ["25", "12", "2023"]

print(lista_data)

data_juntada = '/'.join(lista_data)
print(data_juntada)

"""
Essas são operações comuns quando estamos trabalhando com processamento de texto 
ou manipulação de dados em Python. Conhecer como converter entre strings e 
listas é essencial para muitas tarefas!
"""