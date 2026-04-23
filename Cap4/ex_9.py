preco_casa = float(input("Digite o preço da casa: R$"))
anos = int(input("Informe em quantos anos pagar a casa: "))
prest = preco_casa / (anos * 12)
salario = float(input("Agora informe seu salário: R$"))

if (prest > salario * 30/100):
    print("Empréstimo não aprovado.")
else:
    print("Empréstimo aprovado.")