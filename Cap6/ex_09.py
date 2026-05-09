L = [1, 2, 3, 4, 5, 6, 7, 8, 9]

p = int(input("Digite o valor a procurar: "))
v = int(input("Digite outro valor a procurar: "))
x = 0 

achouP = False
achouV = False

while x < len(L) and (not achouP or not achouV):
    if L[x] == p:
        achouP = True
        posP = x
    if L[x] == v:
        achouV = True
        posV = x
    x += 1

if achouP and achouV:
    print(f"{p} foi achado na posição {posP} e {v} foi achado na posição {posV}")
elif achouV:
    print(f"{p} foi achado na posição {posP} e {v} não foi achado")
elif achouP: 
    print(f"{v} foi achado na posição {posV} e {p} não foi achado")
else:
    print(f"Nem {p}, nem {v} foram encontrados")
    