# separa os valores pares e impares de uma lista

l = [1, 9, 2, 7, 5, 3, 6, 15, 19, 11, 16]
pares = []
impares = []

for x in l:
    if (x % 2 == 0):
        pares.append(x)

    else:
        impares.append(x)

print("Lista:", l)
print("Pares na lista:", pares)
print("Ímpares na lista:", impares)