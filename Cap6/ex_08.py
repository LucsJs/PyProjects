L = [15, 7, 27, 39]

p = int(input("Digite o valor a procurar: "))
x = 0 

while x < len(L) and L[x] != p: 
    x += 1

if x == len(L):
    print(f"{p} não foi achado")

else:
    print(f"{p} foi encontrado na posição {x}")
    