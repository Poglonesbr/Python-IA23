matriz = [0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]

# Inserindo dados na matriz usando for.
for l in range(len(matriz)):
    for c in range(len(matriz[l])):
        matriz[l][c] = int(input("Informe valores para a matriz: "))
        
for l in range(len(matriz)):
    for c in range(len(matriz[l])):
        if c == l:
            print(matriz[l][c])