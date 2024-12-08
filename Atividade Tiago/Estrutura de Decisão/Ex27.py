morango = float(input("Digite em quilos a quantidade de morango que deseja comprar: "))
maca = float(input("Digite em quilos a quantidade de morango que deseja comprar: "))

valor_morango = 0
valor_maca = 0
total = 0
desconto = 0
if morango <= 5:
    valor_morango = morango * 2.5
elif morango > 5:
    valor_morango = morango * 2.2
else:
    print("Número invalido")
    exit()
if maca <= 5:
    valor_maca = maca * 1.8
elif maca > 5:
    valor_maca = maca * 1.5
else:
    print("Número invalido")
    exit()
total = valor_morango + valor_maca
print(f"Você comprou {morango} Kg de morango, equivalente à R${valor_morango} e {maca} Kg de maçã, equivalente à R${valor_maca}\nResultando em R${total}", end="")
if morango + maca > 8 or valor_maca + valor_morango > 25:
    total = (valor_morango + valor_maca) * 0.9
    print(f", com o desconto de 10% ficará R${total} no total")