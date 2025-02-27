# Sistema de vendas

estoque = {
    "Tomate": [1000, 2.3],
    "Alface": [500, 0.45],
    "Batata": [2001, 1.20],
    "Feijão": [100, 1.5]
}

vendas = []
valorTotal = 0

nomeProduto = input("Nome do produto: ")
while(nomeProduto != "fim"):
    while not((nomeProduto in estoque)):
        print("Não existe produto com este nome no estoque.")
        nomeProduto = input("\nNome do produto: ")
        
    quantidadeProduto = int(input("Quantidade do produto: "))
    vendas.append([nomeProduto, quantidadeProduto])
    nomeProduto = input("\nNome do produto: ")

print()
print("=-=" * 10)
print("\n=-=-VENDAS-=-=")

print("Produto  Preço/unid  Quantidade  Preço/total")
for produto, quantidade in vendas:
    valorParcial = quantidade * estoque[produto][1]
    print("%-7s  %-10.2f  %-10d  %-11.2f" % (produto, estoque[produto][1], quantidade, valorParcial))
    valorTotal += valorParcial
    estoque[produto][0] -= quantidade

print("\nValor total: %.2f" % valorTotal)

print("\n")
print("ESTOQUE")
for chave, prod in estoque.items():
    print("%s: %4d %.2f" % (chave, prod[0], prod[1]))



