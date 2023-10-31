"""
Exercício: Palavras com Mais de 4 Letras

Objetivo: Solicite ao usuário uma lista de palavras e, em 
seguida, exiba apenas as palavras que têm mais de 4 letras.

Instruções:

    1. Peça ao usuário que insira palavras separadas 
    por vírgula (por exemplo, ["casa","carro","sol","árvore"]).
    
    2. Use um loop for para iterar sobre essa lista de palavras.
    
    3. Dentro do loop, verifique o comprimento de cada palavra.
    
    4. Se a palavra tiver mais de 4 letras, imprima-a.

Após concluir o exercício, se o usuário inserir "casa,carro,sol,árvore", a saída deve ser:

carro
árvore

"""

# lista de palavras
palavras = ["casa","carro","sol","árvore", "ovo", "professor", "aluno"]

# Itera sobre a lista de palavras
for palavra in palavras:
    
    # Verifica se a palavra tem mais de 4 letras
    if len(palavra) > 4:
        
        # Imprime a palavra
        print(palavra)



