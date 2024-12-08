from unidecode import unidecode

frase = input("Digite a frase a verificar: ")
verificada = frase.replace(" ", "").upper()
if verificada == verificada[::-1]:
    print(f"A frase {frase} é um palíndromo")
elif unidecode(verificada) == unidecode(verificada[::-1]):
    print(f"A frase {frase} é um palíndromo se desconsiderar os acentos")
else:
    print(f"A frase {frase} não é um palíndromo")