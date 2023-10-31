"""
Iteração em Listas
        Usando o loop for.
        Usando enumerate() para obter índice e valor ao iterar.
"""

#Exemplo prático

#Vamos considerar a seguinte lista de frutas:
frutas = ["maçã", "banana", "cereja", "damasco", "figo"]

#Usando o loop for para iterar sobre os valores da lista:

#Neste exemplo, vamos imprimir cada fruta da lista.
for fruta in frutas:
    
    print(fruta)
    
#Usando enumerate() para obter índice e valor ao iterar:

#A função enumerate() retorna tanto o índice quanto o valor ao iterar 
#sobre uma lista. Isso é útil quando você quer saber a posição (índice) 
#de cada item na lista enquanto itera.

for indice, fruta in enumerate(frutas):
    print(f"Fruta no índice {indice} é {fruta}")


"""
Nota: Em Python, a indexação começa em 0, então a primeira 
fruta "maçã" está no índice 0, a segunda "banana" no índice 1 e assim por diante.

Com essas técnicas, você pode facilmente iterar sobre listas em Python, acessando 
não apenas os valores dos itens, mas também seus índices.
"""
    