string = input("Digite uma string: ")
string = string.upper()
contagem = {}

for caractere in string:
 
    if caractere in contagem:
        contagem[caractere] += 1  
    else:
        contagem[caractere] = 1  

for caractere, quantidade in contagem.items():
    print(f"{caractere}: {quantidade}x")