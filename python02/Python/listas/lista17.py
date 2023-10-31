"""
Exercício: Listas e Strings

Objetivo: Familiarizar-se com as operações de conversão entre 
listas e strings, usando métodos como list(), split(), e join().

Instruções:

    Dada a string palavra = "Python", converta-a para uma lista de 
    caracteres e imprima a lista resultante. Use o método list() para isso.

    Dada a frase frase = "Aprendendo Python é divertido!", divida-a em uma 
    lista de palavras e imprima a lista resultante. Utilize o método split().

    Usando a lista do Passo 2, junte as palavras para formar a frase original 
    novamente e imprima-a. Utilize o método join().

    Dada a lista itens = ["maçã", "banana", "cereja"], converta-a em uma string onde 
    cada item é separado por uma vírgula e um espaço e imprima a string resultante. 
    
    Por exemplo: "maçã, banana, cereja".
    
Saída esperada:

Lista de caracteres: ['P', 'y', 't', 'h', 'o', 'n']
Lista de palavras: ['Aprendendo', 'Python', 'é', 'divertido!']
Frase reconstruída: Aprendendo Python é divertido!
String de itens: maçã, banana, cereja

Este exercício ajuda os alunos a entender e praticar as transformações 
entre listas e strings, utilizando os métodos comuns para tais operações.
"""

palavra = "Python"
lista_nova = list(palavra)

print(f'Lista de caracteres: {lista_nova}')

frase = "Aprendendo Python é divertido!"
palavra2 = frase.split()
print(f'Lista de palavras: {palavra2}')

frase_junta = ''.join(frase)
print(f'Frase reconstruída: {frase_junta}')

itens = ["maçã", "banana", "cereja"]

intem_virgula = ', '.join(itens)
print(f'String de itens: {intem_virgula}')