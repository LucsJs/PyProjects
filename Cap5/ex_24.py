nPrimo = int(input("Informe quantos primos mostrar: "))
primoContador = 0
num = 3

if (nPrimo > 0):
    print(2, end=" ")
    primoContador += 1

while (primoContador < nPrimo):
    valor = 3
    while (valor <= num ** (1 / 2)):
        if (num % valor == 0):
            
            break

        valor += 2

    if (valor > num ** (1 / 2)):
        print(f"{num}", end=" ")
        primoContador += 1

    num += 2
    