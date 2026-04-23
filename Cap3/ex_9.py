dias = int(input("Quantos dias: "))
horas = int(input("Quantas horas: "))
min = int(input("Quantos minutos: "))
seg = int(input("Quantos segundos: "))

segundos_tot = (dias * 24 * 60 * 60) + (horas * 60 * 60) + (min * 60) + (seg)

print(f"{dias} dia(s) {horas} hora(s) {min} minuto(s) e {seg} segundo(s) dá {segundos_tot} segundos.")