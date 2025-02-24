# (())        OK
# ()()(()())  OK
# ())         Erro
# Usando pilhas

sequencia = input("Digite a sequência de parêntes: ")
seqPilha = []
pilha = []
i = 0
isErro = False
while (i < len(sequencia)):
    seqPilha.append(sequencia[i])
    i += 1

cont = len(seqPilha) - 1
while (cont >=  0):
    parenteses = seqPilha.pop(-1)
    if (parenteses == ')'):
        pilha.append(parenteses)
    
    else:
        if (len(pilha) > 0):
            if (pilha[-1] == ')'):
                del pilha[-1]
            
            else:
                isErro = True
                break
        else:
            isErro = True
            break
    
    cont -= 1


if (isErro or len(pilha) > 0):
    print("Erro")

else:
    print("OK")
    

