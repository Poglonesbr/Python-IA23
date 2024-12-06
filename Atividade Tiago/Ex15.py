l1 = int(input("Digite um lado do triangulo: "))
l2 = int(input("Digite um lado do triangulo: "))
l3 = int(input("Digite um lado do triangulo: "))

if l1 == l2 and l1 == l3:
    print("Triângulo Equilátero")
elif (l1 == l2 and l1 != l3) or (l1 == l3 and l1 != l2) or (l3 == l2 and  l1 != l2):
    print("Triângulo Isósceles")
elif l1 != l2 and l1 != l3:
    print("Triângulo Escaleno")
else: 
    print("Não tem como formar um triangulo")