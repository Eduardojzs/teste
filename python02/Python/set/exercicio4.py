"""
Exercício: Funções e Métodos Básicos em Conjuntos

Objetivo: Familiarizar-se com algumas das funções e métodos fundamentais 
associados aos conjuntos em Python.

Instruções:

    1. Conjunto de Amostra:
        Crie um conjunto chamado animais contendo os seguintes 
        elementos: "cachorro", "gato", "pássaro", "peixe", "coelho".

    2. Número de Elementos:
        Use a função len() para determinar e imprimir quantos animais 
        existem no conjunto animais.

    3. Verificação de Elemento:
        Escreva uma função chamada verificar_animal que aceite um nome de animal como argumento.
        A função deve verificar se o animal especificado existe no conjunto animais usando o operador in.
        Se o animal estiver no conjunto, a função deve imprimir: "[Nome do animal] está no conjunto de animais!".
        Caso contrário, deve imprimir: "[Nome do animal] não está no conjunto de animais!".
        Teste a função com os nomes "gato" e "elefante".

    4. Cópia do Conjunto:
        Crie uma cópia do conjunto animais e armazene-a em uma variável chamada animais_copia.
        Use a função copy() para isso.
        Verifique e imprima se animais e animais_copia são o mesmo objeto em memória.
        Adicione um novo animal, "tartaruga", apenas ao conjunto animais_copia.
        Imprima ambos os conjuntos para verificar se o conjunto original animais permaneceu inalterado.
"""
#Solução

"""
1. Conjunto de Amostra:
        Crie um conjunto chamado animais contendo os seguintes 
        elementos: "cachorro", "gato", "pássaro", "peixe", "coelho".
"""

animais = {"cachorro", "gato", "pássaro", "peixe", "coelho"}

print(animais)
print()

"""
2. Número de Elementos:
        Use a função len() para determinar e imprimir quantos animais 
        existem no conjunto animais.
"""

print(f"O conjunto 'animais' contém {len(animais)}.")


"""
3. Verificação de Elemento:
        Escreva uma função chamada verificar_animal que aceite um nome de animal como argumento.
        A função deve verificar se o animal especificado existe no conjunto animais usando o operador in.
        Se o animal estiver no conjunto, a função deve imprimir: "[Nome do animal] está no conjunto de animais!".
        Caso contrário, deve imprimir: "[Nome do animal] não está no conjunto de animais!".
        Teste a função com os nomes "gato" e "elefante".
"""

def verificar_animal(nome):
    
    if nome in animais:
        
        print(f"{nome} está no conjunto de animais!")
        
    else:
        
        print(f"{nome} não está no conjunto de animais!")

verificar_animal("gato")
verificar_animal("elefante")

"""
4. Cópia do Conjunto:
        Crie uma cópia do conjunto animais e armazene-a em uma variável chamada animais_copia.
        Use a função copy() para isso.
        Verifique e imprima se animais e animais_copia são o mesmo objeto em memória.
        Adicione um novo animal, "tartaruga", apenas ao conjunto animais_copia.
        Imprima ambos os conjuntos para verificar se o conjunto original animais permaneceu inalterado.
"""

animais_copia = animais.copy()
print(animais is animais_copia)

animais_copia.add("tartaruga")
print(animais)
print(animais_copia)