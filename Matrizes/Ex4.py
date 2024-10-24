matriz = [0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]
soma = 0

for l in range(len(matriz)):
    for c in range(len(matriz[l])):
        matriz[l][c] = int(input("Informe valores para a matriz: "))
        if l == 4:
            soma += matriz[l][c]     
print("A soma dos valores é: ", soma)