soma = 0
for i in range(1, 1001):
    for x in range(1, i):
        if i % x == 0:
            soma += x
    if soma == i:
        print(i)
    soma = 0  