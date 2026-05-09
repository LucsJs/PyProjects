notas = [0, 0, 0, 0, 0]

x = 0 
while (x < 5):
    n = float(input(f"{x + 1}º nota: "))
    notas[x] = n
    x += 1 

i = soma_notas = 0
while (i < 5):
    soma_notas += notas[i]
    i += 1

media = soma_notas / 5

print(f"Media = {media:.1f}")
