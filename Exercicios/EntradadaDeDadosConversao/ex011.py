# Pede a velocidade média de uma viagem e a distância. Retorna o tempo de viagem

dist = int(input("Distância da viagem(Km): "))
velocidade = int(input("Velocidade média esperada para a viagem(Km/H): "))

horas = dist / velocidade
min = (horas - int(horas)) * 60
horas = int(horas)


print("Tempo de viagem estimado: %dhrs e %.0fmin" % (horas, min))

