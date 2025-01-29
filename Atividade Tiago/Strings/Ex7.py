frase=input('Digite uma frase: ').upper()
espacos=0
vogais=0
for i in range(len(frase)):
    if frase[i]==' ':
        espacos+=1
    elif frase[i]=='A' or frase[i]=='E' or frase[i]=='I' or frase[i]=='O' or frase[i]=='U':
        vogais+=1
print('A frase tem',espacos,'espaços e',vogais,'vogais.')