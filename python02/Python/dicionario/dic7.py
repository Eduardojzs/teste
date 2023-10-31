"""
Dicionários e Funções
        Passando dicionários como argumentos para funções
        Retornando dicionários de funções
"""

#Exemplo Prático: Dicionários e Funções

#Vamos criar um sistema simples de gestão de perfis de usuários:

#1. Passando dicionários como argumentos para funções:
#Suponha que temos um dicionário representando um perfil de usuário e 
#queremos exibir este perfil.

#2. Retornando dicionários de funções:
#Vamos criar uma função que pode criar um novo perfil de usuário 
#com base em informações fornecidas.

# Definição do dicionário do perfil do usuário

# Iniciando um dicionário chamado 'usuario'
usuario = {
    "nome": "João",
    "idade": 25,
    "email": "joao@email.com"
}

# 1. Passando dicionários como argumentos para funções

# Define uma função chamada 'exibir_perfil' que aceita um dicionário 'perfil' como parâmetro
def exibir_perfil(perfil):
    
    # Para cada par de chave-valor no dicionário 'perfil'
    for chave, valor in perfil.items():
        
        # Imprime a chave (formatada com a primeira letra maiúscula) e seu respectivo valor
        print(f"{chave.title()}: {valor}")

# Chama a função 'exibir_perfil' passando o dicionário 'usuario' como argumento
exibir_perfil(usuario)

# 2. Retornando dicionários de funções

# Definindo uma função chamada 'criar_perfil'
def criar_perfil(nome, idade, email):
    
    """Retorna um dicionário representando um perfil de usuário"""
    
    # Criando e retornando um dicionário com as informações do perfil do usuário
    return {
        "nome": nome,   # Chave: "nome", Valor: valor da variável 'nome'
        "idade": idade, # Chave: "idade", Valor: valor da variável 'idade'
        "email": email  # Chave: "email", Valor: valor da variável 'email'
    }

# Criando um novo perfil de usuário usando a função 'criar_perfil'
novo_usuario = criar_perfil("Ana", 30, "ana@email.com")

print("\nNovo Perfil Criado:")

# Exibindo o perfil do novo usuário
exibir_perfil(novo_usuario)