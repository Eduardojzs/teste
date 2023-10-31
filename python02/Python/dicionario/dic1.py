"""
Exercício sobre Criando Dicionários

Objetivo: Crie dicionários seguindo as instruções fornecidas e, depois, acesse 
alguns dos valores com base nas etapas do exercício.

Parte 1: Sintaxe básica

    Crie um dicionário chamado animal que tenha as seguintes chaves e valores:
        Chave: "tipo" / Valor: "gato"
        Chave: "cor" / Valor: "branco"
        Chave: "idade" / Valor: 3

Parte 2: Dicionários vazios

    Crie um dicionário vazio chamado estudante.

    Adicione as seguintes chaves e valores ao dicionário estudante usando a sintaxe de atribuição:
        Chave: "nome" / Valor: "Carlos"
        Chave: "curso" / Valor: "Matemática"
        Chave: "semestre" / Valor: 2

Parte 3: Dicionários com múltiplos itens

    Crie um dicionário chamado livro que tenha as seguintes chaves e valores:
        Chave: "titulo" / Valor: "A Arte da Guerra"
        Chave: "autor" / Valor: "Sun Tzu"
        Chave: "publicado" / Valor: -500

Parte 4: Dicionários aninhados

    Crie um dicionário chamado universidade que contenha as seguintes informações:
        Chave: "nome" / Valor: "Universidade Federal"
        Chave: "localidade" / Valor: {"cidade": "Rio de Janeiro", "bairro": "Centro"}

    Ao acessar o dicionário universidade, imprima o nome da universidade e a cidade onde ela se localiza.
"""


"""

Parte 1: Sintaxe básica

    Crie um dicionário chamado animal que tenha as seguintes chaves e valores:
        Chave: "tipo" / Valor: "gato"
        Chave: "cor" / Valor: "branco"
        Chave: "idade" / Valor: 3

"""
animal = {
    "tipo": "gato",
    "cor": "Branco",
    "idade": 3

}

print(animal)

"""
Parte 2: Dicionários vazios

    Crie um dicionário vazio chamado estudante.

    Adicione as seguintes chaves e valores ao dicionário estudante usando a sintaxe de atribuição:
        Chave: "nome" / Valor: "Carlos"
        Chave: "curso" / Valor: "Matemática"
        Chave: "semestre" / Valor: 2
        
"""
estudante = {}

# Adicionando pares chave-valor ao dicionário 'estudante'
estudante["nome"] = "Carlos"             # Adiciona a chave 'nome' com o valor "Carlos"
estudante["curso"] = "Matemática"       # Adiciona a chave 'curso' com o valor "Matemática"
estudante["semestre"] = 2       # Adiciona a chave 'semestre' com o valor numérico 2

"""
Parte 3: Dicionários com múltiplos itens

    Crie um dicionário chamado livro que tenha as seguintes chaves e valores:
        Chave: "titulo" / Valor: "A Arte da Guerra"
        Chave: "autor" / Valor: "Sun Tzu"
        Chave: "publicado" / Valor: -500
"""

livro = {
    "titulo": "A Arte da Guerra",
    "autor": "Sun Tzu",
    "publicado": "-500"
}

"""
Parte 4: Dicionários aninhados

    Crie um dicionário chamado universidade que contenha as seguintes informações:
        Chave: "nome" / Valor: "Universidade Federal"
        Chave: "localidade" / Valor: {"cidade": "Rio de Janeiro", "bairro": "Centro"}

    Ao acessar o dicionário universidade, imprima o nome da universidade e a cidade onde ela se localiza.
"""
universidade = {

    "nome":{
        "nome": "Universidae Federal"

    },

    "localidade":{
        "cidade": "Rio De Janeiro",

        "bairro": "centro"
    }


}

