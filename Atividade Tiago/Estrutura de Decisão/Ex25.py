print("Responda as perguntas sinceramente!")

print("Devia para a vítima?")
soma = 0
opc = int(input("1 - Sim, 2 - Não \n"))
if opc != 1 and opc != 2:
    print("Número digitado não corresponde às opções")
    quit()
soma += opc
opc = 0
print("Telefonou para a vítima?")
opc = int(input("1 - Sim, 2 - Não \n"))
if opc != 1 and opc != 2:
    print("Número digitado não corresponde às opções")
    quit()
soma += opc
opc = 0
print("Esteve no local do crime?")
opc = int(input("1 - Sim, 2 - Não \n"))
if opc != 1 and opc != 2:
    print("Número digitado não corresponde às opções")
    quit()
soma += opc
opc = 0
print("Mora perto da vítima?")
opc = int(input("1 - Sim, 2 - Não \n"))
if opc != 1 and opc != 2:
    print("Número digitado não corresponde às opções")
    quit()
soma += opc
opc = 0
print("Devia para a vítima?")
opc = int(input("1 - Sim, 2 - Não \n"))
if opc != 1 and opc != 2:
    print("Número digitado não corresponde às opções")
    quit()
soma += opc
opc = 0
print("Já trabalhou com a vítima?")
opc = int(input("1 - Sim, 2 - Não \n"))
if opc != 1 and opc != 2:
    print("Número digitado não corresponde às opções")
    quit()

if soma == 0:
    print("Você é uma pessoa inocente")
if soma == 2:
    print("Você é uma pessoa suspeita")
elif soma == 3 and soma == 4:
    print("Você é um Cúmplice")
elif soma == 5:
    print("Você é o Assassino")
 