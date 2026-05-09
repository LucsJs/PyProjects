num = int(input("Digite o número inteiro não negativo: "))

if (num == 0 or num == 1):
    print(f"{num} não é primo")
elif (num == 2):
    print(f"{num} é primo")
    
elif (num % 2 == 0):
    print(f"{num} não é primo")
else:
    valor = 3
    while (valor <= num ** (1 / 2)):
        if (num % valor == 0):
            print(f"{num} não é primo")
            break

        valor += 2

    if (valor > num ** (1 / 2)):
        print(f"{num} é primo")