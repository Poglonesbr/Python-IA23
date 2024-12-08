import numpy as np  

N = 6
matriz = np.zeros((N , N))

provisorial = np.zeros(N)
provisoriac = np.zeros(N)

for l in range(len(matriz)):
    for c in range(len(matriz[l])):
        matriz[l][c] = int(input("Informe valores para a matriz: "))
        if l == 1:
            provisorial[c] = matriz[1][c]

        if c == 3:
            provisoriac[l] = matriz[l][3]

print("Matriz 6x6: ", matriz)
for l in range(len(matriz)):
    for c in range(len(matriz[l])):
            if l == 1:         
                matriz[1][c] = matriz[4][c]
            if c == 3:
                matriz[l][3] = matriz[l][5]
            if l == 4:
                matriz[4][c] = provisorial[c]           
            if c == 5:    
                matriz[l][5] = provisoriac[l]


print("Matriz 6x6: ", matriz)
