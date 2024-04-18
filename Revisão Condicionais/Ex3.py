produto1 = float(input("Digite o valor do primeiro produto: "))
produto2 = float(input("Digite o valor do segundo produto: "))
produto3 = float(input("Digite o valor do terceiro produto: "))

if produto1 < produto2:
    menor = produto1
    numeroproduto = 1
else:
    menor = produto2
    numeroproduto = 2
if produto3 < menor:
    menor = produto3
    numeroproduto = 3
    
print("A melhor decisão é o produto: ", numeroproduto, " pois seu valor é: ", menor)
