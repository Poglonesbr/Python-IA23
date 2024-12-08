codigo = int(input("Digite o código do cargo: "))
salario = float(input("Digite o seu salário: "))

match codigo:
    case 1:
        print("Seu cargo é Escrituário e seu aumento é de 50% ficando com ", salario * 1.50)
    case 2:
        print("Seu cargo é Secretário e seu aumento é de 35% ficando com ", salario * 1.35)
    case 3:
        print("Seu cargo é Caixa e seu aumento é de 20% ficando com ", salario * 1.20)
    case 4:
        print("Seu cargo é Gerente e seu aumento é de 10% ficando com ", salario * 1.10)
    case 5:
        print("Seu cargo é Diretor e seu aumento é de 00% ficando com ", salario )
    