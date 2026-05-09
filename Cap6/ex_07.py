pilha = []

parenteses = input("Digite a sequência de parênteses: ")

estaEmOrdem = True
i = 0
while i < len(parenteses):
    if parenteses[i] == "(":
        pilha.append(parenteses[i])
    elif len(pilha) > 0:
        pilha.pop(-1)
    else:
        estaEmOrdem = False
        break
    i += 1

if len(pilha) > 0 or not estaEmOrdem:
    print("Os parênteses NÃO estão na ordem correta.")
else:
    print("Os parênteses estão na ordem correta.")


