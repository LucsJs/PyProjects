valor = float(input("Digite o valor a pagar:"))
cedulas = 0
atual = 50
apagar = valor

while (True):
    if (atual <= apagar):
        apagar -= atual
        cedulas += 1

    else:
        print(f"{cedulas} cédula(s) de R${atual}")
        if (atual == 50):
            atual = 20
        elif (atual == 20):
            atual = 10
        elif (atual == 10):
            atual = 5
        elif (atual == 5):
            atual = 1
        elif (atual == 1):
            break
        cedulas = 0

atual = 0.5
moedas = 0

while (True):
    if (atual <= apagar):
        apagar -= atual
        moedas += 1

    else:
        print(f"{moedas} moeda(s) de R${atual}")
        if (atual == 0.5):
            atual = 0.1
        elif (atual == 0.1):
            atual = 0.05
        elif (atual == 0.05):
            atual = 0.02
        elif (atual == 0.02):
            atual = 0.01
        elif (atual == 0.01):
            break
        moedas = 0