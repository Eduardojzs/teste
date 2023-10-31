"""""
Exercicio
Crie um algoritimo que solicite a senha a 
usúario é so saia quando a senha for digitada correta

"""
while True:

    senha = 123456789
    usuario = int(input('Digite uma senha:. '))

    if senha == usuario:
        print('Entrando!')
        break
    else:
        print('Senha Errada!')
