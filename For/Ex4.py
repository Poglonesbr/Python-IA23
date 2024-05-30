numprimo = 0
num = 2

while numprimo < 10:
    primo = True
    for i in range(2, int(num**0.5) + 1):  
        if num % i == 0:
            primo = False
    if primo:
        print(f"O número {num} é primo!")
        numprimo += 1
    num += 1