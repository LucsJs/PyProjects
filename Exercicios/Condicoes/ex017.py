# le 3 números e diz o maior

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))

if (num1 > num2):
    aux = num1
    num1 = num2
    num2 = aux

if (num2 > num3):
    aux = num2
    num2 = num3
    num3 = aux

if (num1 > num2):
    aux = num1
    num1 = num2
    num2 = aux

maior = num3
menor = num1

print("O maior número digitado foi %d e o menor %d" % (maior, menor))