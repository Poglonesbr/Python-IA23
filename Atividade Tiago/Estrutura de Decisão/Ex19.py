from math import floor
num = int(input("Digite um número inteiro abaixo de 1000: "))


if num < 1000 and num > 0:
    centena = num // 100
    dezena = (num % 100) // 10
    unidade = num % 10

    print(f"{centena}", end="")
    if centena == 1:
        print(" centena", end="")
    elif centena > 1:
        print(" centenas", end="")
    
    if dezena > 0:
        print(", " if centena > 0 else "", end="")
        print(f"{dezena}", end="")
        if dezena == 1:
            print(" dezena", end="")
        else:
            print(" dezenas", end="")
    
    if unidade > 0:
        print(" e " if centena > 0 or dezena > 0 else "", end="")
        print(f"{unidade}", end="")
        if unidade == 1:
            print(" unidade")
        else:
            print(" unidades")
    else:
        print() 
else:
    print("Número inválido. Insira um número entre 1 e 999.")
