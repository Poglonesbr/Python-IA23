dia = int(input("Digite o dia: "))
mes = int(input("Digite o mes: "))
ano = int(input("Digite o ano: "))

dias = int(input("Digite a quantidade de dias a ser somado: "))
dia = dia + dias
while dia > 30 :
    mes = mes + 1
    dia = dia - 30
while mes > 12 :
    mes = mes - 12
    ano = ano + 1


print(dia, mes, ano)