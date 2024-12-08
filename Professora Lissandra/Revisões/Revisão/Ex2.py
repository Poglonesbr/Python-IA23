num = int(input("Digite um numero para verificar o quadrado: "))

raiz = num ** 0.5

if (raiz % 1 == 0):
    print("O numero é um quadrado perfeito")
else :
    print("O numero não é um quadrado perfeito")
print(raiz)