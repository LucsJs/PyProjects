# implentar divisão inteira e resto da divisão usando apenas soma e sub

divInt = 0

dividendo = int(input("Digite o dividendo: "))
divisor = int(input("Digite o divisor: "))
copiaDividendo = dividendo

while (copiaDividendo > divisor):
    copiaDividendo -= divisor
    divInt+=1

restoDiv = copiaDividendo

print("Divisão inteira: %d" % divInt)
print("Resto da divisão: %d" % restoDiv)
