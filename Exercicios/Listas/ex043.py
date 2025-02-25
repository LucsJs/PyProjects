salas = [10, 2, 1, 3, 0]

while (True):
    for x, y in enumerate(salas):
        print("Assentos livres na Sala %d: %d" % (x + 1, y))

    numSala = int(input("Informe o número da sala(0 para sair): "))
    while (numSala > 5 or numSala < 0):
        print("Sala inválida! Informe um número entre 0 e 5.")
        numSala = int(input("Informe o número da sala(0 para sair): "))
    
    if (numSala == 0):
        break

    lugares = int(input("Quantidade de lugares a comprar: "))
    if (salas[numSala - 1] == 0):
        print("Sem assentos nesta sala.")
    
    elif (salas[numSala - 1] >= lugares):
        print("Seu(s) lugar(es) foi reservados com sucesso")
        salas[numSala - 1] -= lugares
        
    else:
        print("Não há esta quantidade de lugares disponíveis nesta sala.")



