import numpy as np
tamanho = 6
vetor = np.zeros(tamanho)
for i in range(tamanho):
    vetor[i] = float(input(f'Informe um valor para V[{i}]: '))
for i in range (tamanho-1, -1, -1):
    print(vetor[i])