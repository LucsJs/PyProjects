
totalAPagar = 0

while (True):
    cod = int(input("Código do produto: "))

    if (cod == 0):
        break

    while (cod != 1 and cod != 2 and cod != 3 and cod != 5 and cod != 9):
        print("Código inválido!")
        cod = int(input("Código do produto: "))
    
    qtd = int(input("Quantidade do produto: "))

    if (cod == 1):
        preco = 0.5
    elif (cod == 2):
        preco = 1
    elif (cod == 3):
        preco = 4
    elif (cod == 5):
        preco = 7
    else:
        preco = 8
    
    totalAPagar += qtd * preco

print(f"Total a pagar: R${totalAPagar:.2f}")
    