saldo = float(input("Digite o valor do salario: "))
CPMF = float (0.0038)
cheque1 = float(input("Digite o valor do primeiro cheque: "))
cheque2 = float(input("Digite o valor do segundo cheque: "))

saldo = saldo - ((cheque1 * CPMF ) + (cheque2 * CPMF ))
print("O valor na conta é: ", saldo)