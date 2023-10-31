"""
Métodos de Dicionários
        keys(), values(), e items()
        clear()
        setdefault()
        update()
        fromkeys()
"""

#Exemplo Prático:

#Vamos supor que estamos administrando uma livraria e 
#temos um dicionário que representa um livro específico. 

#Usaremos diferentes métodos de dicionário para manipular e 
#extrair informações sobre esse livro.

# Dicionário representando um livro
# Inicialização de um dicionário chamado 'livro' para 
# representar características de um livro específico
livro = {
    "titulo": "O Pequeno Príncipe",               # Chave 'titulo' com o valor "O Pequeno Príncipe"
    "autor": "Antoine de Saint-Exupéry",          # Chave 'autor' com o valor "Antoine de Saint-Exupéry"
    "ano": 1943,                                  # Chave 'ano' com o valor numérico 1943
    "editora": "Reynal & Hitchcock",              # Chave 'editora' com o valor "Reynal & Hitchcock"
    "preco": 20.5                                 # Chave 'preco' com o valor numérico 20.5
}


# 1. keys(), values(), e items()
print("\n1. keys(), values(), e items()")
print("Chaves do dicionário:", list(livro.keys())) # Retorna todas as chaves
print("Valores do dicionário:", list(livro.values())) # Retorna todos os valores
print("Itens do dicionário:", list(livro.items())) # Retorna pares chave-valor

# 2. clear()
print("\n2. clear()")
copia_livro = livro.copy()
copia_livro.clear() # Remove todos os itens do dicionário
print("\nDicionário após clear():", copia_livro)

# 3. setdefault()
# Retorna o valor da chave especificada. Se a chave não existir, insere a 
#chave com um valor especificado (ou padrão se nenhum valor for fornecido)
print("\n3. setdefault()")
isbn = livro.setdefault("ISBN", "978-3-16-148410-0")
print("\nISBN:", isbn)
print("Dicionário após setdefault():", livro)

# 4. update()
# Atualiza o dicionário com elementos de outro dicionário ou de um iterável com pares chave-valor
print("\n4. update()")

# Inicialização de um dicionário chamado 'atualizacoes' contendo os itens a serem 
#atualizados ou adicionados ao dicionário 'livro'
atualizacoes = {
    "preco": 18.5,              # Chave 'preco' com o novo valor numérico 18.5
    "formato": "Capa dura"     # Chave 'formato' com o valor "Capa dura" (esse é um novo item que será adicionado ao dicionário 'livro')
}

# Utilização do método .update() do dicionário 'livro' para atualizar (ou adicionar) os itens a partir do dicionário 'atualizacoes'
livro.update(atualizacoes)

print("\nDicionário após update():", livro)

# 5. fromkeys()
# Retorna um novo dicionário com chaves de um iterável e valor definido
print("\n5. fromkeys()")

# Lista de chaves que queremos usar para criar um novo dicionário
chaves = ["titulo", "autor", "sinopse"]

# Utilização do método .fromkeys() da classe dict para criar um novo dicionário ('novo_livro').
# Todas as chaves especificadas na lista 'chaves' terão o valor "Desconhecido".
novo_livro = dict.fromkeys(chaves, "Desconhecido")

# Impressão do dicionário recém-criado 'novo_livro'.
print("\nDicionário criado com fromkeys():", novo_livro)