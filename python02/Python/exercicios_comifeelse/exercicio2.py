"""Exercico 
verifique a elegibilidade para votar
"""
idade_permitida = 18
idade = int(input('Digite o ano que nasceu: '))

if idade >= idade_permitida:
    print('Você ja esta de maior, então ja pode votar! ')
else:
    print('Você ainda não esta na idade para votar')
