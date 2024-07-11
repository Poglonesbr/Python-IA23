x = [0, 0, 0, 0, 0]
z = 0
numerador = 0
for i in range (0, 5):
    x[i] = int(input("Digite um numero: "))
    z += x[i]
    numerador += 1
print(z/numerador)