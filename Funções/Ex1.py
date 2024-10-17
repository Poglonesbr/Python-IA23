x = float(input("Digite um numero: "))
y = float(input("Digite um numero: "))

def max (x,y):
    if x > y:
        return f"é {x}"
    elif x < y: 
        return f"é {y}"
    else:
        return "são iguais"
print(f"O maior numero {max(x,y)}")