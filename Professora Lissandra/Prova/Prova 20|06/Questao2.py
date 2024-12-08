opc = int(input("Digite 1 - Entrar, 2 - Sair: "))
while opc == 1:
    n1 = int(input("Digite o primeiro numero a ser calculado: "))
    n2 = int(input("Digite o segundo numero a ser calculado: "))
   
    op = int(input("Digite o numero da operação 1-Soma, 2-Subtração, 3-Multiplicação, 4-Divisão, 5-Potenciação: "))
    if op == 1:
        soma = n1 + n2 
        print(f"O resultado de {n1} + {n2} = {soma}")
    elif op == 2:
        soma = n1 - n2 
        print(f"O resultado de {n1} - {n2} = {soma}")
    elif op == 3:
        soma = n1 * n2 
        print(f"O resultado de {n1} * {n2} = {soma}")
    elif op == 4:
        soma = n1 / n2 
        print(f"O resultado de {n1} / {n2} = {soma}")
    elif op == 5:
        soma = n1 ** n2 
        print(f"O resultado de {n1} ** {n2} = {soma}")
    opc = int(input("Quer continuar? Digite 1 - Sim, 2 - Não: "))
