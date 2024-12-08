ano=int(input("Informe um ano:"))
if ano<0:
    print("Não são permitidas datas negativas.")
    exit()
mes=int(input("Informe um mês(números): "))
if mes<1 or mes>12:
    print("Mês inválido.")
    exit()
dia=int(input("Informe um dia válido correspondente ao mês e ano informado: "))
if dia<1 or dia>31:
    print("Dia inválido.")
    exit()
elif ano%4!=0 and mes==2 and dia>28:
    print("Dia inválido.")
    exit()
elif ano%4==0 and mes==2 and dia>29:
    print("Dia inválido.")
    exit()
elif (mes==4 or mes==6 or mes==9 or mes==11) and dia>30:
    print("Dia inválido.")
    exit()
else:
    print(dia,"/",mes,"/",ano)