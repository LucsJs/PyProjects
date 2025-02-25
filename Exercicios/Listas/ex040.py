# percorrer lista para achar maior e menor valor

l = [1, 9, 3, 7, 2, 8, 5, 6, 12, 15, 0]
maior = l[0]
menor = l[0]

for x in l:
    if (x > maior):
        maior = x

    elif (x < menor):
        menor = x

print("Maior é %d" % maior)
print("Menor é %d" % menor)
    