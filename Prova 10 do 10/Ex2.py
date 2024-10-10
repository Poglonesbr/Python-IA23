import numpy as np  

lista = np.zeros(5)
contrario = np.zeros(len(lista))

for i in range(0, len(lista)):
    lista[i] = int(input('Digite um número: '))

for i in range(0,len(lista)):

    contrario[i] *= (-1)
    contrario[i] = lista[(len(lista)-1) - i]

print(f'Contrário: {contrario * -1}')

