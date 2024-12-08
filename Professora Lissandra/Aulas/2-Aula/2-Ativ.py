deposito = float (input("Digite o seu depósito: "))
juros =  float (input("Digite a taxa de juros em porcentagem: ") )
rende = deposito * (juros / 100)
print("O seu deposito de ", deposito, " rendeu ", rende, "resultando em: ", deposito + rende)