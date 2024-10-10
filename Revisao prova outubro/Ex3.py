pares = set()

impares = set()

for i in range(1,11):
    if i % 2 == 0:
        pares.add(i)
    else:
        impares.add(i)

print(pares|impares)
print(pares&impares)


