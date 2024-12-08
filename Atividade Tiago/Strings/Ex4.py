nome = input("Digite seu nome (letras maiúsculas ou minúsculas): ").upper()

for i in range (0, len(nome)):
    for x in range (0, i+1):
        print(nome[x], end="")
    print("")

# OU
# for i in range (0, len(nome)):
#   print(nome(i:))
#