matriz = [0,0,0],[0,0,0],[0,0,0]
soma = 0
# Inserindo dados na matriz usando for.
for l in range(len(matriz)):
    for c in range(len(matriz[l])):
        matriz[l][c] = int(input("Informe valores para a matriz: "))
        soma += matriz[l][c]     
print("A soma dos valores é: ", soma)
print(matriz)