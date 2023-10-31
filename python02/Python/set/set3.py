"""
Operações com Conjuntos
        União: s1 | s2 ou s1.union(s2)
        Intersecção: s1 & s2 ou s1.intersection(s2)
        Diferença: s1 - s2 ou s1.difference(s2)
        
        Diferença simétrica (elementos que estão em um conjunto ou 
        no outro, mas não em ambos): s1 ^ s2 ou s1.symmetric_difference(s2)
        
        Subset (subconjunto): s1.issubset(s2)
        Superset (superconjunto): s1.issuperset(s2)
"""

#1. Criando dois conjuntos iniciais:
s1 = {1, 2, 3, 4}
s2 = {3, 4, 5, 6}

#2. União:
#Une os elementos dos dois conjuntos, eliminando repetições.
uniao = s1 | s2
print(uniao)  # Saída: {1, 2, 3, 4, 5, 6}

# Ou usando o método union()
uniao_metodo = s1.union(s2)
print(uniao_metodo)  # Saída: {1, 2, 3, 4, 5, 6}

#3. Intersecção:

#Retorna os elementos que estão presentes em ambos os conjuntos.
interseccao = s1 & s2
print(interseccao)  # Saída: {3, 4}

# Ou usando o método intersection()
interseccao_method = s1.intersection(s2)
print(interseccao_method)  # Saída: {3, 4}

#4. Diferença:

#Retorna os elementos que estão no primeiro conjunto, mas não no segundo.
diferenca = s1 - s2
print(diferenca)  # Saída: {1, 2}

# Ou usando o método difference()
diferenca_metodo = s1.difference(s2)
print(diferenca_metodo)  # Saída: {1, 2}

#5. Diferença simétrica:

#Retorna os elementos que estão em um conjunto 
#ou no outro, mas não em ambos.
diferenca_simetrica = s1 ^ s2
print(diferenca_simetrica)  # Saída: {1, 2, 5, 6}

# Ou usando o método symmetric_difference()
diferenca_simetrica_metodo = s1.symmetric_difference(s2)
print(diferenca_simetrica_metodo)  # Saída: {1, 2, 5, 6}

#6. Subset (subconjunto):

#Verifica se o primeiro conjunto é um subconjunto do segundo.
s3 = {1, 2}
is_subset = s3.issubset(s1)
print(is_subset)  # Saída: True

#7. Superset (superconjunto):

#Verifica se o primeiro conjunto é um superconjunto do segundo.
is_superset = s1.issuperset(s3)
print(is_superset)  # Saída: True

"""
Estes exemplos mostram o básico sobre como realizar operações 
em conjuntos em Python. Conjuntos são ferramentas poderosas, especialmente 
quando você precisa realizar operações matemáticas em grupos de dados.
"""

"""
Os métodos symmetric_difference(), issubset(), e issuperset() são métodos 
associados à estrutura de dados set em Python. 

Vamos explorar cada um deles em detalhes:

    symmetric_difference():
        Função: Este método retorna a diferença simétrica de dois conjuntos.
        
        Definição: A diferença simétrica de dois conjuntos é o 
        conjunto de elementos que estão em um dos conjuntos, mas não estão em ambos.
        
    issubset():

        Função: Este método verifica se um conjunto é subconjunto de outro.
        
        Definição: Um conjunto A é considerado um subconjunto de B se todos 
        os elementos de A também estiverem em B.
        
    issuperset():

        Função: Este método verifica se um conjunto é superconjunto de outro.
    
        Definição: Um conjunto A é considerado um superconjunto de B se A 
        contiver todos os elementos de B.
        
    Em resumo:

        symmetric_difference() é útil quando você deseja encontrar elementos 
        que são exclusivos para cada conjunto quando comparados entre si.

        issubset() e issuperset() são úteis para verificar as relações de 
        subconjunto e superconjunto entre dois conjuntos, respectivamente.
"""