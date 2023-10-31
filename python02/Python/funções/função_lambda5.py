"""
Suponhamos que queremos filtrar uma lista de nomes e obter 
apenas aqueles que são exatamente "Alice".

Problema:
Dada uma lista de nomes, filtre-a para obter apenas as entradas que são "Alice".
"""

# Lista original de nomes
nomes = ["Alice", "Bob", "Anna", "Charlie", "Alex", "Tom", "Alice"]

# Usando filter() e lambda para obter apenas as entradas que são "Alice"
nomes_Alice = list(filter(lambda nome: nome == "Alice", nomes))

print(nomes_Alice)  # Saída: ['Alice', 'Alice']

"""
Explicação:
A função lambda lambda nome: nome == "Alice" compara cada entrada 
da lista nomes com a string "Alice". Se a entrada for exatamente igual 
a "Alice", a função retorna True; caso contrário, retorna False. A função 
filter() pega esses valores True e False e inclui apenas as entradas que 
retornam True no resultado final.
"""