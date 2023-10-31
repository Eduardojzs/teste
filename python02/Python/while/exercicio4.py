somaNumerosDigitados = 0


while True:
   
    numero = int(input("Digite um número ou 0 para sair: "))
    

    somaNumerosDigitados += numero

    if numero == 0:
        print("Total: ", somaNumerosDigitados)
        break