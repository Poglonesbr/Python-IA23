cpf=input('Digite o CPF em formato(XXX.XXX.XXX XX):')
print(cpf)
if len(cpf)!=14:
    print("CPF inválido.")
elif cpf[3]!='.' or cpf[7]!='.' or cpf[11]!=' ':
    print('CPF inválido.')
elif not cpf[0].isdigit():
    print('CPF inválido.')
elif not cpf[1].isdigit():
    print('CPF inválido.')
elif not cpf[2].isdigit():
    print('CPF inválido.')
elif not cpf[4].isdigit():
    print('CPF inválido.')
elif not cpf[5].isdigit():
    print('CPF inválido.')
elif not cpf[6].isdigit():
    print('CPF inválido.')
elif not cpf[8].isdigit():
    print('CPF inválido.')
elif not cpf[9].isdigit():
    print('CPF inválido.')
elif not cpf[10].isdigit():
    print('CPF inválido.')
elif not cpf[12].isdigit():
    print('CPF inválido.')
elif not cpf[13].isdigit():
    print('CPF inválido.')
else: 
    print('CPF válido.')