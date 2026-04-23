valor = int(input("Digite o valor a pagar:"))
cedulas = 0
atual = 50
apagar = valor

while (True):
    if (atual <= apagar):
        apagar -= atual
        cédulas += 1

    else:
        print(f"{cedulas} cédula(s) de R${atual}")
        if (apagar == 0):
            break
        if atual == 50:
            atual = 20
        else