A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print("Matriz A\n")
for linha in range(3):

    for coluna in range(3):

        

        print(f"{A[linha] [coluna]}", end=" ")

    print()
print()

B = [[10, 11, 12], [13, 14, 15], [16,17,18]]

print("Matriz B\n")

for linha in range(3):

    for coluna in range(3):

        print(f"{B[linha][coluna]}", end=" ")
    print()    


C = [[0,0,0], [0,0,0], [0,0,0]]
print()
print("Matriz C\n")

for linha in range(3):

    for coluna in range(3):

        print(f"{C[linha][coluna]}", end=" ")
    print()    
print()

print("Matriz de Subtração\n")
for linha in range(3):

    for coluna in range(3):

        C[linha][coluna] = A [linha][coluna] - B[linha][coluna]

        print(f"{C[linha][coluna]}", end=" ")
    print()  

print()
print("Matriz de soma\n")
for linha in range(3):

    for coluna in range(3):

        C[linha][coluna] = A [linha][coluna] + B[linha][coluna]

        print(f"{C[linha][coluna]}", end=" ")
    print()  
print()


soma_na_diagonal = 0

for i in range(3):

    soma_na_diagonal+= B[i][i]
print()

print(soma_na_diagonal)