# Calcula conta de energia

kwhConsumido = float(input("Quantidade de kWt consumida: "))
tipoInstalacao = input("Digite o tipo de instalação(R/I/C): ")

if (tipoInstalacao == "R"):
    if (kwhConsumido <= 500):
        preco = 0.4
    
    else:
        preco = 0.65

elif (tipoInstalacao == "C"):
    if (kwhConsumido <= 1000):
        preco = 0.55
    
    else:
        preco = 0.6

else:
    if (kwhConsumido <= 5000):
        preco = 0.55
    
    else:
        preco = 0.6

valorPagamento = kwhConsumido * preco

print("Valor a ser pago: R$ %.2f" % valorPagamento)