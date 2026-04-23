dist = float(input("Informe a distância em Km/H: "))

if (dist <= 200):
    preco = dist * 0.5
else:
    preco = dist * 0.45

print(f"O preco a ser pago é: R$ {preco:.2f}")


