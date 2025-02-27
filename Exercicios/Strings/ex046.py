# programa lê duas strings e informa se a segunda está contida na primeira

stringGrande = input("Digite uma string: ")
stringPequena = input("Digite a sting a ser buscada: ")

posicao = stringGrande.find(stringPequena)

if (posicao == -1):
    print("%s não foi encontrado na string %s" % (stringPequena, stringGrande))

else:
    print("%s encontrada na posição %d de %s" % (stringPequena, posicao, stringGrande))