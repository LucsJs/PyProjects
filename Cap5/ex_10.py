ponto = 0
questao = 1

while (questao <= 3):
    resposta = input(f"Reposta da questão {questao}: ")
    if (questao == 1 and (resposta == "b" or resposta == "B")):
        ponto = ponto + 1

    if (questao == 2 and (resposta == "a" or resposta == "A")):
        ponto = ponto + 1

    if (questao == 3 and (resposta == "d" or resposta == "D")):
        ponto = ponto + 1

    questao = questao + 1

print(f"O aluno fez {ponto} pontos.")