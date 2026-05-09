lista1 = [1, 9, 3, 7, 1, 2, 9, 4]
lista2 = [0, 3, 8, 1, 8, 5, 6, 2]
listas_concat = lista1 + lista2

lista_resultado = []
i = 0
while (i < len(listas_concat)):
    j = 0
    while (j < len(lista_resultado)):
        if (lista_resultado[j] == listas_concat[i]):
            break                                     # esse trecho inteiro do while ficaria mais legível com:
                                                      # if (lista1[i] not in lista_resultado):
        j += 1                                        #     lista_resultado.append(lista1[i])
                                                      # mas o livro ainda não ensinou o 'in'
    if (j == len(lista_resultado)):
        lista_resultado.append(listas_concat[i])

    i += 1

print(lista_resultado)



