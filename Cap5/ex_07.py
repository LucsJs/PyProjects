inicio = int(input("Inicio da tabuada: "))
fim = int(input("Fim da tabuada: "))

num = int(input("Tabuda: "))

x = inicio
while (x <= fim):
    print(f"{num} x {x} = {num * x}")
    x = x + 1