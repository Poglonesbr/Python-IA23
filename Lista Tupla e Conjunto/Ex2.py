R = []
S = []

for i in range(5):
    R.append(input("Digite o Gabarito: "))
for i in range(10):
    S.append(input("Digite a aposta: "))


R_set = set(R)
S_set = set(S)

Z = R_set & S_set

print("Você fez ", len(Z), " pontos")