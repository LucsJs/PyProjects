# le duas strings e escreve outra com valores que aparecem em apenas uma das strings

string1 = input("1º string: ")
string2 = input("2º string: ")

string3 = []

for letra in string1:
    if (letra not in string2 and letra not in string3):
        string3.append(letra)

for letra in string2:
    if (letra not in string1 and letra not in string3):
        string3.append(letra)

string3 = "".join(string3)
print("3º string: %s" % string3)