x = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
for i in range (0, 10):
    x[i] = int(input("Digite um numero: "))

def verificarNumero (x):
    for i in range (0, 10):
        if x[i] < 0:
            x[i] = 0
    print(x)

verificarNumero(x)