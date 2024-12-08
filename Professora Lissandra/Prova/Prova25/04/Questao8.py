num1 = int(input("Digite um numero: "))
num2 = int(input("Digite um numero: "))
num3 = int(input("Digite um numero: "))

if (num1 < num2) and (num1 < num3):
    menor = num1
    print(menor)
    if(num2 < num3):
        print(num2, "\n", num3)
    else:
        print(num3, "\n", num2)

elif (num2 < num1) and (num2 < num3):
    menor = num2
    print(menor)
    if(num1 < num3):
        print(num1, "\n", num3)
    else:
        print(num3, "\n", num1)

elif (num3 < num1) and (num3 < num2):
    menor = num3
    print(menor)
    if(num2 < num1):
        print(num2, "\n", num1)
    else:
        print(num1, "\n", num2)
    