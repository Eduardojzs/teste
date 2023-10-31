matriz_aluno = []

for l in range(3):

    nome = input(f'Digite nome do aluno {l +1}: ')


    nota = [] 

    for c in range(4):

        notas =input(f'Digite Nota {c + 1} do aluno {nome}: ')

        nota.append(notas)
    matriz_aluno.append([nome] + notas)


for aluno in matriz_aluno:

    nome= aluno[0]
    notas = aluno [1:]
    media = sum(notas)/4

    print("\n", + "*" * 40)
    print(f'nome: {nome}')
    print(f'Notas: {notas}')
    print(f'Médoa: {media}')
