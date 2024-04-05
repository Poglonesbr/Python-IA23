x = float(input("Digite o valor de x: "))
y = float(input("Digite o valor de y: "))

if (x + y) * 0.30 > 500:
    troca = x 
    x = y 
    y = troca
    print( x+y)
    print("x é: ", x, " e y é: ", y)
else :
    if x > y:
        print(y)
    else:
        print(x)