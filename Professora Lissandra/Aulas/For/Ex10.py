negativo = 0
soma = 0
for i in range(0, 20):
    x = int(input("Digite um numero: "))
    if x < 0:
        negativo += 1
    else:
        soma += x
print("A quantidade negativos é:", negativo)
print("A soma de positivos é:", soma)