# le duas strings e gera uma terceira que é a primeira sem os elementos da segunda

string1 = input("1º string: ")
string2 = input("2º string: ")

string1Lista = list(string1)

for letra in string2:
    pos = "".join(string1Lista).find(letra)
    while (pos != -1):
        del string1Lista[pos]
        pos = "".join(string1Lista).find(letra, pos)

string3 = "".join(string1Lista)
print("3º string: %s" % string3)
