# Lê 7 notas e faz a média utilizando listas

notas = [0, 0, 0, 0, 0, 0, 0]

x = 0
soma = 0
while (x < 7):
    notas[x] = float(input("NOTA %d: " % (x+1)))
    soma += notas[x]
    x += 1 

print("Média do aluno é %.1f" % (soma/x))