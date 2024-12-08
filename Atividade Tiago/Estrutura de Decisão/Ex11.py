salario = float(input("Digite o valor do seu salário atual: "))
reajuste = 0
novo_salario = 0
aumento = 0
if 0 < salario <= 280:
    reajuste = 0.2
    aumento = salario * reajuste
    novo_salario = salario + aumento
elif 280 < salario <= 700:
    reajuste = 0.15
    aumento = salario * reajuste
    novo_salario = salario + aumento
elif 700 < salario < 1500:
    reajuste = 0.1
    aumento = salario * reajuste
    novo_salario = salario + aumento
elif 1500 >= salario:
    reajuste = 0.5
    aumento = salario * reajuste
    novo_salario = salario + aumento
else:
    print("Salário inválido")

print(f"O salário inicial é {salario}, o percentual do aumento é {reajuste*100}%, o valor do aumento é {aumento} e o salário final é {novo_salario}")