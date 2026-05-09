lista = [9, 1, 7, 3, 0, 1, 7, 3, 9, 4, 6, 7, 1]
lista = [13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2,]

i = 0
j = len(lista)

print(lista)
while (j > i):
    while (i < j - 1):
        if (lista[i] > lista[i + 1]):
            aux = lista[i]
            lista[i] = lista[i + 1]
            lista[i + 1] = aux
        i += 1
    i = 0
    j -= 1

print(lista)
