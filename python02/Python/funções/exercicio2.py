def fabrica_de_funcoes(operacao):
    
    # Esta função recebe um número indefinido de argumentos e os soma.
    def soma(*args):
        
        return sum(args)
    
    # Esta função subtrai todos os números subsequentes do primeiro número.
    def subtracao(*args):
        
        resultado = args[0]
        
        # Itera sobre todos os números após o primeiro
        for num in args[1:]:
            
            #resultado = resultado - num
            resultado -= num
            
        return resultado
    
    # Esta função multiplica todos os números fornecidos.
    def multiplicacao(*args):
        
        resultado = 1
        
        # Itera sobre todos os números e os multiplica
        for num in args:
            
            #resultado = resultado * num
            resultado *= num
            
        return resultado
    
    # Esta função divide o primeiro número pelos números subsequentes.
    def divisao(*args):
        
        resultado = args[0]
        
        # Itera sobre todos os números após o primeiro
        for num in args[1:]:
            
            # Verifica se algum número é zero (para evitar divisão por zero)
            if num == 0:
                
                """
                é usada para lançar (ou "raise", em inglês) uma exceção do tipo ValueError.

                Em programação, uma exceção é uma forma de sinalizar que algo inesperado 
                aconteceu durante a execução de um programa. Quando uma exceção é 
                lançada e não tratada, ela interrompe a execução do programa e produz 
                uma mensagem de erro.

                A razão pela qual lançamos essa exceção específica é porque a divisão por zero 
                é matematicamente indefinida e resultaria em um erro se tentássemos fazer 
                isso em Python (ou na maioria das linguagens de programação). Em vez de permitir 
                que esse erro ocorra, detectamos o caso em que um número é dividido por zero e 
                lançamos uma exceção com uma mensagem explicativa.

                Em outras palavras, essa linha foi adicionada para:

                    Prevenir a ocorrência de um erro de divisão por zero.
                    
                    Fornecer uma mensagem de erro amigável e explicativa para o usuário, 
                    informando-o do problema.

                Se você remover essa linha e tentar dividir por zero, o Python lançará sua 
                própria exceção de ZeroDivisionError, que pode não ser tão amigável ou específica 
                quanto à mensagem que fornecemos.
                """
                raise ValueError("Divisão por zero não é permitida.")
                
            resultado /= num
            
        return resultado
    
    # Retorna a função correspondente baseada no valor da 'operacao'
    if operacao == "soma":
        
        return soma
    
    elif operacao == "subtracao":
        
        return subtracao
    
    elif operacao == "multiplicacao":
        
        return multiplicacao
    
    elif operacao == "divisao":
        
        return divisao
    
    else:
        
        def operacao_nao_suportada(*args):

            return "Operação não suportada."
        
        return operacao_nao_suportada
    
    
# Testando o código
adicionar = fabrica_de_funcoes("soma")
print(adicionar(5, 3, 2, 9, 4, 7)) # Esperado: 30

subtrair = fabrica_de_funcoes("subtracao")
print(subtrair(50, 30, 5)) # Esperado: 15

multiplicar = fabrica_de_funcoes("multiplicacao")
print(multiplicar(5, 3, 2)) # Esperado: 30

dividir = fabrica_de_funcoes("divisao")
print(dividir(10, 2, 2)) # Esperado: 2.5

operacao_invalida = fabrica_de_funcoes("modulo")
print(operacao_invalida(5, 3)) # Esperado: "Operação não suportada."
            
