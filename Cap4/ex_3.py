num = int(input("Digite o primeiro inteiro: "))
maior = num
menor = num

num = int(input("Digite o segundo inteiro: "))
if (num > maior):
    maior = num

if (num < menor):
    menor = num


num = int(input("Digite o segundo inteiro: "))
if (num > maior):
    maior = num

if (num < menor):
    menor = num

print(f"Maior número digitado: {maior}")
print(f"Menor número digitado: {menor}")