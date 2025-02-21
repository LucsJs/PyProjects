# Calcula preço da mercadoria com desconto

preco = float(input("Preço da mercadoria: "))
perc = float(input("Percentual de desconto: "))

valorDesc = preco * perc/100
precoAPagar = preco - valorDesc

print("Valor de desconto: R$ %.2f" % valorDesc) 
print("Preço a pagar: R$ %.2f" % precoAPagar)