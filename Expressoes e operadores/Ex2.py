a = int(input("Digite o valor de a: "))
b = int(input("Digite o valor de b: "))
c = int(input("Digite o valor de c: "))

if a >= b and a >= c :
    maior = a
    if b < c:
        menor = b
        print(" ", menor, c, maior)
    else:
        menor = c 
        print(menor, b, maior) 

if b >= a and b >= c :
    maior = b
    
    if a < c:
        menor = a
        print(menor, c, maior)
    else:
        menor = c 
        print(menor, a, maior) 

if c >= a and c >= b :
    maior = c
    
    if b > a:
        menor = a
        print(menor, b, maior)
    else:
        menor = b
        print(menor, a, maior) 