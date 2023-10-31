"""
Exercício sobre Operações Básicas com Dicionários

Objetivo: Dado um dicionário que representa informações de 
um aluno, sua tarefa é realizar operações para 
adicionar, atualizar, remover e copiar informações.

Dicionário fornecido:

aluno = {
    "matricula": "A12345",
    "nome": "João Silva",
    "curso": "Engenharia de Computação",
    "semestre": 5,
    "cr": 8.5
}

Instruções:

    1. Adicionando itens:
        - Adicione uma chave "hobbies" com o valor de uma 
        lista contendo: "Leitura", "Corrida", "Xadrez".
        
        - Adicione uma chave "idade" com valor 22.

    2. Atualizando itens:
        - Atualize o valor da chave "semestre" para 6.
        - Atualize o valor da chave "cr" para 8.7.

    3. Removendo itens:
        - Use o método del para remover a chave "idade".
        
        - Use o método pop() para remover a chave "hobbies" 
        e imprima os hobbies removidos.
        
        - Use o método popitem() para remover o último item adicionado 
        ao dicionário e imprima a chave e o valor do item removido.

    4. Copiando dicionários:
        - Crie uma cópia do dicionário aluno chamada copia_1 usando o método copy().
        - Crie outra cópia do dicionário aluno chamada copia_2 usando o método dict().
"""
#Solução:

# Inicialização de um dicionário chamado 'aluno' com cinco pares chave-valor
aluno = {
    "matricula": "A12345",                         # Chave 'matricula' com o valor "A12345"
    "nome": "João Silva",                          # Chave 'nome' com o valor "João Silva"
    "curso": "Engenharia de Computação",           # Chave 'curso' com o valor "Engenharia de Computação"
    "semestre": 5,                                 # Chave 'semestre' com o valor numérico 5
    "cr": 8.5                                      # Chave 'cr' (Coeficiente de Rendimento) com o valor numérico 8.5
}

# 1. Adicionando itens ao dicionário 'aluno'

# Adicionando a chave 'hobbies' com uma lista de hobbies
aluno["hobbies"] = ["Leitura", "Corrida", "Xadrez"]

# Adicionando a chave 'idade' com o valor numérico 22
aluno["idade"] = 22

# 2. Atualizando itens do dicionário 'aluno'

# Atualizando o valor associado à chave 'semestre' para 6
aluno["semestre"] = 6

# Atualizando o valor associado à chave 'cr' (Coeficiente de Rendimento) para 8.7
aluno["cr"] = 8.7

# 3. Removendo itens do dicionário 'aluno'

# Removendo o item com a chave 'idade' do dicionário
del aluno["idade"]

# Removendo e retornando o valor associado à chave 'hobbies', e armazenando-o na variável 'hobbies_removidos'
hobbies_removidos = aluno.pop("hobbies")

# Imprimindo a lista de hobbies que foi removida
print("Hobbies removidos:", hobbies_removidos)

# Removendo e retornando o último par chave-valor inserido no dicionário, e armazenando-o na variável 'item_removido'
item_removido = aluno.popitem()

# Imprimindo o par chave-valor que foi removido
print("Item removido:", item_removido)

print("\nDicionário:", aluno)

# 4. Copiando o dicionário 'aluno'

# Criando uma cópia superficial do dicionário 'aluno' usando o método .copy()
copia_1 = aluno.copy()

# Criando outra cópia superficial do dicionário 'aluno' usando a função dict()
copia_2 = dict(aluno)

# Imprimindo as cópias criadas
print("\nCópias do dicionário aluno:")
print("Cópia 1:", copia_1)
print("Cópia 2:", copia_2)
