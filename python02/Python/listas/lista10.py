"""
Listas Aninhadas (listas de listas)
        Criando e acessando listas dentro de listas.
        Utilizando loops aninhados para iterar sobre elas.
        
Listas aninhadas, ou listas de listas, são basicamente listas que 
têm outras listas como seus elementos. Elas são úteis em muitas situações, 
especialmente ao representar estruturas bidimensionais como matrizes.

"""

#1. Criando Listas Aninhadas:

#Vamos considerar que queremos representar uma matriz 3x3:
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

#Aqui, matriz é uma lista de 3 elementos, onde cada elemento é, por sua vez, uma lista de 3 números.

#2. Acessando Listas Aninhadas:

#Para acessar um elemento específico, você precisa especificar dois índices: o índice 
#da lista externa e o índice da lista interna.

#Por exemplo, para acessar o número 5:
elemento = matriz[1][1]
print(elemento)

#O primeiro índice [1] refere-se à segunda lista [4, 5, 6], e o segundo 
#índice [1] refere-se ao segundo elemento dessa lista, que é 5.

#3. Utilizando Loops Aninhados para Iterar:

# Para iterar sobre cada elemento da matriz, usamos loops for aninhados:
# Loop externo: itera sobre cada linha da matriz
for linha in matriz:
    
    # Loop interno: itera sobre cada número (ou elemento) dentro da linha atual
    for numero in linha:
        
        # Imprime o número atual seguido por um espaço, sem mudar de linha devido ao parâmetro "end=' '"
        print(numero, end=' ')
    
    # Uma vez que todos os números de uma linha são impressos, esta linha imprime uma quebra de linha
    # para separar visualmente as linhas da matriz ao imprimir
    print()  

#Aqui, o loop externo itera sobre cada linha da matriz, enquanto o loop 
#interno itera sobre cada numero dentro da respectiva linha.



#4. Exemplo Prático:

#Vamos supor que queremos calcular a transposta dessa matriz. 
#A transposta de uma matriz é obtida trocando suas linhas por colunas:

# Inicializando uma lista vazia chamada "transposta"
transposta = []

# Loop através de cada coluna da matriz original
for i in range(len(matriz[0])):
    
    # Inicializa uma linha temporária para construir uma linha da matriz transposta
    linha_temporaria = []
    
    # Loop através de cada linha da matriz original
    for j in range(len(matriz)):
        
        # Adiciona o elemento da posição j,i (transposto) à linha temporária
        linha_temporaria.append(matriz[j][i])
        
    # Adiciona a linha temporária completa à matriz transposta
    transposta.append(linha_temporaria)

"""
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
"""