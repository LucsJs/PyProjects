ultimo = 10
fila = list(range(1, ultimo + 1))

while (True):
    print(f"Existem {len(fila)} pessoas na fila.")
    print(fila)
    print("Aperte A para atender alguem da fila,")
    print("F para adicionar alguém ao final. S para sair.")
    comandos = input("Digite a sequência de comandos: ")

    i = 0
    mensagemMostrada = False
    while (i < len(comandos)):
        if (comandos[i] == "A"):
            if (len(fila) == 0):
                if (not mensagemMostrada):
                    print("Ninguém na fila para atender. Aperte F para adicionar alguém a fila.")
                    mensagemMostrada = True
            else:
                print(f"{fila.pop(0)} foi atendido.")
                mensagemMostrada = False

        elif (comandos[i] == "F"):
            ultimo += 1
            fila.append(ultimo)

        else:
            break

        i += 1

    print()
    if (i != len(comandos)):
        break
