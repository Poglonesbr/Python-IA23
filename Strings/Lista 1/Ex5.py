x = []
z = []
lista = []
for i in range (0,5):
    num = int(input("Digite um numero: "))
    x.append(num)

print("Próxima lista")

for i in range (0,5):
    num = int(input("Digite um numero: "))
    z.append(num)



for i in range (0, 5):
    lista.append(x[i])
    
for i in range (0,5):
    lista.append(z[i])

print(lista)