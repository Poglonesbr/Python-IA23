n1=float(input("Digite a primeira nota do aluno: "))
n2=float(input("Digite a segunda nota do aluno: "))
n3=float(input("Digite a terceira nota do aluno: "))
media=(n1+n2+n3)/3
if media>=7 and media!=10:
    print("Aprovado!\nMédia: ",media)
elif media<7:
    print("Reprovado!\nMédia: ",media)
else:
    print("Aprovado com DISTINÇÃO!\nMédia: ",media)