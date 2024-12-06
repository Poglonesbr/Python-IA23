valor = int(input("Digite o valor do saque (mínimo R$10, máximo R$600): "))

if valor < 10 or valor > 600:
    print("Valor inválido. O saque deve ser entre R$10 e R$600.")


notas = [100, 50, 10, 5, 1] 
quantidade_notas = {} 
for nota in notas:
    quantidade_notas[nota] = valor // nota  
    valor %= nota  

print("O saque será efetuado com:")
for nota, quantidade in quantidade_notas.items():
    if quantidade > 0:
        print(f"{quantidade} nota(s) de R${nota}")