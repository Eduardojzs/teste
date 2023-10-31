"""
Exercício sobre Dicionários Aninhados

Objetivo: Você possui um dicionário que contém informações 
sobre carros em um estacionamento, incluindo a marca, modelo e dono 
do carro. Seu objetivo é acessar e modificar algumas informações nesse dicionário.

Dicionário fornecido:

estacionamento = {
    "A1": {
        "marca": "Toyota",
        "modelo": "Corolla",
        "dono": "Sr. Silva"
    },
    "B2": {
        "marca": "Honda",
        "modelo": "Civic",
        "dono": "Dona Maria"
    },
    "C3": {
        "marca": "Ford",
        "modelo": "Mustang",
        "dono": "Sr. Jorge"
    }
}


Onde as chaves (A1, B2, C3) representam as vagas no estacionamento.

Instruções:

    1. Acesse e imprima o modelo do carro estacionado na vaga "B2".
    
    2. Altere o dono do carro na vaga "A1" para "Sra. Lúcia".
    
    3. Adicione um novo carro na vaga "D4" com as seguintes 
        informações: marca "Chevrolet", modelo "Onix", dono "Sr. Roberto".
        
    4. Acesse e imprima a marca do carro que agora pertence à "Sra. Lúcia".
"""
#Solução 

# Definindo um dicionário chamado 'estacionamento'.
# Cada chave do dicionário representa um espaço no estacionamento, 
#e o valor associado é outro dicionário que contém detalhes do carro 
#estacionado naquela vaga.

# Inicializando um dicionário chamado 'estacionamento' com informações de veículos.
estacionamento = {
    "A1": {               # Vaga "A1" do estacionamento.
        "marca": "Toyota",  # Marca do carro estacionado na vaga "A1".
        "modelo": "Corolla", # Modelo do carro estacionado na vaga "A1".
        "dono": "Sr. Silva"  # Dono do carro estacionado na vaga "A1".
    },
    "B2": {               # Vaga "B2" do estacionamento.
        "marca": "Honda",   # Marca do carro estacionado na vaga "B2".
        "modelo": "Civic",  # Modelo do carro estacionado na vaga "B2".
        "dono": "Dona Maria" # Dono do carro estacionado na vaga "B2".
    },
    "C3": {               # Vaga "C3" do estacionamento.
        "marca": "Ford",    # Marca do carro estacionado na vaga "C3".
        "modelo": "Mustang", # Modelo do carro estacionado na vaga "C3".
        "dono": "Sr. Jorge"  # Dono do carro estacionado na vaga "C3".
    }
}

# 1. Acesse e imprima o modelo do carro estacionado na vaga "B2".
print("1. Modelo do carro na vaga B2:", estacionamento["B2"]["modelo"])

# 2. Altere o dono do carro na vaga "A1" para "Sra. Lúcia".
estacionamento["A1"]["dono"] = "Sra. Lúcia"
print(f"2. Modificando dono do carro em A1: {estacionamento['A1']['dono']}")

# 3. Adicione um novo carro na vaga "D4" com as seguintes 
# informações: marca "Chevrolet", modelo "Onix", dono "Sr. Roberto".

# Atualizando ou adicionando um novo carro ao dicionário 
#'estacionamento' na posição "D4".
estacionamento["D4"] = {
    "marca": "Chevrolet",  # Define a marca do carro como "Chevrolet".
    "modelo": "Onix",      # Define o modelo do carro como "Onix".
    "dono": "Sr. Roberto"  # Define o dono do carro como "Sr. Roberto".
}


# Exibindo as informações do carro que foi estacionado na vaga D4.
print("\n3. Adicionando carro em D4", estacionamento["D4"])


# 4. Acesse e imprima a marca do carro que agora pertence à "Sra. Lúcia".

print("\n4. Acessando marca do carro da Sra. Lúcia")

# Para cada par 'vaga' e 'carro' no dicionário 'estacionamento'
for vaga, carro in estacionamento.items():
    
    # Verifica se o campo "dono" do dicionário 'carro' é igual a "Sra. Lúcia"
    if carro["dono"] == "Sra. Lúcia":
        
        # Imprime a marca do carro que pertence à Sra. Lúcia
        print(f"Marca do carro da Sra. Lúcia: {carro['marca']}")
        
        # Encerra o loop após encontrar o carro da Sra. Lúcia
        break

        