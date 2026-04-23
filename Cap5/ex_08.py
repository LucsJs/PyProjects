num1 = int(input("Digite um número inteiro: "))
num2 = int(input("Digite outro número inteiro: "))

x = 1
prod = 0

while (x <= num2):
    prod = prod + num1
    x = x + 1

print(f"{num1} x {num2} = {prod}")