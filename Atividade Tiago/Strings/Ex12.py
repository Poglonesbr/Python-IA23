numero = input("Digite o numero de telefone:")
num1, num2 = numero.split("-")
if len(num1) + len(num2) == 8:
    print(f"Telefone valido sem formatação: {num1}{num2}")
    print(f"Telefone valido com formatação: {num1}-{num2}")
elif len(num1) + len(num2) == 7:
    print(f"Telefone corrigido sem formatação: 3{num1}{num2}")
    print(f"Telefone corrigido com formatação: 3{num1}-{num2}")
else:
    print("Você digitou o número errado!")