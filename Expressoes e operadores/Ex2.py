a = int(input("Digite o valor de a: "))
b = int(input("Digite o valor de b: "))
c = int(input("Digite o valor de c: "))

if a >= b and a >= c :
    maior = a
    if b < c:
        print(b, c, maior)
    else:
        print(c, b, maior) 
if b >= a and b >= c:
    maior = b
    if c > a:
        print(a, c, maior)
