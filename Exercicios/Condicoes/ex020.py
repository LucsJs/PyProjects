# Calcula conta de telefone com base nos minuts usador no mês
# abaixo de 200m -> R$0.20/m | entre 200m e 400m -> R$0.18/m | acima de 400m -> R$0.15/min

minutos = int(input("Minutos utilizados no mês: "))

if (minutos < 200):
    preco = 0.2

else:
    if (minutos < 400):
        preco = 0.18

    else:
        preco = 0.15

valorPagamento = minutos * preco

print("Valor a pagar: R$ %.2f" % valorPagamento)