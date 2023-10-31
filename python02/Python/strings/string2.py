#metodos para strings



# upper transforma a frase tudo em maiusculo
texto = 'ola Mundo!'
novo_texto = texto.upper()
print(novo_texto)

# lower faz texto fica em minusculo 
texto2 = 'OLA MUNDO'
novo_texto2 = texto2.lower()

print(novo_texto2)
# Tranasforma a primeira letra em mausculo
texto_capitalize = texto.capitalize()
print(texto_capitalize)

# Conta quantas letras tem da sua escolha
ocorrencia = texto.count('o')
print(ocorrencia)

#replace muda um palavra do texto ou texto todo
texto_substituido = texto.replace(texto, 'Ei Jhow')
print(texto_substituido)