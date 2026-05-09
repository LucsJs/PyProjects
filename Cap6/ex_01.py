notas = [0, 0, 0, 0, 0, 0, 0]

i = soma_notas = 0
while (i < 7):
    notas[i] = float(input(f"{i + 1}º nota: "))
    soma_notas += notas[i]
    i += 1
    
media = soma_notas / 7

print(f"Media das notas é {media:.1f}")