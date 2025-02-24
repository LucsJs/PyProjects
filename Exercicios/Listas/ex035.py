# Faz união de duas listas sem repetições

lista1 = [1, 1, 5, 8, 6, 7, 9, 3, 10, 4]
lista2 = [3, 5, 8, 1, 4, 8, 9, 3, 2]
uniao = []

i = 0
while (i < len(lista1)):
    x = 0
    repetido = False
    while (x < len(uniao)):
        if (lista1[i] == uniao[x]):
            repetido = True
            break

        x += 1
        
    if (repetido == False):
        uniao.append(lista1[i])

    i += 1

i = 0
while (i < len(lista2)):
    x = 0
    repetido = False
    while (x < len(uniao)):
        if (lista2[i] == uniao[x]):
            repetido = True
            break

        x += 1
        
    if (repetido == False):
        uniao.append(lista2[i])

    i += 1

print(uniao)


    