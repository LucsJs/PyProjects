num = int(input("Entre com um inteiro (0's a esquerda serão desconsiderados): "))

copiaNum = num
outroNum = 0

while (copiaNum != 0):
    ultimoDigito = copiaNum % 10
    outroNum *= 10
    outroNum += ultimoDigito
    copiaNum = (copiaNum - ultimoDigito) / 10

if (num == outroNum):
    print(f"{num} é palíndromo")
else:
    print(f"{num} não é palíndromo")