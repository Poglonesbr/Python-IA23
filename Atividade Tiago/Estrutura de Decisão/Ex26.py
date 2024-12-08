tipo=input("Escolha:\nG-Gasolina\nA-Álcool\n")
litros=float(input("Quantos litros serão colocados? "))
if tipo=='G':
    valor=litros*2.5
    if litros>20:
        print("O valor é de: ",valor*0.95)
    else:
        print("O valor é de: ",valor*0.97)
else:
    valor=litros*1.9
    if litros>20:
        print("O valor é de: ",valor*0.94)
    else:
        print("O valor é de: ",valor*0.96)