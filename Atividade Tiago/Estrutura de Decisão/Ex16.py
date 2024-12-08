a=float(input("Digite um valor para A:"))
if a==0:
    print("A equação não é de segundo grau.")
    exit()    
b=float(input("Digite um valor para B:"))
c=float(input("Digite um valor para C:"))
if ((b*b)-4*a*c)<0:
    print("A equação não possui raízes reais.")
    exit()
if ((b*b)-4*a*c)==0:
    print("A equação possui apenas uma raiz real.")
if ((b*b)-4*a*c)>0:
    print("A equação possui duas raízes reais.")