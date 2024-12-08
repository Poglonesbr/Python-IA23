n1 = float(input('Informe o primeiro número: '))
n2 = float(input('Informe o segundo número: '))
op = input('Informe a operacao("+", "-", "*", "/"): ')
match op:
    case '+':
        resultado=n1+n2
    case '-':
        resultado=n1-n2
    case '*':
        resultado=n1*n2
    case '/':
        resultado=n1/n2
    case default:
        exit
print("O resultado foi:",resultado)
if resultado%2==0:
    print(resultado,'é um número par.')
else:
    print(resultado,'é um número ímpar.')
if resultado>=0:
    print(resultado,'é positivo')
else:
    print(resultado,'é negativo')
if resultado//1==resultado:
    print(resultado,'é um número inteiro.')
else:
    print(resultado,'é um número decimal.')