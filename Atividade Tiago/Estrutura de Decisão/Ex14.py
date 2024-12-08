n1=float(input("Digite a primeira nota do aluno: "))
n2=float(input("Digite a segunda nota do aluno: "))
media=(n1+n2)/2
print("NOTAS\n  1° NOTA: ",n1)
print("  2°NOTA: ",n2)
print("\nMÉDIA: ",media)
if media<4:
    print("\nConceito: E")
elif media>=4 and media <6:
    print("\nConceito: D")
elif media>=6 and media <7.5:
    print("\nConceito: C")
elif media>=7.5 and media<9:
    print("\nConceito: B")
else:
    print("\nConceito: A")
if media>=6:
    print("\nStatus: APROVADO")
else:
    print("\nStatus: REPROVADO")