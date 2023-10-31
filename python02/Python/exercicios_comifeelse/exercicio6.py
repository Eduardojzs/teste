"""
Exercício

Entrada para um Evento Exclusivo

Você foi convidado para um evento exclusivo. Para entrar, você deve 
atender a pelo menos uma das seguintes condições:

    Ter um convite VIP.
    Estar na lista de convidados.
    Ser um membro do clube.

    Execute o programa.
    
    Responda às perguntas fornecidas com 'sim' ou 'não'.
    O programa irá informar se você pode entrar no evento ou não.
    
    
    Bem-vindo(a) ao evento!
    Desculpe, você não pode entrar no evento.
    
"""
sim = True
não = None

print(' Bem-vindo(a) ao evento!')
print()
ter_um_convite_vip = input('Tem Convite vip? sim ou não: ')
print()
estar_na_lista_de_convidados = input('Esta com nome na lista? sim ou não: ') 
print()
ser_um_membro_clube = input('ser um membro na lista? sim ou não: ')
print()

if ter_um_convite_vip == 'sim':

    print('Entrada para um Evento Exclusivo')

elif estar_na_lista_de_convidados == 'sim':
    print('Entrada para um Evento Exclusivo')

elif ser_um_membro_clube == 'sim':
    print('Entrada para um Evento Exclusivo')
else:
    print('Desculpe, você não pode entrar no evento.')

# or usando or
"""""
# Verifica se o usuário atende a pelo menos uma das condições
if convite_vip == "sim" or na_lista  == "sim" or membro_clube == "sim":
                  
    # Se atender a pelo menos uma das condições, permite a entrada
    print("Bem-vindo(a) ao evento!")
                     
else:
    
    # Se não atender a nenhuma das condições, nega a entrada
    print("Desculpe, você não pode entrar no evento.")"""    