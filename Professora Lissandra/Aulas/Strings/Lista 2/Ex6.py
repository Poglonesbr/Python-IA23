frase_ = input("Digite uma frase: ")
frase = frase_.lower()
frase = frase.replace(" ", "")


if (frase == frase[::-1] ):
    print("A frase ", frase_, " é um palindromo!")
else:
    print("A frase não é um palindromo")