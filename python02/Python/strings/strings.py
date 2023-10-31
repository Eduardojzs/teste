# in é usado para verificar se a presença da frase em listas, tuplas ou str

frase = 'olá mundo'

print('mundo' in  frase)

# strip usamos para remover espaço de uma string
frase2 = '     olá mundo       '

print(frase.strip())

frase3 = 'olá, como vai você?'

palavras = frase3.split()#divide a frase em palavras usando o espaço em branco como separador

print(palavras)


palavras = ['olá', 'como', 'vai', 'você?']
frase4 = ''.join(palavras)
print(frase4)