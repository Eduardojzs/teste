"""""
Número secreto
"""""

import random

numero_secreto = random.randint(1,100)
print(numero_secreto)

tentativas = 0

while True:
    
    palpite = int(input('Tente número da sorte: '))
    tentativas +=1

    if palpite < numero_secreto:

        print('Seu número é menor que número secreto')

    elif palpite > numero_secreto:

        print('seu número é maior que o número secreto')


    else:

        print(f'Parabéns Você acertou número da sorte foi {numero_secreto} você acertou em {tentativas}')
        break