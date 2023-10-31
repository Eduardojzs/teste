"""
Funções Anônimas (Lambda)
o	Definição e uso
o	Limitações em relação às funções regulares


Função lambda


Funções lambda são funções anônimas de pequena extensão. Ao contrário 
de uma função definida com def, a função lambda pode ter apenas uma 
expressão e retorna implicitamente o resultado dessa expressão. Ela é 
frequentemente usada para pequenas operações que são convenientes de 
se definir sem nomear uma função completa.


"""

#Exemplo Prático 1: Definição e uso

#Função Regular para Dobrar um Número

def dobrar(n):
    
    return n * 2

print("Função Regular:", dobrar(5)) # Saída: 10 

#Função Lambda para Dobrar um Número
dobrar_com_lambda = lambda n: n * 2

print("Função Lambda:", dobrar_com_lambda(5)) # Saída: 10 

"""
Exemplo Prático 2: Limitações

    Expressividade

Função Regular para Classificar Números:
"""

def classificar_numero(n):
    
    if n < 0:
        
        return "Negativo"
    
    elif n == 0:
        
        return "Zero"
    
    else:
        
        return "Positivo"

print(classificar_numero(5)) #Saída: Positivo

#Tentativa de Função lambda para Classificar Números (Menos Clara):

classificar_numero_lambda = lambda n: "Negativo" if n < 0 else ( "Zero" if n == 0 else "Positivo")

print(classificar_numero_lambda(5)) #Saída: Positivo