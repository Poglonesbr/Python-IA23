carne=input("Escolha qual carne você deseja:\nF-Filé Duplo\nA-Alcatra\nP-Picanha\n")
quantidade=float(input("Digite quantos kg de carne você deseja: "))
if carne=='F':
    if quantidade<=5:
        valor=quantidade*4.9
    else:
        valor=quantidade*5.8
    carne='Filé Duplo'
if carne=='A':
    if quantidade<=5:
        valor=quantidade*5.9
    else:
        valor=quantidade*6.8
    carne='Alcatra'
if carne=='P':
    if quantidade<=5:
        valor=quantidade*6.9
    else:
        valor=quantidade*7.8
    carne='Picanha'
pag=input("Escolha a forma de pagamento:\nC-Cartão\nD-Dinheiro\n")
preco=valor
if pag=='C':
    valor*=0.95
    pag='Cartão'
    desconto='5%'
else:
    pag='Dinheiro'
    desconto='0%'
print("     NOTA FISCAL")
print("Tipo:", carne)
print("Quantidade: ", quantidade)
print("Preço total:", preco)
print("Forma de pagamento: ", pag)
print("Valor do desconto: ", desconto)
print("Valor a pagar: ", valor)