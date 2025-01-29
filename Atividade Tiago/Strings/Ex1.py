frase1=input('Digite uma frase: ')
frase2=input("Digite uma segunda frase: ")
print("A primeira frase foi: -", frase1,'- ela contém ',len(frase1),'caracteres.')
print("A segundra frase foi: -", frase2,'- ela contém ',len(frase2),'caracteres')
a=0
for i in range (len(frase1)):
    if frase1[i]==frase2[i]:
        a+=1
if len(frase1)==len(frase2):
    print("As duas frases têm o mesmo tamanho.")
    if a==len(frase1):
        print("As duas possuem contéudos iguais.")
    else:
        print('As duas possuem conteúdos diferentes.')
else:
    print("As duas frases têm tamanhos diferentes.")
    print('As duas possuem conteúdos diferentes.')
