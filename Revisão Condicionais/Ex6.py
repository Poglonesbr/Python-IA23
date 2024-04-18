codigo = int(input("Digite o código do produto: "))

match codigo:
    case 1: 
        print("Alimento Não-Perecível")
        
    case  2 | 3 | 4: 
        print("Alimento Perecível")

    case 5 | 6:
        print("Vestuário")

    case 7:
        print("Higiene pessoal")

    case  8 | 9 | 10 | 11 | 12 | 13 | 14 | 15:
        print("Limpeza e utensílios domésticos")

    case _:
        print("Inválido")