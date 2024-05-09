dia = int(input("Digite o dia:"))

mes = int(input("Digite o mes: "))

ano = int(input("Digite o ano: "))

if (ano >= 1):

    if (( mes > 0) and (mes < 13)):

            match mes:

                case 1:
                    if ((dia > 0) and (dia < 31) ):
                        print("Data valida")
                case 2:
                    if ((dia > 0) and (dia < 29)):
                        print("Data valida")
                    elif ( ((ano % 4) == 0) and dia == 29):
                        print("Data valida")
                    else:
                        print("Data invalida")
                case 3:
                    if ((dia > 0) and (dia < 31) ):
                        print("Data valida")
                case 4:
                    if ((dia > 0) and (dia < 30) ):
                        print("Data valida")
                case 5:
                    if ((dia > 0) and (dia < 31) ):
                       print("Data valida")
                case 6:
                    if ((dia > 0) and (dia < 30) ):
                        print("Data valida")
                case 7:
                    if ((dia > 0) and (dia < 31) ):
                        print("Data valida")
                case 8:
                    if ((dia > 0) and (dia < 31) ):
                        print("Data valida")
                case 9:
                    if ((dia > 0) and (dia < 30) ):
                        print("Data valida")
                case 10:
                    if ((dia > 0) and (dia < 31) ):
                        print("Data valida")
                case 11:
                    if ((dia > 0) and (dia < 30) ):
                        print("Data valida")
                case 12:
                    if ((dia > 0) and (dia < 31) ):
                        print("Data valida")
                case _:
                    print("Data invalida")
    else:
        print("Data invalida")
else:
    print("Data invalida")
