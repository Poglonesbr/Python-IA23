matriz = [0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]

# Inserindo dados na matriz usando for.
for c in range(len(matriz)):
    for l in range(len(matriz[c])):
        matriz[l][c] = int(input("Informe valores para a matriz: "))
print("Matriz 5x5: ", matriz)