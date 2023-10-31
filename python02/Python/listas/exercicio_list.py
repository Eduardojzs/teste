"""
Exercício: Lista de Compras

Crie um programa em Python que permita ao usuário adicionar 
itens a uma lista de compras. O programa deve exibir um menu com as seguintes opções:

    1. Adicionar item à lista
    2. Remover item da lista
    3. Exibir lista de compras
    4. Sair

O programa deve continuar executando até que o usuário escolha a opção 4 para sair.

"""
amarzenamento = []
while True:
    print(""" 
              Menu
          
    1. Adicionar item à lista
    2. Remover item da lista
    3. Exibir lista de compras
    4. Sair
          """)

    escolha = input('Escolha uma opção: ')

    if escolha == '1':
        item = input('Escolha item que deseja colocar na lista: ')
        amarzenamento.append(item)
        print('item Adicionado!')

       

    elif escolha == '2':
        if len(amarzenamento) == 0:
            print('lista vazia')
        else:
            escolha2 = input('Escolha item que deseja remover : ')
            if escolha in amarzenamento:
                amarzenamento.remove(escolha2)
                print('item removido')    
            else:
                print('item não esta na lista!')
    

    elif escolha == '3':

        if len(amarzenamento) == 0:
            print('lista vazia')
        novo_amarzem = '\n'.join(amarzenamento)
        print(novo_amarzem)

    elif escolha == '4':

        break

    else:
        print('opção invalida')

print('Sistema finalizado!')        