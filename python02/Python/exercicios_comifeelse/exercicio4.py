"""
Exercício:

Calculadora de Descontos

Você é um cliente em uma loja que está tendo uma promoção especial. Dependendo 
do valor da sua compra, você pode receber um desconto!

    Execute o programa.
    
    Insira o valor da sua compra quando solicitado.
    
    O programa irá calcular e informar o valor do desconto aplicado e o valor final 
    com o desconto.

Os descontos são aplicados da seguinte forma:

    Compras acima de R$1000 recebem 20% de desconto.
    Compras de R$500 a R$1000 recebem 10% de desconto.
    Compras abaixo de R$500 não recebem desconto.
    
    
"""
# Solicita ao usuário o valor da compra
valor_compra = float(input("Por favor, digite o valor da sua compra: $"))

# Verifica em qual categoria de desconto a compra se encaixa
if valor_compra > 1000:
    
    # Se a compra for maior que R$1000, aplica um desconto de 20%
    desconto = 0.20 * valor_compra
    
    # Imprime uma mensagem informando o desconto de 20%
    print("Você recebeu 20% de desconto!")
    
elif valor_compra >= 500 and valor_compra <= 1000:
    
    # Se a compra for entre R$500 e R$1000, aplica um desconto de 10%
    desconto = 0.10 * valor_compra
    
    # Imprime uma mensagem informando o desconto de 10%
    print("Você recebeu 10% de desconto!")
    
else:
    
    # Se a compra for menor que $500, não aplica desconto
    desconto = 0
    
    # Imprime uma mensagem informando que não há desconto
    print("Você não recebeu desconto.")

# Calcula o valor final após o desconto
valor_final = valor_compra - desconto

# Imprime o valor do desconto e o valor final da compra
print(f"Valor do desconto: R${desconto:.2f}")
print(f"Valor final da compra: R${valor_final:.2f}")
