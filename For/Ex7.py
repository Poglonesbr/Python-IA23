num = int(input("Digite um numero: "))
maior = num
menor = num
for i in range(1, 10):
    num = int(input("Digite um numero: "))
    if num < menor:
        menor = num
    if num > maior:
        maior = num
print(maior, menor)