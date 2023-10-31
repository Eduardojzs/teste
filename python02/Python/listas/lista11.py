"""
Exercício: Listas Aninhadas

Objetivo: Aprofundar o entendimento sobre listas dentro de listas e como interagir com elas usando loops aninhados.

Instruções:

    Crie uma matriz 3x3 chamada matriz com os seguintes valores:
    
1, 2, 3
4, 5, 6
7, 8, 9

Represente essa matriz como uma lista de listas.

1. Acesse e imprima o valor localizado na segunda linha e terceira coluna (deve ser o número 6).

2. Utilizando loops aninhados, calcule e imprima a soma de todos os valores presentes na matriz.

3. Usando loops aninhados, imprima a matriz linha por linha, e cada elemento separado por uma tabulação (\t).

Valor na segunda linha e terceira coluna: 6
Soma dos valores da matriz: 45
Matriz:
1	2	3	
4	5	6	
7	8	9	

Esse exercício oferece uma prática abrangente sobre a interação com listas 
aninhadas e a manipulação de elementos dentro de matrizes.

"""
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]


elemento = matriz[1][2]
print(f'alor na segunda linha e terceira coluna: {elemento}')

print()

soma = 0 
for linha in matriz:

    
    for numero in linha:
        soma += numero

print(f'Soma dos valores da matriz: {soma}')
print()


for linha in matriz:

    # Loop interno: itera sobre cada número (ou elemento) dentro da linha atual
    for numero in linha:
    
        # Imprime o número atual seguido por uma tabulação (representada por "\t"), 
        # mantendo os números na mesma linha ao imprimir
        print(numero, end="\t")

print()            