num1 = float(input("Digite um número: "))
num2 = float(input("Digite outro número: "))
aux = 0

print("OPERAÇÕES")
print("+ para soma")
print("- para subtração")
print("* para multiplicação")
print("/ para divisão")
print("")

operacao = input("Informe qual a operação desejada: ")

if (operacao == "+"):
    resultado = num1 + num2
elif (operacao == "-"):
    resultado = num1 - num2
elif (operacao == "*"):
    resultado = num1 * num2
elif (operacao == "/"):
    resultado = num1 / num2
else:
    aux = 1

if (aux == 1):
    print("Entre com uma operação listada!")

else:
    print(f"{num1} {operacao} {num2} = {resultado}")
