num1 = int(input("Entre um número inteiro: "))
num2 = int(input("Entre com outro número inteiro: "))

num1Copia = num1

while (num1Copia >= num2):
    num1Copia = num1Copia - num2

resto = num1Copia

print(f"Resto da divisão é {resto}")