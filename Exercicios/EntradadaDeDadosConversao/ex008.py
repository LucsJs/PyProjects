# Lê dias, horas, minutos e segundos e retorna quantidade em segundos

dia = int(input("Quantidade de dias: "))
hora = int(input("Quantidade de horas: "))
min = int(input("Quantidade de minutos: "))
seg = int(input("Quantidade de segundos: "))

qtd_seg = dia*24*60*60 + hora*60*60 + min*60 + seg

print("Total de segundos: %d" % qtd_seg)