sexo = input("Digite o seu sexo em F ou M: ")
idade = int(input("Digite sua idade: "))

if sexo == 'F' or sexo == 'f':
    if idade <= 12:
        print("É uma menina")
    elif idade <= 24:
        print("É uma moça")
    elif idade > 24:
        print("É uma mulher")
elif sexo == 'M' or sexo == 'm':
    if idade <= 12:
        print("É um menino")
    elif idade <= 24:
        print("É um moço")
    elif idade > 24:
        print("É um homem")
else:
    print("Voce é burro? refaça")

