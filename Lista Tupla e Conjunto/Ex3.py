K = []

for i in range(20):
    K.append(input("Digite um valor: "))

for i in range(len(K)):
    if i != (len(K) - 1):
        x = K[i+1]
        K[i+1] = K[i]
        K[i] = x

print(K)
