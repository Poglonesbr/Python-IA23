K = [1, 2, 3, 4, 5, 6, 7, 8, 9]

div = 0


for i in range (0, len(K)):
    for x in range (1, K[i]+1):
        if K[i] % x == 0:
            div += 1
    if div == 2:
        print(f"O numero {K[i]} está na posicao {i}")
    div = 0

