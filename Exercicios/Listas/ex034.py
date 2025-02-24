# lê duas listas e gera uma terceira com os elementos das duas
lista1 = []
lista2 = []
uniao = []

while (True):
    num = int(input("Digite um valor para a primeira lista(0 para sair): "))
    if (num == 0):
        break

    lista1.append(num)

print("")

while (True):
    num = int(input("Digite um valor para a segunda lista(0 para sair): "))
    if (num == 0):
        break

    lista2.append(num)

uniao = lista1 + lista2

print(uniao)