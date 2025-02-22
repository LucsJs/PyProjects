# Empréstimo de banco para comprar casa
# Pergunta salário, valor de casa a comprar e quantidade de anos a pagar.
# se valor da prestação mensal for maior que 30% do salario, o empréstimo não é aprovado

print("EMPRÉSTIMO BANCÁRIO")

salario = float(input("Digite seu salário: R$ "))
valorCasa = float(input("Entre com o valor da casa: R$ "))
anos = int(input("Informe em quantos anos deseja quitar este imóvel: "))

valorPrestacao = valorCasa/(anos*12)

if (valorPrestacao > salario * 30/100):
    situacao = "NÃO APROVADO"

else:
    situacao = "APROVADO"

print("Situação do empréstimo: %s" % situacao)

