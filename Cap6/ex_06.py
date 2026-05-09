ultimo1 = ultimo2 = 10

fila1 = list(range(1, ultimo1 + 1))
fila2 = list(range(1, ultimo2 + 1))

while (True): 
    print(f"Existem {len(fila1)} pessoas na fila 1.")
    print(fila1)

    print(f"Existem {len(fila2)} pessoas na fila 2.")
    print(fila2)

    print("Aperte A para atender alguem da fila 1 ou B para fila 2,")
    print("F para adicionar alguém ao final da fila 1 e G para fila 2. S para sair.")
    operacao = input("Comando: ")

    while (operacao != "A" and operacao != "F" and operacao != "S" and operacao != "B" and operacao != "G"):
        print("\nDigite uma operação válida!")
        print("Aperte A para atender alguem da fila 1 ou B para fila 2,")
        print("F para adicionar alguém ao final da fila 1 e G para fila 2. S para sair.")
        operacao = input("Comando: ")

    if (operacao == "A"):
        if (len(fila1) == 0):
            print("Ninguém na fila 1 para atender. Aperte F para adicionar alguém a fila 1.")
        else:
            print(f"{fila1.pop(0)} foi atendido.")

    elif (operacao == "B"):
        if (len(fila2) == 0):
            print("Ninguém na fila 2 para atender. Aperte G para adicionar alguém a fila 2.")
        else:
            print(f"{fila2.pop(0)} foi atendido.")
        
    elif (operacao == "F"):
        ultimo1 += 1
        fila1.append(ultimo1)

    elif (operacao == "G"):
        ultimo2 += 2
        fila2.append(ultimo2)

    else:
        break

    print()

    

