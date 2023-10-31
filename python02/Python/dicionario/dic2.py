"""
Acessando Itens do Dicionário
        Acessando valores usando chaves
        Método get()
        Verificando a existência de uma chave
"""
#Acessando Itens do Dicionário

#Exemplo Prático:

#Vamos supor que você tem um dicionário representando informações 
#sobre um smartphone. Queremos acessar certas informações usando diferentes métodos.

# Definindo o dicionário do smartphone
# Criação de um dicionário chamado 'smartphone' com cinco pares chave-valor
smartphone = {
    "marca": "Apple",             # Chave 'marca' com o valor "Apple"
    "modelo": "iPhone 12",        # Chave 'modelo' com o valor "iPhone 12"
    "cor": "Azul",                # Chave 'cor' com o valor "Azul"
    "capacidade": "128GB",        # Chave 'capacidade' com o valor "128GB"
    "sistema": "iOS"              # Chave 'sistema' com o valor "iOS"
}

# 1. Acessando valores usando chaves
# Imprimindo uma mensagem indicativa
print("Método direto:")

# Acessando e imprimindo o valor associado à chave 'marca' do dicionário 'smartphone'
print("Marca:", smartphone["marca"])  # Saída esperada: Apple
#print("Marca:", smartphone["camera"])

# Mas, se tentarmos acessar uma chave que não existe, receberemos um erro.
# Por exemplo, tentar acessar smartphone["camera"] lançaria um KeyError.

# 2. Método get()
print("\nUsando o método get():")
print("Modelo:", smartphone.get("modelo"))  # Saída: iPhone 12

# Se tentarmos acessar uma chave que não existe usando get(), ele retorna None por padrão.
# Porém, podemos especificar um valor padrão para ser retornado.
print("Câmera:", smartphone.get("camera")) 
print("Câmera:", smartphone.get("camera", "Informação não disponível"))  # Saída: Informação não disponível

#3. Verificando a existência de uma chave

# Imprimindo uma linha em branco e uma mensagem indicativa
print("\nVerificando chaves:")

#if - se
# Verificando se a chave 'sistema' está presente no dicionário 'smartphone'
if "sistema" in smartphone:
    
    # Se 'sistema' estiver presente, imprime o valor associado a essa chave
    print("O smartphone roda no sistema:", smartphone["sistema"])  # Saída esperada: iOS
    
else:
    
    # Se 'sistema' não estiver presente, imprime uma mensagem indicando isso
    print("Sistema operacional não especificado.")

# Verificando se a chave 'camera' está presente no dicionário 'smartphone'
if "camera" in smartphone:
    
    # Se 'camera' estiver presente, imprime o valor associado a essa chave
    print("Câmera:", smartphone["camera"])
    
else:
    
    # Se 'camera' não estiver presente, imprime uma mensagem indicando a ausência de informações sobre a câmera
    print("Informações da câmera não disponíveis.")  # Saída esperada: Informações da câmera não disponíveis.

    
"""
Neste exemplo, mostramos diferentes formas de acessar e verificar itens 
em um dicionário. É essencial entender esses métodos porque eles previnem erros 
ao tentar acessar chaves que podem não existir no dicionário.
"""
