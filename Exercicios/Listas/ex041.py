# Vê uma lista de temperaturas e pega o menor e maior valor e a média

t = [-10, -8, 0, 1, 2, 5, -2, -4]

maximo = t[0]
minimo = t[0]
soma = 0

for x in t:
    if (x > maximo):
        maximo = x

    elif (x < minimo):
        minimo = x

    soma += x

media = soma / len(t)

print("Temperatura máxima:", maximo)
print("Temperatura mínima:", minimo)
print("Média das temperaturas: %.2f" % media)