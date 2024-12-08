x = []
z = []
multiplicacao = []
for i in range (0,5):
    num = int(input("Digite um numero: "))
    x.append(num)

print("Próxima lista")

for i in range (0,5):
    num = int(input("Digite um numero: "))
    z.append(num)

indice = 4

for i in range (0, 5):
    valor = x[i] * z[indice]
    multiplicacao.append(valor)
    indice -= 1
    


print(multiplicacao)