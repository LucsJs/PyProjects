cig_dia = int(input("Digite quantos cigarros fumados no dia: "))
anos = int(input("Informe quantos anos que você fuma: "))

cig_tot = cig_dia * 365 * anos
min_perdido = cig_tot * 10
dias_perdido = (min_perdido / 60) / 24;

print(f"Você perdeu {dias_perdido:.0f} dias de vida.")