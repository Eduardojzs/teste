#Vários argumentos *args com números

"""
 parâmetro especial *args, que permite receber um número variável de argumentos numéricos. 
 Dentro da função, os argumentos são tratados como uma tupla.
"""

def soma(*args):
    
    """Função que retorna a soma de vários números."""
    resultado = sum(args)
    return resultado

total = soma(2, 4, 6, 8, 10)
print("A soma dos números é:", total)

"""
Dessa forma, a função soma() é capaz de lidar com qualquer quantidade de argumentos 
numéricos e retorna a soma total desses números.
"""
print()