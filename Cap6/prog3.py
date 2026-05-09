ultimo = 10

fila = list(range(1, ultimo + 1))

while (True): 
    print(f"Existem {len(fila)} pessoas na fila.")
    print(fila)
    print("Aperte A para atender alguem da fila,")
    print("F para adicionar alguém ao final. S para sair.")
    operacao = input("")

    while (operacao != "A" and operacao != "F" and operacao != "S"):
        print("\nDigite uma operação válida!")
        print("Aperte A para atender alguem da fila,")
        print("F para adicionar alguém ao final. S para sair.")
        operacao = input("")

    if (operacao == "A"):
        if (len(fila) == 0):
            print("Ninguém na fila para atender. Aperte F para adicionar alguém a fila.")
        else:
            print(f"{fila.pop(0)} foi atendido.")
        
    elif (operacao == "F"):
        ultimo += 1
        fila.append(ultimo)

    else:
        break

    print()

    

