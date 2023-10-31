import random

#Números Aleatorios
print(random.randrange(1, 1000))

#Números Flutuantes 
print(random.random())

#Números interios Aleatorios
print(random.randint(1, 10))

# escolhe aleatorio str de uma lista 
frutas = ['uva', 'pera', 'banana']

nova_fruta = random.choice(frutas)
print(nova_fruta)

# Números aleatorio de uma lsita
numeros = [1, 2, 3, 4, 5, 6]

random.shuffle(numeros)
print(numeros)