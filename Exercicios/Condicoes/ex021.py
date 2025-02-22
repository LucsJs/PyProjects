# Calculadora básica

print("Calculadora de inteiros")

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

print("Soma[+]")
print("Subtração[-]")
print("Multiplicação[*]")
print("Divisão[/]")

operacao = input("Digite a operação desejada: ")
isInvalid = False

if (operacao == "+"):
    result = num1 + num2

elif (operacao == "-"):
    result = num1 - num2

elif (operacao == "*"):
    result = num1 * num2

elif (operacao == "/"):
    result = num1 / num2

else:
    isInvalid = True

if (isInvalid):
    print("Digite uma operação válida")

else:
    print("%d %s %d = %.1f" % (num1, operacao, num2, result))