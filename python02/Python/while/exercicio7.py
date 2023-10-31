"""
Exercício: Calculadora Simples

Desenvolva uma calculadora simples que permite ao usuário realizar operações 
básicas de adição, subtração, multiplicação e divisão.

Objetivos:

    Mostrar um Menu ao Usuário:
    
        - A calculadora deve exibir um menu com cinco opções: 
            - adição
            - subtração
            - multiplicação
            - divisão
            - sair
            
        O usuário deve ser capaz de selecionar a operação desejada através da entrada de um número correspondente.

    Receber Dois Números:
    
        - Após selecionar a operação, o usuário deve inserir dois números
        que serão utilizados na operação.

    Realizar a Operação Selecionada:
    
        - A calculadora deve realizar a operação selecionada com os números 
        inseridos e exibir o resultado.
        
    Repetir ou Encerrar:
    
        - Após cada operação, o menu deve ser exibido novamente, permitindo que 
        o usuário realize outra operação ou saia do programa.
        - O programa deve continuar funcionando até que o usuário escolha sair.


Boa sorte e divirta-se programando!
"""

while True:

    print("""Bem vindo a calculadora
    [1]- adição
    [2]- subtração
    [3]- multiplicação
    [4]- divisão 
    [5]- sair """)
    pergunta = input('Qual deseja: ')


    if pergunta == '1':
        print('Calculo de adição')
        print()
        numero1 = float(input('Escolha um número: '))
        numero2 = float(input('Escolha Outro número: '))
        resposta1 = numero1 + numero2
        print(f'resposta é {resposta1}')

    elif pergunta == '2':
        print('Calculo de subtração')
        print()
        numero3 = float(input('Escolha um número: '))
        numero4 = float(input('Escolha Outro número: '))
        resposta2 = numero3 - numero4
       
        print(f'resposta é {resposta2}')    
           
    elif pergunta == '3':
        
            print('Calculo de multiplicação')
            print()
            numero5 = float(input('Escolha um número: '))
            numero6 = float(input('Escolha Outro número: '))
            resposta3 = numero5 * numero6
            print(f'resposta é {resposta3}')
        
        
            

    elif pergunta == '4':
        print('Calculo de divisão')
        print()
        numero7 = float(input('Escolha um número: '))
        numero8 = float(input('Escolha Outro número: '))
        if numero8 !=0:
            resposta3 = numero7 / numero8
            print(f'resposta é {resposta3}') 
        else:
             print('Erro: Divisão por zero.')    
        
                    
    elif pergunta == '5':
        break


    else:
        print()
        print('opeção invalida')
                                                    

print('Obrigado volte sempre!')                                                    