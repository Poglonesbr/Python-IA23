string1 = input("Digite alguma coisa:")
string2 = input("Digite o que quer encontrar: ")

if (string1.find(string2) != -1):
    print(f"{string2} está na posição {string1.find(string2)}")
else: 
    print(f"{string2} não está na frase")