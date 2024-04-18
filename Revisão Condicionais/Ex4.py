ano = int(input("Digite o ano atual: "))
nascimento = int(input("Digite o seu ano de nascimento: "))

if ano - nascimento >= 16:
    print("Já tem idade para votar!!")
else:
    print("Não tem idade para votar!")