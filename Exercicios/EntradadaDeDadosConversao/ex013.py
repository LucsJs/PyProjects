# Pergunta quantidade de km e dias com um carro alugado. Retorna valor a pagar 
# R$60/dia e R$0.15/km

dia = int(input("Por quantos dias o carro foi alugado? "))
km = int(input("Quantos km foram rodados? "))

valorPagar = dia*60 + km*0.15

print("Valor a pagar: R$ %.2f" % valorPagar)