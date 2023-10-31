A = [[1,2,3,4], [5,6,7,8], [9,10,11,12],[13,14,15,16]]

for l in range(4):

    for c in range(4):

        print(f'{A[l][c]}', end=' ')
    print()    


coluna_especifica = 2
soma_da_coluna = 0


for l in range(4):

    soma_da_coluna+= A[l][coluna_especifica]
print(f'Posição da coluna [{coluna_especifica}] é a soma {soma_da_coluna}')    

linha_especifica = 2
soma_da_linha = 0

for c in range(4):

    soma_da_linha += A[linha_especifica][c]

print(f'Posição da coluna [{linha_especifica}] é a soma {soma_da_linha}')   