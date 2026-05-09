l = []

i = 0
num = int(input(f"Digite o {i + 1}º inteiro (0 para sair): ")) 
while (num != 0):
    l.append(num)
    i += 1
    num = int(input(f"Digite o {i + 1}º inteiro (0 para sair): ")) 

x = 0
while (x < len(l)):
    print(l[x])
    x += 1

