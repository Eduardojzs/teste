"""
Documentação e Anotações de Funções
•	Docstrings
•	Anotações de tipo (Type Hints)


1. Docstrings:

Docstrings são usadas para documentar especificamente o que uma função 
faz, seus parâmetros e o que ela retorna. Eles são colocados logo após 
a definição da função, antes do código da função começar, e são escritos entre três aspas duplas """

#Exemplo
def somar(a, b):
    
    """
    Função que retorna a soma de dois números.

    Parâmetros:
    a (int ou float): Primeiro número.
    b (int ou float): Segundo número.

    Retorna:
    int ou float: A soma de a e b.
    """
    return a + b


print(somar(2, 3))  # Saída: 5
print(somar.__doc__)  # Isso imprimirá a docstring da função


#2. Anotações de tipo (Type Hints)
"""
Anotações de tipo são usadas para indicar os tipos esperados dos 
argumentos e o tipo de retorno de uma função. Elas não causam nenhuma 
verificação de tipo em tempo de execução, mas são úteis para documentação e 
ferramentas de verificação estática de tipo como o mypy.

Exemplo:
"""
def multiplicar(a: int, b: int) -> int:
    
    """Função que retorna a multiplicação de dois números inteiros."""
    return a * b

print(multiplicar(4, 5))  # Saída: 20

"""
No exemplo acima, as anotações a: int e b: int indicam que os parâmetros 
a e b devem ser inteiros. A anotação -> int indica que a função retorna um inteiro.

A combinação de docstrings e anotações de tipo pode tornar o código 
Python mais legível e manutenível, pois fornece informações claras sobre a função, seus 
argumentos e retornos.
"""
