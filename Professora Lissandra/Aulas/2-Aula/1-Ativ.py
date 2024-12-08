salario = float (input("Digite o seu salario "))
gratificacao = salario * 0.05 
imposto = salario * 0.07
salario = salario - (imposto - gratificacao) 
print("Seu salario é: ", salario)