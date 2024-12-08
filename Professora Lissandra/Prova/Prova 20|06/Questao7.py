import random
num = random.randint(1, 100)
x = int(input("De um palpite para acertar o numero aleatorio: "))
while x != num:
    if x > num:
        x = int(input("O numero é menor que o digitado: "))
    if x < num:
        x = int(input("O numero é maior que o digitado: "))
print("Parabéns voce acertou!")