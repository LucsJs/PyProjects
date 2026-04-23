categoria = int(input("Categoria do produto: "))
if (categoria == 1):
    preco = 10
elif (categoria == 2):
    preco = 18
elif (categoria == 3):
    preco = 23
elif (categoria == 4):
    preco = 26
elif (categoria == 5):
    preco = 31
else:
    preco = 0



if (preco == 0):
    print("Informe uma categoria válida!")
else:
    print(f"O preço desse produto é {preco}")