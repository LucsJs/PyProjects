soma = 0    
qtd = 0

while (True):
    num = int(input("Informe o número a ser somado (0 para sair): "))
    if (num == 0):
        break
    soma += num
    qtd += 1

if (qtd == 0):
    print("Nenhum número digitado")
else:
    print(f"Quantidade de números digitados: {qtd}")
    print(f"Soma dos números digitados é {soma}")
    print(f"A média dos números digitados é {soma / qtd:.1f}")




