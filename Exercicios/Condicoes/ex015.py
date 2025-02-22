# Pergunta velocidade de carro. Se maior que 80km/h retorne multa
# R$5.00/km acima de 80

velocidade = int(input("Informe sua velocidade no momento(Km/h): "))

if (velocidade > 80):
    multa = (velocidade - 80) * 5
    print("Você foi multado em R$ %.2f por excesso de velocidade." % multa)