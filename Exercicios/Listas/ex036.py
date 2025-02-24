# Simulação de fila de banco

ultimo1 = 10
ultimo2 = 10
fila1 = list(range(1, ultimo1 + 1))
fila2 = list(range(1, ultimo2 + 1))

while (True):
    print("\nExistem %d clientes na fila 1" % len(fila1))
    print("Fila 1 atual:", fila1)
    print("\nExistem %d clientes na fila 2" % len(fila2))
    print("Fila 2 atual:", fila2)
    print("\nDigite F para adicionar um cliente ao fim da fila 1 e G para fila 2,")
    print("ou A para realizar o atendimento na fila 1 e B para fila 2. S para sair.")
    sequencia = input("Operação (F, A, S, B ou G): ")
    
    i = 0
    while(i < len(sequencia)):
        operacao = sequencia[i]
        if (operacao == 'A'):
            if (len(fila1) > 0):
                atendido = fila1.pop(0)
                print("Cliente %d da fila 1 atendido." % atendido)

            else:
                print("Fila vazia! Ninguém para atender.")

        elif (operacao == 'F'):
            ultimo1 += 1
            fila1.append(ultimo1)

        elif (operacao == 'B'):
            if (len(fila2) > 0):
                atendido = fila2.pop(0)
                print("Cliente %d  da fila 2 atendido." % atendido)

            else:
                print("Fila vazia! Ninguém para atender.")

        elif (operacao == 'G'):
            ultimo2 += 1
            fila2.append(ultimo2)

        elif (operacao == 'S'):
            break

        else:
            print("Operação válida! Digite apenas F, A, S, B ou G ")
        
        i += 1
    
    if (operacao == 'S'):
        break
