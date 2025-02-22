# imprime tabuada do 2 mas começa e termina onde o usuário mandar

inicio = int(input("Digite o inicio da tabuada: "))
fim = int(input("Digite o fim da tabuada: "))
cont = inicio

while (cont <= fim):
    print("2 x %2d = %2d" % (cont, 2*cont))
    cont += 1