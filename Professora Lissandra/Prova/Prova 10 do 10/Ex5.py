import numpy as np
# np.set_printoptions(legacy='1.25')
n = 3
matriz = np.zeros((n,n))
vetor = np.zeros(n)

for i in range (0,n):
    vetor[i] = int(input('Digite um número: '))

for l in range(0, len(matriz)):
    for c in range (0, len(matriz)):
        matriz[l][c] = int(input('Digite um número: '))

for l in range(0, n):
    for c in range (0, len(matriz)):
        matriz[l][c] *= vetor[l] 
print("Matriz 3x3: \n", matriz)