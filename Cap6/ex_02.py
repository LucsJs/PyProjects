l1 = []
l2 = []
i = 0
num = int(input(f"Digite o {i + 1}º inteiro da primeira lista (0 para sair): ")) 
while (num != 0):
    l1.append(num)
    i += 1
    num = int(input(f"Digite o {i + 1}º inteiro da primeira lista (0 para sair): ")) 


i = 0
num = int(input(f"Digite o {i + 1}º inteiro da segunda lista (0 para sair): ")) 
while (num != 0):
    l2.append(num)
    i += 1
    num = int(input(f"Digite o {i + 1}º inteiro da segunda lista (0 para sair): ")) 

l = l1[:]
l.extend(l2)
print(f"a lista com todos os valores digitados fica {l}")