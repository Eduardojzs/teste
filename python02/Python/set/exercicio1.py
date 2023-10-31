"""
Exercício: Criação de Conjuntos em Python

Objetivo: Familiarizar-se com a criação de conjuntos em Python utilizando duas abordagens diferentes.

Instruções:

    1. Usando Chaves:
        Crie um conjunto chamado frutas_chaves que contenha as seguintes 
        frutas: "maçã", "banana" e "cereja".
        
        Imprima o conjunto.

    2. Usando a Função set():
        Crie uma lista chamada frutas_lista contendo as 
        frutas: "uva", "manga", "manga" e "uva".
        
        Converta frutas_lista em um conjunto chamado frutas_funcao.
        Imprima o conjunto.

    3. Comparação:
        Verifique se os conjuntos frutas_chaves e frutas_funcao possuem 
        alguma fruta em comum. Se sim, imprima a fruta em comum. Caso contrário, 
        imprima "Os conjuntos não têm frutas em comum".

Dicas:

    Lembre-se que conjuntos não permitem elementos duplicados. Portanto, ao 
    criar um conjunto com elementos repetidos, o conjunto resultante terá apenas 
    uma instância de cada elemento.
"""
frutas_chaves = {"maçã", "banana", "cereja"}

print(frutas_chaves)

frutas_lista = ["uva", "manga", "manga", "uva","maçã"]

print(frutas_lista)

frunta_funcao = set(frutas_lista)

print(frunta_funcao)

interseccao = frutas_chaves.intersection(
frunta_funcao)
if interseccao:
    print(f"Fruta(s) em comum: {interseccao}")
else:
    print("Os conjuntos não têm frutas em comum.")

"""
O método intersection() é um dos vários métodos disponíveis para 
conjuntos (set) em Python. Ele é usado para obter a intersecção de dois ou 
mais conjuntos, o que significa que ele retornará um novo conjunto contendo apenas 
os elementos que estão presentes em todos os conjuntos envolvidos na operação.
"""