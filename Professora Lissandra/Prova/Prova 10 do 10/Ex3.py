import numpy as np  

lista = np.zeros(100)
pares = 0
impares = 0
quant_imp = 0

for i in range(0, len(lista)):
    lista[i] = int(input('Digite um número: '))

    if lista[i] % 2 == 0:
        pares += 1
    else:
        impares += lista[i]
        quant_imp += 1
impares = impares / quant_imp 

print(f"A quantidade de valores pares é: {pares}")
print(f"A media de valores impares é: {impares}")
