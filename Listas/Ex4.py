x = [0, 0, 0, 0, 0]
x[0] = int(input("Digite um numero: "))
maior = x[0]
for i in range (1, 5):
    if maior < x[i]:
        maior = x[i]
    x[i] = int(input("Digite um numero: "))
   
print(maior)