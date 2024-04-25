salario_atual = float(input("Digite o salario atual: "))

if salario_atual <= 290 :

    salario_reajuste =  salario_atual * 1.2
    print("O salario inicial é: ", salario_atual,", o aumento é de 20%, o valor do aumento é: ",
           salario_reajuste - salario_atual, " e o salario atual é: ", salario_reajuste  )

elif (salario_atual > 290) and (salario_atual <= 800):
    salario_reajuste =  salario_atual * 1.15
    print("O salario inicial é: ", salario_atual,", o aumento é de 15%, o valor do aumento é: ",
           salario_reajuste - salario_atual, " e o salario atual é: ", salario_reajuste  )

elif (salario_atual > 800) and (salario_atual <= 1700):
    salario_reajuste =  salario_atual * 1.1
    print("O salario inicial é: ", salario_atual,", o aumento é de 10%, o valor do aumento é: ",
           salario_reajuste - salario_atual, " e o salario atual é: ", salario_reajuste  )
    
elif (salario_atual > 1700):
    salario_reajuste =  salario_atual * 1.05
    print("O salario inicial é: ", salario_atual,", o aumento é de 5%, o valor do aumento é: ",
    salario_reajuste - salario_atual, " e o salario atual é: ", salario_reajuste  )

