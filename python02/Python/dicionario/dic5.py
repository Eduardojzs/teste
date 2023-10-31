"""
Iterando Sobre Dicionários
        Usando loops for
        Iterando sobre chaves, valores e itens
"""

#Iterando Sobre Dicionários

#Exemplo Prático:

#Imagine que temos um dicionário que representa as notas de um aluno
#em diferentes matérias. Queremos iterar sobre esse dicionário para 
#exibir as matérias, as notas e também calcular a média das notas.

# Definindo um dicionário chamado 'notas' que armazena 
# as notas do aluno em diferentes matérias
notas = {
    "Matemática": 8.5,  # Matemática: 8.5
    "Português": 9.0,   # Português: 9.0
    "História": 7.5,    # História: 7.5
    "Geografia": 8.0,   # Geografia: 8.0
    "Química": 9.5      # Química: 9.5
}

# 1. Iteração sobre as chaves do dicionário (neste caso, são as matérias)

# Imprimindo um cabeçalho para identificar a seção de saída
print("Matérias cursadas pelo aluno:")

# Usando um loop 'for' para iterar sobre as chaves do 
#dicionário 'notas' (por padrão, a iteração é feita sobre as chaves)
for materia in notas:
    print(materia)
    
# Outra forma de iterar sobre as chaves de um 
# dicionário é usar o método .keys()

# Imprimindo um cabeçalho para identificar a nova seção de saída
print("\nMatérias (usando .keys()):")

# Iterando sobre as chaves do dicionário 'notas' usando o 
#método .keys() e imprimindo cada chave
for materia in notas.keys():
    print(materia)

    
# 2. Iterando apenas sobre os valores (notas)

# Imprimindo um cabeçalho para identificar a seção de saída
print("\nNotas do aluno:")

# Inicializando uma variável 'total' para somar as notas do aluno
total = 0

# Usando um loop 'for' para iterar sobre os valores do 
# dicionário 'notas' usando o método .values()
for nota in notas.values():
    
    # Imprimindo a nota atual
    print(nota)
    
    # Somando a nota atual ao total
    # total = total + nota
    total += nota

# Calculando a média das notas dividindo o total pelo 
# número de notas (len(notas))
media = total / len(notas)

# Imprimindo a média calculada
print("\nMédia das notas:", media)
