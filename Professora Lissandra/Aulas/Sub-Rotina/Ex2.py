import numpy as np

def somarMatriz(matriz):
    soma = 0
    for l in range(len(matriz)):
        for c in range(len(matriz[l])):
            soma += matriz[l][c]
    return soma

n = 5
matriz = np.zeros((n,n))


for l in range(len(matriz)):
    for c in range(len(matriz[l])):
        matriz[l][c] = int(input("Informe valores para a matriz: "))


print(somarMatriz(matriz))
