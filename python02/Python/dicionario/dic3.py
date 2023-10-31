"""
Operações Básicas com Dicionários
        Adicionando itens
        Atualizando itens
        Removendo itens (del, pop(), popitem())
        Copiando dicionários (copy(), dict())
"""

#Operações Básicas com Dicionários

#Exemplo Prático:

#Suponhamos que temos um dicionário que representa um produto em 
#um e-commerce. Vamos realizar várias operações 
#para adicionar, atualizar, remover e copiar informações sobre o produto.

# Dicionário inicial do produto
# Inicialização de um dicionário chamado 'produto' com cinco pares chave-valor
produto = {
    "id": 12345,                  # Chave 'id' com o valor numérico 12345
    "nome": "Camisa Polo",        # Chave 'nome' com o valor "Camisa Polo"
    "cor": "Vermelho",            # Chave 'cor' com o valor "Vermelho"
    "preco": 49.90,               # Chave 'preco' com o valor numérico 49.90
    "estoque": 100                # Chave 'estoque' com o valor numérico 100
}

# 1. Adicionando itens ao dicionário 'produto'

# Adicionando a chave 'marca' com o valor "FashionBrand"
produto["marca"] = "FashionBrand"

# Adicionando a chave 'desconto' com o valor numérico 10 (representa uma porcentagem)
produto["desconto"] = 10

# Imprimindo o dicionário 'produto' após a adição dos novos itens
print("Após adicionar itens:", produto)

# 2. Atualizando itens

produto["preco"] = 59.90  # alterando o preço
produto["desconto"] = 15  # atualizando o valor do desconto

print("\nApós atualizar itens:", produto)

# 3. Removendo itens (del, pop(), popitem())

del produto["desconto"]  # remove o item "desconto" do dicionário

# Usando pop() para remover item por chave
cor_removida = produto.pop("cor")
print(f"\nCor removida: {cor_removida}")

# Usando popitem() para remover o último item inserido
item_removido = produto.popitem()
print("Item removido:", item_removido)

print("\nApós remover itens:", produto)

#4. Copiando dicionários (copy(), dict())

# Método copy()
produto_copia_1 = produto.copy()

# Método dict()
produto_copia_2 = dict(produto)

print("\nCópias do produto:")
print("Cópia 1:", produto_copia_1)
print("Cópia 2:", produto_copia_2)

"""
Neste exemplo, realizamos várias operações básicas em um dicionário. 

É importante entender como manipular dicionários efetivamente, pois são 
uma estrutura de dados fundamental em Python.
"""

"""
Método copy():
O método copy() é uma função integrada em objetos de dicionário em 
Python. Ele cria uma cópia superficial (shallow copy) do dicionário. 
Isso significa que os valores dos itens (pares chave-valor) são 
copiados, mas se esses valores forem objetos mutáveis (como listas 
ou outros dicionários), eles ainda serão compartilhados entre o 
dicionário original e a cópia.

Função dict() (construtor de dicionário):
A função dict() pode ser usada para criar uma cópia rasa 
(shallow copy) ou profunda (deep copy) do dicionário, dependendo 
de como ela é usada. Ao passar outro dicionário como argumento 
para dict(), você cria uma cópia rasa. No entanto, se você quiser 
criar uma cópia profunda, precisará usar a biblioteca copy e o 
método deepcopy().

"""