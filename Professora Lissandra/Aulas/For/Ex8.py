x = int(input("Digite o começo do intervalo: "))
y = int(input("Digite o começo do intervalo: "))
soma = 0
for i in range(x, y):
    if i % 2 == 0:
        soma += i
        print(i)
print(soma)