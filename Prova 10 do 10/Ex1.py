import numpy as np  

lista = np.zeros(8)
positivos = []
negativos = []

for i in range(0, len(lista)):
    lista[i] = int(input('Digite um número: '))
    if lista[i] > 0:
        positivos.append(lista[i])
    if lista[i] < 0:
        negativos.append(lista[i])

for x in range(0, len(lista)):
    print(f"Lista principal: Posição {x} {lista[x]}")
print(" ")
for x in range(0, len(positivos)):
    print(f"Lista positivos: Posição {x} {positivos[x]}")   
print(" ")    
for x in range(0, len(negativos)):
    print(f"Lista negativos: Posição {x} {negativos[x]}")       