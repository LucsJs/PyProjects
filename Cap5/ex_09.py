num1 = int(input("Digite o primeiro inteiro: "))
num2 = int(input("Digite o segundo inteiro: "))

div_int = 0
num1Copia = num1

while (num1Copia - num2 >= 0):
    num1Copia = num1Copia - num2
    div_int = div_int + 1

resto = num1Copia

print(f"Divisão inteira de {num1} por {num2} é {div_int}")
print(f"Resto da divisão é {resto}")

