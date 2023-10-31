numero = 1

# Pede ao usuário para inserir um número inteiro e converte para inteiro
max = int(input("Digite um inteiro maior que 1: ") )

# Imprime uma mensagem indicando o que será mostrado
print("Números pares entre 1 e", max, ":")

# Continua o loop enquanto 'numero' for menor ou igual a 'max'
while numero <= max:
    
    # Verifica se 'numero' é par (divisível por 2)
    if numero % 2 == 0:
        
        # Imprime o valor atual de 'numero' se for par, sem adicionar uma nova linha
        print(numero, end=" ")
        
    # Incrementa 'numero' em 1 para a próxima iteração
    numero += 1