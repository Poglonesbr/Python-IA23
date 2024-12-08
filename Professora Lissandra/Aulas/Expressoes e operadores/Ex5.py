litros = float(input("Digite a quantidade de litros compradas: "))
gas = input("Selecione o combustivel, A para Alcool e G para Gasolina: ")
if gas == 'G' or gas == 'g':
    if litros <= 20:
        preco = (7.2 * 0.96) * litros
    else:
        preco = (7.2 * 0.94) * litros
    print("O valor é: ", preco )
elif gas == 'A' or gas == 'a':
    if litros < 20:
        preco = (6.5 * 0.97) * litros
    else:
        preco = (6.5 * 0.95) * litros
    print("O valor é: ", preco )
else:
    print("Refaça")