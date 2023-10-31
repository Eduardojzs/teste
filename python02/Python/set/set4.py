"""
Outras Funções e Métodos
        len(): Retorna o número de elementos no conjunto.
        in: Verifica a existência de um elemento no conjunto.
        copy(): Retorna uma cópia do conjunto.
"""

#Conjunto de Amostra

#Vamos considerar um conjunto chamado frutas que contém os nomes de algumas frutas:
frutas = {"maça", "banana", "laranja", "uva", "manga"}

#1. len():

#Usar len() para obter o número de frutas no conjunto:
numero_de_frutas = len(frutas)
print(f"O conjunto tem {numero_de_frutas} frutas.") 
# Saída: O conjunto tem 5 frutas.

#2. in:

#Verificar se uma fruta específica está no conjunto:
fruta_desejada = "maça"
if fruta_desejada in frutas:
    print(f"{fruta_desejada} está no conjunto de frutas.")
else:
    print(f"{fruta_desejada} não está no conjunto de frutas.")
# Saída: maçã está no conjunto de frutas.

#3. copy():

#Copiar o conjunto de frutas para outro conjunto:
frutas_copia = frutas.copy()
print(frutas_copia)
# Saída: {'banana', 'maça', 'manga', 'uva', 'laranja'}

# Verificando se os conjuntos são realmente diferentes em memória:
print(frutas is frutas_copia)  # Saída: False


"""
Estes exemplos ilustram como usar funções e métodos comuns em 
conjuntos para realizar tarefas básicas.
"""