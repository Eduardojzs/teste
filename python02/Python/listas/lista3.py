"""
Exercício: Operações Básicas com Listas

Objetivo: Familiarizar-se com operações fundamentais em listas, como 
adicionar, remover elementos, concatenar listas, repetir e verificar a presença de um item.

Instruções:

    1. Comece com uma lista vazia chamada animais.

    2. Adicione os seguintes animais à lista usando o método 
    append(): "gato", "cachorro" e "pássaro".

    3. Insira "peixe" na segunda posição da lista usando 
    o método insert().

    4. Remova "gato" da lista usando o método remove().

    5. Remova o último animal da lista usando o método pop() e armazene-o 
    em uma variável chamada animal_removido.

    6. Crie uma segunda lista chamada novos_animais com os 
    valores "tartaruga" e "hamster".

    7. Concatene as duas listas (animais e novos_animais) usando o 
    operador + e armazene o resultado na lista todos_animais.

    8. Duplique os elementos da lista todos_animais usando o 
    operador * e armazene o resultado em animais_duplicados.

    9. Verifique se "cachorro" está na lista todos_animais usando o 
    operador in e imprima o resultado.
"""
animais = []
animais.append("gato")
animais.append("cachorro")
animais.append("Pássaro")
print(animais)

print()
animais.insert(1, "peixe")
print(animais)
print()
animais.remove("gato")
print(animais)
print()

animais_removido = animais.pop()
print(animais_removido)
print()

print(animais)
print()

novos_animais = ["tartaruga", "hamster"]
print(novos_animais)
print()
todos_animais = animais + novos_animais

print(todos_animais)
print()

animais_duplicado = todos_animais*2

print(animais_duplicado)
print()

if "cachorro" in todos_animais:
    print('Cachorro esta na lista')

else:
    print('cachorro não esta!')