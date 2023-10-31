"""
Exercício: Função para Calcular Estatísticas de Números

Objetivo: Familiarizar com a definição de funções que 
aceitem um número variável de argumentos usando *args, bem como calcular 
algumas estatísticas básicas de um conjunto de números.

Instruções:

    1. Defina uma função chamada estatisticas que aceite 
    um número variável de argumentos numéricos.
    
    2. A função deve retornar a média, o maior e o menor número do conjunto.
    3. Peça ao usuário para inserir uma sequência de números, separados por espaços.
    4. Converta essa entrada do usuário em uma lista de números.
    5. Use a função estatisticas para calcular a média, o maior e o menor número da lista.
    6. Mostre ao usuário a média, o maior e o menor número.
"""
def estatisticas(*args):
    
    return sum(args) / len(args), max(args), min(args)

"""
input("Digite uma sequência de números separados por espaços: "): A função 
input() é usada para obter uma entrada do usuário no console. Nesse caso, a 
mensagem "Digite uma sequência de números separados por espaços: " é exibida para 
o usuário, pedindo que ele insira uma sequência de números separados por espaços.

.split(): O método split() é chamado na string de entrada fornecida pelo 
usuário. Ele divide a string em partes separadas por espaços em branco, criando 
uma lista de strings.

map(float, ...): A função map() é usada para aplicar a função 
float() a cada elemento da lista de strings. A função float() é responsável 
por converter uma string que representa um número em um número de ponto 
flutuante (float). Isso é feito para garantir que todos os números da sequência 
digitada sejam tratados como valores numéricos de ponto flutuante.

list(...) : O resultado da função map(float, ...) é convertido em uma lista de 
números de ponto flutuante. Agora, a variável numeros é uma lista contendo os 
números digitados pelo usuário, convertidos em valores de ponto flutuante.

Depois disso, a função estatisticas(*numeros) é chamada com a lista de números 
numeros desempacotada usando o operador *. A função estatisticas calcula a média, o 
maior e o menor número da sequência e retorna esses valores.

Finalmente, os resultados são impressos na tela usando a função print() para 
mostrar a média, o maior e o menor número da sequência digitada pelo usuário.
"""
numeros = list(map(float, input("Digite uma sequência de números separados por espaços: ").split()))

media, maior, menor = estatisticas(*numeros)

print(f"Média: {media}")
print(f"Maior Número: {maior}")
print(f"Menor Número: {menor}")
