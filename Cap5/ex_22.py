SOMA = '+'
SUBTRACAO = '-'
MULTIPLICACAO = '*'
DIVISAO = '/'
SAIDA = '0'

while (True):
    print("OPÇÕES DE TABUADA")
    print(f"[{SOMA}] para soma;")
    print(f"[{SUBTRACAO}] para subtração;")
    print(f"[{MULTIPLICACAO}] para multiplicação;")
    print(f"[{DIVISAO}] para divisão;")
    print(f"[{SAIDA}] para sair.")
    
    operacao = input("Informe a operação: ")
    while (operacao != SOMA and operacao != SUBTRACAO and operacao != DIVISAO and operacao != MULTIPLICACAO and operacao != SAIDA):
        print("=-="*7)
        print("Operação inválida!")
        print(f"[{SOMA}] para soma;")
        print(f"[{SUBTRACAO}] para subtração;")
        print(f"[{MULTIPLICACAO}] para multiplicação;")
        print(f"[{DIVISAO}] para divisão;")
        print(f"[{SAIDA}] para sair.")
        
        operacao = input("Informe a operação: ")
    

    if (operacao == SAIDA):
        break

    num = int(input("Digite o número inteiro a ser tabuado: "))

    i = 1
    if (operacao == SOMA):
        while (i <= 10):
            print(f"{num} + {i:-2} = {num + i}")
            i += 1
    elif (operacao == SUBTRACAO):
        while (i <= 10):
            print(f"{num} - {i:-2} = {num - i}")
            i += 1
    elif (operacao == MULTIPLICACAO):
        while (i <= 10):
            print(f"{num} * {i:-2} = {num * i}")
            i += 1
    else:
        while (i <= 10):
            print(f"{num} / {i:-2} = {num / i}")
            i += 1
    print("=-=" * 9)