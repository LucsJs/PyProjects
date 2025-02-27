# Fazer uma lista de compras

compras = []

print("LISTA DE COMPRAS")

nomeProduto = input("Produto: ")
while (nomeProduto != "fim"):
    qtd = int(input("Quantidade: "))
    preco = float(input("Preço: "))
    compras.append([nomeProduto, qtd, preco])
    print("=-" * 10)
    nomeProduto = input("Produto: ")

print("=-" * 10)
precoTotal = 0

for produto in compras:
    precoTotal += produto[1] * produto[2]

print("Valor Total da compra:", precoTotal)


