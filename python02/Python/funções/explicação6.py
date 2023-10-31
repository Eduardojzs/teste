#Vários argumentos xargs nomeando parametros

#função que recebe vários argumentos nomeados usando **kwargs:

"""
Em Python, **kwargs é um parâmetro especial usado em definições de função 
para capturar argumentos nomeados extras passados para a função. 
O termo "kwargs" é uma convenção comumente usada, mas o nome em si pode ser 
qualquer outro desde que seja precedido por dois asteriscos (**).

O parâmetro **kwargs permite que uma função aceite um número variável 
de argumentos nomeados adicionais. Os argumentos nomeados extras são 
passados para a função como um dicionário, onde as chaves são os nomes 
dos argumentos e os valores são os valores atribuídos a esses argumentos.
"""

def exibir_informacoes(**teste):
    
    """Função que exibe informações pessoais"""
    for chave, valor in teste.items():
        print(chave + ": " + str(valor))
        
exibir_informacoes(nome="João", idade=25, cidade="São Paulo", sexo="Masculino", nome_da_mãe = "Rita")