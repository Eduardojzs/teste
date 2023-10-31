#Solução:

# Inicialização de um dicionário chamado 'filme' para representar características de um filme específico
filme = {
    "titulo": "Inception",                       # Chave 'titulo' com o valor "Inception"
    "diretor": "Christopher Nolan",              # Chave 'diretor' com o valor "Christopher Nolan"
    "ano": 2010,                                # Chave 'ano' com o valor numérico 2010
    "genero": "Ficção Científica"                # Chave 'genero' com o valor "Ficção Científica"
}

# 1. Demonstração dos métodos keys(), values(), e items() em dicionários
print("\n1. keys(), values(), e items()")

# Extraindo e imprimindo as chaves do dicionário 'filme' usando o método keys()
print("Chaves:", list(filme.keys()))

# Extraindo e imprimindo os valores do dicionário 'filme' usando o método values()
print("Valores:", list(filme.values()))

# Extraindo e imprimindo os pares chave-valor do dicionário 'filme' usando o método items()
print("Itens:", list(filme.items()))


# 2. Demonstração do método clear() para limpar o conteúdo de um dicionário
print("\n2. clear()")

# Fazendo uma cópia do dicionário 'filme' e armazenando em 'filme_copia'
filme_copia = filme.copy()

# Usando o método clear() para limpar todos os itens de 'filme_copia'
filme_copia.clear()
print("\nDicionário após clear():", filme_copia)


# 3. Demonstração do método setdefault() para obter o valor de uma chave ou definir um padrão se ela não existir
print("\n3. setdefault()")

# Tentando obter a chave 'elenco' no dicionário 'filme'; se não existir, ela será criada com o valor fornecido
elenco = filme.setdefault("elenco", ["Leonardo DiCaprio", "Ellen Page"])
print("\nElenco:", elenco)
print("Dicionário após setdefault():", filme)


# 4. Demonstração do método update() para adicionar ou atualizar itens no dicionário
print("\n4. update()")

# Definindo um novo dicionário com informações adicionais
informacoes_adicionais = {
    "duracao": 148,
    "idioma": "Inglês"
}

# Atualizando o dicionário 'filme' com as informações de 
#'informacoes_adicionais'
filme.update(informacoes_adicionais)
print("\nDicionário após update():", filme)

# 5. Demonstração do método fromkeys() para criar um novo dicionário com chaves especificadas e um valor padrão
print("\n5. fromkeys()")

# Lista de chaves que queremos usar para criar um novo dicionário
chaves = ["nome", "idade", "ocupacao"]

# Criando um novo dicionário usando as chaves fornecidas com o valor "Desconhecido"
perfil = dict.fromkeys(chaves, "Desconhecido")
print("\nDicionário criado com fromkeys():", perfil)