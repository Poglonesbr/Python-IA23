mes = input("Escreva o nome de um mes: ")

match mes:
    case 'janeiro':
        print("31 dias")
    case 'fevereiro':
        print("28 dias")
    case 'marco':
        print("31 dias")
    case 'abril':
        print("30 dias")
    case 'maio':
        print("31 dias")
    case 'junho':
        print("30 dias")
    case 'julho':
        print("31 dias")
    case 'agosto':
        print("31 dias")
    case 'setembro':
        print("30 dias")
    case 'outubro':
        print("31 dias")
    case 'novembro':
        print("30 dias")
    case 'dezembro':
        print("31 dias")
    case _:
        print("Nome invalido")
