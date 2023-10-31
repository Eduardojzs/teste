"""
List Comprehensions
        Uma maneira concisa de criar listas: [x**2 for x in range(10) if x % 2 == 0]
        
"List Comprehensions" são uma das características mais úteis e elegantes de Python. 

Elas oferecem uma maneira concisa de criar listas, e são frequentemente 
mais compreensíveis e mais eficientes do que usar loops."""

#1. Exemplo básico:

#Vamos começar com um exemplo simples. Imagine que queremos 
#criar uma lista dos quadrados dos números de 0 a 9:
quadrados = [x**2 for x in range(10)]
print(quadrados)
# Saída: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

#Exemplo básico e tradicional

# Inicializando uma lista vazia chamada "quadrados"
quadrados = []

# Loop através de números de 0 a 9 (pois range(10) gera números de 0 até 9)
for x in range(10):
    
    # Calculando o quadrado do número atual e adicionando à lista "quadrados"
    quadrados.append(x**2)

# Imprimindo a lista "quadrados"
print(quadrados)

quadrados_pares2 = [x**2 for x in range (10) if x % 2 == 0 ]

print(quadrados_pares2)

# Inicializando uma lista vazia chamada "quadrados_pares"
quadrados_pares = []

# Loop através de números de 0 a 9 (pois range(10) gera números de 0 até 9)
for x in range(10):
    
    # Verificando se o número atual é par
    if x % 2 == 0:
        
        # Calculando o quadrado do número par atual e adicionando à lista "quadrados_pares"
        quadrados_pares.append(x**2)

# Imprimindo a lista "quadrados_pares"
print(quadrados_pares)