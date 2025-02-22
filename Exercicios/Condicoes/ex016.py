# imposto de renda
# 0% nos primeiros R$1000, 20% entre 1000 e 3000 e 35% acima disto

salario = float(input("Informe seu salário: R$ "))
imp = 0

if (salario >= 1000 and salario < 3000):
    imp = (salario - 1000) * 20/100

if (salario >= 3000):
    imp = (salario - 3000) * 35/100 + 2000 * 20/100

print("Imposto a pagar R$ %.2f" % imp)

