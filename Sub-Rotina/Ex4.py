
def calculadora (n1, n2, op):
    match op:
        case 1:
            
            return (n1 + n2)
        case 2:
            return(n1-n2)
        case 3:
            return(n1*n2)
        case 4:
            if n2 == 0:
                print("Não é possivel divir por zero refaça o calculo")
            else:
                return(n1/n2) 
        case 5:
            return(n1**n2)
        case 6:
            return(n1**(0,n2))
        case _:
            print("Voce digitou um numero errado")

n1 = int(input("Digite o primeiro numero para realizar o calculo: "))
n2 = int(input("Digite o segundo numero para realizar o calculo: "))
op = int(input("Digite o numero correspondente ao operador \n1-Soma 2-Subtração 3-Multiplicação 4-Divisão 5-Exponenciação 6-Raiz\n"))
print(calculadora(n1, n2, op))