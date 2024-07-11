x = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
x[0] = int(input("Digite um numero: "))
maior = x[0]
nmaior = 0
menor = x[0]
nmenor = 0
for i in range (1, 10):
    if maior < x[i]:
        maior = x[i]
        nmaior = i
    if menor > x[i]:
        menor = x[i]
        nmenor = i
    x[i] = int(input("Digite um numero: "))
    
print(f"O maior está na posicao {nmaior} e o menor esta na posicao {nmenor}")