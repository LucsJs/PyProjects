preco = float(input("Informe o preço da mercadoria: R$"))
desc = float(input("Digite o percentual de desconto(%): "))

precoDescontado = preco * (1 - desc / 100) # -> preco - preco * desc / 100

print(f"O preço com desconto fica {precoDescontado:.2f}")
