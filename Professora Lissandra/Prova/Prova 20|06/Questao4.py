x = int(input("Digite um numero: "))
n = 1
media = x
while x > 0:
    x = int(input("Digite um numero: "))
    if x > 0:
        media += x
        n += 1
media = media / n
print(media)