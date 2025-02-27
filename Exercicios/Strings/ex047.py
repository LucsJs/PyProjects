# faz uma intersecção de caracteres entre duas strings

string1 = input("1º string: ")
string2 = input("2º string: ")

interseccao = []

for letra in string2:
    if (letra in string1 and letra not in interseccao):
        interseccao.append(letra)

interseccao = "".join(interseccao)

print("Resultado: %s" % interseccao)