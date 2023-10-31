#Argumentos Default e Non-default

"""
Em Python, ao definir uma função, você pode atribuir valores 
padrão aos parâmetros da função. Esses valores padrão são chamados de 
"argumentos default" (padrão) e permitem que você chame a função sem precisar 
fornecer valores para esses parâmetros, pois eles já têm um valor pré-definido.

Por outro lado, os "argumentos non-default" (não padrão) são aqueles que não 
possuem um valor padrão atribuído na definição da função e, portanto, precisam ser 
fornecidos como argumentos quando a função é chamada.
"""

def exibir_informacoes(nome="Allan", idade=39, cidade="Desconhecida"):
    
    """Função que exibe informações pessoais."""
    print("Nome:", nome)
    print("Idade:", idade)
    print("Cidade:", cidade)
    print()

# Argumentos sem valores default
exibir_informacoes("João", 25, "São Paulo")

# Argumento com valor default
exibir_informacoes("Maria", 30)