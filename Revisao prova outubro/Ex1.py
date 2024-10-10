lista = []
lista.append(float(input("Digite um valor para isso para lista: ")))
maior = lista[0]
menor = lista[0]
for i in range (1,5):
    lista.append(float(input("Digite um valor para isso para lista: ")))
    if lista[i] > maior:
        maior = lista[i]
    if lista[i] < menor:
        menor = lista[i]

print(lista)
print(maior, " ", menor)