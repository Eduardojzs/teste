"""
Dicionários Aninhados
        Acessando e modificando valores em dicionários aninhados
"""

#Dicionários Aninhados

#Um dicionário aninhado é um dicionário dentro de outro dicionário. 
#É uma forma útil de representar, por exemplo, dados hierárquicos ou estruturados.

#Exemplo Prático:

#Imagine que você está administrando uma escola e quer armazenar informações 
#sobre seus alunos, incluindo suas notas em diferentes matérias. Um dicionário aninhado 
#seria útil nesse cenário.

# Dicionário de alunos com notas em diferentes matérias

# Definindo um dicionário chamado 'alunos'.
# Cada chave do dicionário representa o nome de um aluno, e o valor 
# associado é outro dicionário que contém as notas do aluno nas diferentes matérias.

# Inicializando um dicionário chamado 'alunos' para armazenar as notas 
#dos alunos em diferentes matérias.

alunos = {
    "João": {          # Informações sobre o aluno chamado "João".
        "Matemática": 8.5,  # Nota de João em Matemática.
        "Português": 9.0,   # Nota de João em Português.
        "História": 7.5     # Nota de João em História.
    },
    "Maria": {         # Informações sobre a aluna chamada "Maria".
        "Matemática": 9.5,  # Nota de Maria em Matemática.
        "Português": 8.0,   # Nota de Maria em Português.
        "Geografia": 8.7    # Nota de Maria em Geografia.
    },
    "Pedro": {         # Informações sobre o aluno chamado "Pedro".
        "Matemática": 7.0,  # Nota de Pedro em Matemática.
        "Português": 7.5,   # Nota de Pedro em Português.
        "História": 8.0,    # Nota de Pedro em História.
        "Geografia": 9.0    # Nota de Pedro em Geografia.
    }
}

# Acessando notas do João em Matemática
nota_joao_matematica = alunos["João"]["Matemática"]
print(f"Nota do João em Matemática: {nota_joao_matematica}")

# Modificando a nota de Maria em Geografia
alunos["Maria"]["Geografia"] = 9.2
print(f"Nota atualizada de Maria em Geografia: {alunos['Maria']['Geografia']}")

# Adicionando um nota de Química para Pedro
alunos["Pedro"]["Química"] = 8.8
print(f"Nota do Pedro em Química: {alunos['Pedro']['Química']}")

"""
Neste exemplo, temos um dicionário alunos, onde cada chave é o nome 
de um aluno e o valor associado é outro dicionário que contém as notas 
desse aluno em diferentes matérias. Ao usar chaves de maneira hierárquica, 
podemos acessar e modificar facilmente valores em dicionários aninhados.
"""