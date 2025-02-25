# Faz busca sequencial por dois números fala quem foi achado primeiro

l = [1, 9, 6, 2, 8, 1, 5, 2, 13, 16, 8, 12, 10, 20, 1]

num1 = int(input("Digite o primeiro número a ser buscado: "))
num2 = int(input("Digite o segundo número a ser buscado: "))

indice1 = 0
indice2 = 0

while (indice1 < len(l)):
    if (l[indice1] == num1):
        break

    indice1 += 1

while (indice2 < len(l)):
    if (l[indice2] == num2):
        break

    indice2 += 1

if (indice1 == len(l)):
    print("%d não foi achado." % num1)

else:
    print("%d está na posição %d" % (num1, indice1))

if (indice2 == len(l)):
    print("%d não foi achado." % num2)

else:
    print("%d está na posição %d" % (num1, indice2))

    

    