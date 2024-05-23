num = int(input("Digite um numero: "))
fatorial = num
for i in range(1, num):
    fatorial = i * fatorial
print(f"{num}! = {fatorial}")