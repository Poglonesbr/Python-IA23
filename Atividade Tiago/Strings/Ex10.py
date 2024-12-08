dezena = {
    "2": "vinte",
    "3": "trinta",
    "4": "quarenta",
    "5": "cinquenta",
    "6": "sessenta",
    "7": "setenta",
    "8": "oitenta",
    "9": "noventa",
}
unidade = {
    "1": "um",
    "2": "dois",
    "3": "três",
    "4": "quatro",
    "5": "cinco",
    "6": "seis",
    "7": "sete",
    "8": "oito",
    "9": "nove",
}
especiais = {
    "10": "dez",
    "11": "onze",
    "12": "doze",
    "13": "treze",
    "14": "catorze",
    "15": "quinze",
    "16": "dezesseis",
    "17": "dezessete",
    "18": "dezoito",
    "19": "dezenove",
}
num = input("Digite um número inteiro até 99: ")
if not num.isdigit() or int(num) < 0 or int(num) > 99:
    print("Número inválido. Digite um número entre 0 e 99.")
else:
    if len(num) == 1:
        print("Por extenso:", unidade.get(num, "zero"))
    elif num in especiais: 
        print("Por extenso:", especiais[num])
    else:
        dez = dezena.get(num[0], "")
        uni = unidade.get(num[1], "")
        if uni:
            print("Por extenso:", f"{dez} e {uni}")
        else:
            print("Por extenso:", dez)