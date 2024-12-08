frase = input("Digite uma frase: ")
branco = frase.count(" ")

a = frase.count("a")
e = frase.count("e") 
i = frase.count("i") 
o = frase.count("o")
u = frase.count("u") 
vogais = a + e + i + o + u
print(f"O número de espaços em branco é: {branco} e de vogais é: {vogais}")