n1 = float(input("Digite o valor da primeira nota: "))
p1 = int(input("Digite o pesoa da primeira nota: "))
n2 = float(input("Digite o valor da segunda nota: "))
p2 = int(input("Digite o pesoa da segunda nota: "))
n3 = float(input("Digite o valor da terceira nota: "))
p3 = int(input("Digite o pesoa da terceira nota: "))

media = int((n1 * p1 + n2 *p2 + n3 * p3) / (p1 + p2 + p3))

if media >= 6: 
    print("Aprovado!! Média: ", media)
else:
    print("Reprovado! Média: ", media)