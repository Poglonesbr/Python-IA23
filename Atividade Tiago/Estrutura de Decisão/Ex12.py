horas=int(input('Digite quantas horas você trabalha no mês: '))
valor=float(input("Digite o valor da sua hora:"))
sBruto=horas*valor
salario=sBruto-(sBruto*0.03)
fgts=sBruto-(sBruto*.89)
if sBruto>900 and sBruto <=1500:
    salario-=(salario*.05)
    ir=5
elif sBruto>1500 and sBruto <=2500:
    salario-=(salario*.1)
    ir=10
elif sBruto>2500:
    salario-=(salario*.2)
    ir=20
print("Salário bruto: ", sBruto)
print('Imposto de renda(',ir,'%): -',sBruto*(ir/100))
print('FGTS(11%):',fgts)
print('Total de Descontos:',sBruto-salario)
print('Salário Líquido: ',salario)