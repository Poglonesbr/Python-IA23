n1 = int(input("Digite um numero: "))
n2 = int(input("Digite um numero: "))
n3 = int(input("Digite um numero: "))
maior = n1
menor = n2
meio = n3
if n1 >= n2 and n1 >= n3:
    maior = n1
    if n3 >= n2:
        menor = n2
        meio = n3
    else:
        menor = n3
        meio = n2
elif n2 >= n1 and n2 >= n3:
    maior = n2
    if n3 >= n1:
        menor = n1
        meio = n3
    else:
        menor = n3
        meio = n1
elif n3 >= n2 and n3 >= n1:
    maior = n3
    if n1 >= n2:
        menor = n2
        meio = n1
    else:
        menor = n1
        meio = n2

print(f"{maior}, {meio}, {menor}")