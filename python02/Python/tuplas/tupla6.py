"""
Exercício: Gestão de Pacotes de Viagem

Contexto: Você trabalha em uma agência de turismo e tem pacotes 
de viagem que são representados como tuplas. Cada pacote contém o 
destino, o número de noites e o preço. Para facilitar o processamento 
desses pacotes, você precisa desempacotar os detalhes em variáveis individuais.

Dados fornecidos:

Considere o seguinte pacote de viagem: pacote_viagem = ("Paris", 5, 1500), onde:

    "Paris" é o destino da viagem.
    5 é o número de noites.
    1500 é o preço do pacote em dólares.

Objetivo: Desempacote os detalhes do pacote de viagem em variáveis individuais e imprima as informações.

Instruções:

    Atribua os valores da tupla pacote_viagem a três variáveis: destino, noites e preco.
    Imprima o destino, o número de noites e o preço do pacote.

Questões:

print('a) Qual é o destino do pacote de viagem?')
print('b) Por quantas noites é o pacote?')
print('c') Qual é o preço do pacote?')

Este exercício visa ajudar a compreenderem e praticarem o desempacotamento 
de tuplas, uma técnica útil para atribuir múltiplos valores a variáveis de 
uma vez. Ao final, os alunos devem ser capazes de extrair informações de 
uma tupla e utilizá-las separadamente.
"""

pacote_viagem = ("Paris", 5, 1500)

viagem, dias, valor = pacote_viagem
print('a) Qual é o destino do pacote de viagem?')
print(f'Destino {viagem}')
print()
print('b) Por quantas noites é o pacote?')
print(f'Quantidade de noites {dias}')
print()
print('c) Qual é o preço do pacote?')
print(f'preço {valor}')