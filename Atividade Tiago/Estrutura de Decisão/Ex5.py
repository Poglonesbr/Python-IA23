n1 = float(input("Digite a primeira nota do aluno: "))
n2 = float(input("Digite a segunda nota do aluno: "))

media = (n1 + n2) / 2

if media == 10:
    print("Aprovado com Distinção!")
elif media > 7:
    print("Aprovado!")
else:
    print("Reprovado!")

print(f"Média final: {media}")