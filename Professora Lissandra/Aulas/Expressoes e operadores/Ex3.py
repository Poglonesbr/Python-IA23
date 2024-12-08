
a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))
d = float(input("Digite o valor de d: "))
e = float(input("Digite o valor de e: "))

if a >= b:
    maior = a
else:
    maior = b

if maior <= c:
    maior = c
if maior <= d:
    maior = d
if maior <= e:
    maior = e

print(maior)