x=float(input("Digite o valor do primeiro produto: "))
y=float(input("Digite o valor do segundo produto: "))
z=float(input("Digite o valor do terceiro produto: "))
if x<y and x<z:
    print('Compre o produto com valor', x)
elif y<x and y<z:
    print('Compre o produto com valor', y)
else:
    print('Compre o produto com valor', z)