dia = int(input("Digite o número equivalente ao dia da semana: "))

match dia:
    case 1: 
        print("Domingo")
    case 2:
        print("Segunda")
    case 3:
        print("Terça")
    case 4:
        print("Quarta")
    case 5: 
        print("Quinta")     
    case 6:
        print("Sexta")
    case 7:
        print("Sabado")
    case _:
        print("Numero inválido")