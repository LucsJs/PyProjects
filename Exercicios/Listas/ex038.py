# Busca sequêncial

lista = [1, 2, 3, 7, 4, 7, 3, 9, 10, 2, 15, 713, 6]

num = int(input("Digite o número a ser buscado: "))

x = 0
while (x < len(lista) and lista[x] != num):
    x+=1

if (x == len(lista)):
    print("%d não encontrado" % num)

else:
    print("%d achado na posição %d" % (num, x))