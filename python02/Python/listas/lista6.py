"""
Slicing de Listas
        Como acessar subconjuntos de listas: minha_lista[1:3]
        Omissão de índices iniciais ou finais: minha_lista[:2], minha_lista[2:]
        Slicing com passos: minha_lista[::2]
        
O "slicing" (fatiamento) é uma maneira poderosa de acessar subconjuntos de 
listas. 

Vamos explorar isso com exemplos práticos."""

#Considere a seguinte lista para nossos exemplos:
minha_lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


#licing de Listas
#1. Como acessar subconjuntos de listas

#Para obter um subconjunto de elementos da lista, especificamos os 
#índices de início e fim separados por dois pontos :. Lembre-se de que o índice 
#de início é inclusivo, enquanto o índice de término é exclusivo.

subconjunto = minha_lista[1:4]
print(subconjunto)  # Saída: [1, 2, 3]

#2. Omissão de índices iniciais ou finais

#Se omitirmos o índice inicial, o Python começará o fatiamento desde o início 
#da lista. Se omitirmos o índice final, ele continuará até o final da lista.
# Pega todos os elementos até o índice 2 (exclusivo)

primeiros_elementos = minha_lista[:2]
print(primeiros_elementos)  # Saída: [0, 1]

# Pega todos os elementos a partir do índice 2
elementos_depois_do_indice_2 = minha_lista[2:]
print(elementos_depois_do_indice_2) # Saída: [2, 3, 4, 5, 6, 7, 8, 9]

#3. Slicing com passos

#Podemos também especificar um passo (ou incremento) para o fatiamento. 
#Por exemplo, um passo de 2 pegaria todos os outros elementos.
# Pega todos os elementos com um passo de 2 (pegando alternadamente)

elementos_alternados = minha_lista[::2]
print(elementos_alternados)  # Saída: [0, 2, 4, 6, 8]

# Podemos combinar isso com índices iniciais e finais também
subconjunto_alternado = minha_lista[2:8:2]
print(subconjunto_alternado)  # Saída: [2, 4, 6]

"""
Vamos detalhar a operação de slicing minha_lista[2:8:2].

No slicing, o formato geral é lista[início:fim:passo].

    Início (início): É onde o slicing começa. Se especificado, como neste 
    caso, o slice começará neste índice.

    Fim (fim): É onde o slicing termina, mas é exclusivo, o que significa que 
    o índice de término especificado não será incluído no slice.

    Passo (passo): É o intervalo entre os índices. Isso define de quantos em 
    quantos índices a lista será "fatiada".

Usando a nossa lista exemplo:
minha_lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

Quando fazemos:
subconjunto = minha_lista[2:8:2]

Isso pode ser lido como: "A partir da lista minha_lista, pegue todos os elementos 
começando no índice 2 até o índice 8 (mas não inclua o índice 8) em intervalos de 2 índices."

Então, isso nos dá:

    minha_lista[2] é 2
    minha_lista[4] é 4 (pulamos o índice 3 por causa do passo de 2)
    minha_lista[6] é 6 (novamente pulamos o índice 5 por causa do passo de 2)

Assim, o subconjunto resultante será: [2, 4, 6]
"""


"""
O "slicing" de listas em Python é uma ferramenta extremamente útil, que 
permite manipular e acessar os dados de maneiras versáteis. Dominar essa técnica 
pode facilitar significativamente muitas operações de manipulação de dados.
"""