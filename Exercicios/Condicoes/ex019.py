# Pergunta distância de viagem e calcula preço da passagem
# R$0.50/km até 200km, do contrário R$0.45/km

dist = int(input("Informe distância da viagem(Km): "))

if (dist <= 200):
    preco = 0.5
else:
    preco = 0.45

valorPassagem = dist * preco

print("Valor da passagem fica em R$ %.2f" % valorPassagem)