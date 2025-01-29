nome=input('Digite um nome:').upper()
for i in range(len(nome), 0, -1):
    print(nome[:i])
