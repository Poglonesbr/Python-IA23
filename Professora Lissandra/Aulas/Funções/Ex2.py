x = float(input("Digite um numero: "))

def par (x):
    if x % 2 == 0:
        return True
    else:
        return False

print(f"O numero {x} é par? {par(x)}")