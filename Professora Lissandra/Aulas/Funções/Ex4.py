base = float(input("Digite a base: "))
altura = float(input("Digite a altura: "))

def area (base, altura):
    return (base * altura)/2

print(f"A area de um quadrado de base {base} e altura {altura} é {area(base, altura)}")