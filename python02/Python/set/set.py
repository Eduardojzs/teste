"""
Set (conjuntos):

    Definição e Características
        - Um "set" é uma coleção desordenada de elementos únicos. Isso 
        significa que não permite duplicatas.
        
        Sets são mutáveis, mas os elementos contidos neles devem 
        ser imutáveis (por exemplo, números, strings e tuplas).

    Criando um Conjunto
        Usando chaves: s = {1, 2, 3}
        Usando a função set(): s = set([1, 2, 3])

    Adicionando e Removendo Elementos
        add(): Adiciona um elemento ao conjunto.
        remove(): Remove um elemento do conjunto. Gera um erro se o elemento não existir.
        discard(): Remove um elemento do conjunto se ele existir.
        pop(): Remove e retorna um elemento do conjunto. Como os sets são desordenados, você não sabe qual item será removido.
        clear(): Remove todos os elementos do conjunto.

    Operações com Conjuntos
        União: s1 | s2 ou s1.union(s2)
        Intersecção: s1 & s2 ou s1.intersection(s2)
        Diferença: s1 - s2 ou s1.difference(s2)
        Diferença simétrica (elementos que estão em um conjunto ou no outro, mas não em ambos): s1 ^ s2 ou s1.symmetric_difference(s2)
        Subset (subconjunto): s1.issubset(s2)
        Superset (superconjunto): s1.issuperset(s2)

    Outras Funções e Métodos
        len(): Retorna o número de elementos no conjunto.
        in: Verifica a existência de um elemento no conjunto.
        copy(): Retorna uma cópia do conjunto.

    Imutabilidade e Frozensets
        Como mencionado, os elementos de um set devem ser imutáveis. No entanto, o próprio set é mutável. Se você precisar de um conjunto imutável, pode usar um frozenset.

    Aplicações Práticas
        Sets são frequentemente usados para remover duplicatas de uma lista.
        Eles são úteis para testar a pertença de um elemento.
        São utilizados em operações matemáticas de conjunto, como união, interseção e diferença.

    Limitações
        Conjuntos não suportam indexação, fatiamento ou outras operações de sequência.
        Não podem conter elementos duplicados.

"""
"""
Definição e Características
        - Um "set" é uma coleção desordenada de elementos únicos. Isso 
        significa que não permite duplicatas.
        
        Sets são mutáveis, mas os elementos contidos neles devem 
        ser imutáveis (por exemplo, números, strings e tuplas).
"""

#Exemplo 1: Removendo Duplicatas de uma Lista

#Uma aplicação comum do set é a remoção de duplicatas de uma lista.

# Dada a seguinte lista:
lista = [1, 2, 2, 3, 4, 4, 5, 5, 5]
print(lista)

# Convertendo a lista para um conjunto, as duplicatas são automaticamente removidas
conjunto = set(lista)
print(conjunto)  # Saída: {1, 2, 3, 4, 5}

print()
#Exemplo 2: Verificando a Imutabilidade dos Elementos

#Enquanto o próprio conjunto é mutável (o que significa que você pode 
#adicionar ou remover elementos dele), os elementos dentro do conjunto devem ser imutáveis.

# Criando um conjunto com elementos imutáveis
conjunto = {1, 2, "Python", (4, 5)}
print(conjunto)  # Saída: {1, (4, 5), 2, 'Python'}

"""
Em Python, um conjunto é uma coleção não ordenada de 
elementos únicos. Isso significa que a ordem dos elementos 
dentro de um conjunto não é garantida. Quando você imprime um 
conjunto, os elementos podem ser exibidos em qualquer ordem, pois 
a estrutura subjacente de dados (geralmente uma tabela hash) não 
mantém uma ordem específica.

Os elementos {1, 2, "Python", (4, 5)} foram inseridos no 
conjunto, mas a ordem em que eles aparecem na saída não 
é previsível. A ordem que você vê 1, (4, 5), 2, 'Python' pode ser 
resultado da implementação interna do conjunto ou de como o Python 
decide exibir os elementos no momento da impressão.

Portanto, não há um motivo específico para o texto "Python" ter 
ido para o final. Trata-se apenas de como o Python decidiu exibir 
os elementos no conjunto no momento da impressão, e essa ordem pode 
variar entre diferentes execuções ou versões do Python.
"""

# Tentando adicionar uma lista (que é mutável) a um conjunto resultará em um erro
try:
    conjunto.add([6, 7])
except TypeError as e:
    print(f"Erro: {e}")  # Saída: Erro: unhashable type: 'list'

"""
Neste exemplo, ao tentar adicionar uma lista ao conjunto, recebemos 
um erro "unhashable type". Isso acontece porque os elementos dentro de 
um conjunto devem ser de um tipo que não pode ser alterado após serem 
criados (ou seja, imutáveis), como números, strings e tuplas. Por outro 
lado, listas e dicionários são mutáveis e, portanto, não podem ser 
adicionados a conjuntos.

Esses exemplos demonstram algumas das características fundamentais 
dos sets em Python: sua capacidade de armazenar elementos únicos e 
a exigência de que esses elementos sejam imutáveis.
"""

"""
Criando um Conjunto
        Usando chaves: s = {1, 2, 3}
        Usando a função set(): s = set([1, 2, 3])
"""

#Criando um conjunto usando chaves

#1. Usando chaves:
# Criando um conjunto usando chaves
s_chaves = {1, 2, 3, 3, 4}
print(s_chaves)  # Saída: {1, 2, 3, 4}

# Note que adicionamos o número 3 duas vezes ao conjunto acima, mas na saída ele aparece apenas uma vez.
# Isso ocorre porque os conjuntos não permitem elementos duplicados.


#Criando um conjunto usando a função set()

#2. Usando a função set():

# Criando um conjunto a partir de uma lista usando a função set()
s_funcao = set([1, 2, 3, 3, 4])
print(s_funcao)  # Saída: {1, 2, 3, 4}

# Novamente, note que o número 3 foi adicionado duas vezes, mas aparece apenas uma vez na saída.

#Comparando os dois métodos

# Vamos verificar se os conjuntos criados pelos dois métodos são iguais
print(s_chaves == s_funcao)  # Saída: True

# Como esperado, ambos os métodos produzem o mesmo resultado.

"""
Ambas as abordagens são válidas para criar conjuntos em Python, mas 
o uso de chaves é mais conciso e geralmente preferido quando você já conhece 
os elementos que deseja incluir no conjunto. Por outro lado, a função set() 
é versátil e pode ser usada para converter outras estruturas de dados, como 
listas ou tuplas, em conjuntos.

"""