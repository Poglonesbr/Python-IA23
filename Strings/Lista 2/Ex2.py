nome = input("Digite um nome: ")
nome = nome.upper()
lista = list(nome)
tamanho = len(lista)

for i in range (0, tamanho):
    print(lista.strip())