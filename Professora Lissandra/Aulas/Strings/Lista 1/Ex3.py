x = []
z = []
soma = []
for i in range (0,5):
    num = int(input("Digite um numero: "))
    x.append(num)

print("Próxima lista")

for i in range (0,5):
    num = int(input("Digite um numero: "))
    z.append(num)

for i in range (0, 5):
    valor = x[i] + z[i]
    soma.append(valor)
print(soma)