"""
Adicionando e Removendo Elementos
        add(): Adiciona um elemento ao conjunto.
        remove(): Remove um elemento do conjunto. Gera um erro se o elemento não existir.
        discard(): Remove um elemento do conjunto se ele existir.
        pop(): Remove e retorna um elemento do conjunto. Como os sets 
        são desordenados, você não sabe qual item será removido.
        
        clear(): Remove todos os elementos do conjunto.
"""

#Vamos ao exemplo prático sobre a adição e remoção de elementos em um conjunto em Python:

s = {1, 2, 3, 4}
print(s)  # Saída: {1, 2, 3, 4}

#2. Usando add()

#Adiciona um elemento ao conjunto. Se o elemento 
#já existir, o conjunto não será alterado.
s.add(5)
print(s)  # Saída: {1, 2, 3, 4, 5}

s.add(3)  # Tentando adicionar um elemento que já existe
print(s)  # Saída: {1, 2, 3, 4, 5}

#3. Usando remove()

#Remove um elemento do conjunto. Se o elemento 
#não existir, gera um erro.

s.remove(5)
print(s)  # Saída: {1, 2, 3, 4}

# Tentando remover um elemento que não existe:
try:
    s.remove(50)
except KeyError as e:
    print(f"Erro: {e}")  # Saída: Erro: 5
    
#4. Usando discard()

#Remove um elemento do conjunto se ele existir. Se o 
#elemento não existir, nada acontece (não gera um erro).

s.discard(4)
print(s)  # Saída: {1, 2, 3}

s.discard(4)  # Tentando descartar um elemento que não existe
print(s)  # Saída: {1, 2, 3} - Nenhum erro é gerado


#5. Usando pop()

#Remove e retorna um elemento do conjunto. Como os sets 
#são desordenados, você não sabe qual item será removido.
elemento_removido = s.pop()
print(f"Elemento removido: {elemento_removido}")
print(s)  # Saída varia pois os sets são desordenados. Exemplo de saída: {2, 3}

#6. Usando clear()

#Remove todos os elementos do conjunto.
s.clear()
print(s)  # Saída: set()

"""
Esses exemplos ilustram como manipular elementos em um 
conjunto usando diferentes métodos. Cada um desses métodos tem 
sua própria utilidade, dependendo das necessidades específicas 
da operação ou aplicação.
"""