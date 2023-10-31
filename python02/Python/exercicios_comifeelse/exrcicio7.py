#Exercicio Par ou Impar
#Crie um algoritmo que solicite a entrada de um número positivo e inteiro e imprima se o
#número é PAR ou IMPAR

n1 = int(input("Digite um número: "))

verificaNumero = n1 % 2

if verificaNumero == 0:
    
    print(f"O número {n1} é PAR")
    
else:
    
    print(f"O número {n1} é IMPAR")