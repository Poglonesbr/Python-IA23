x = []
for i in range (0, 10):
    z = int(input("Digite um numero: "))
    if(z%2 == 0):
        z = z * i
    else:
        z = i
    x.append(z)
    
print(x)