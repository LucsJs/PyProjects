# le 3 strings e substitui na primeira, os caracteres da segunda pela terceira

string1 = input("1º string: ")
string2 = input("2º string: ")
string3 = input("3º string: ")

string1Lista = list(string1)

for x in range(len(string2)):
    pos = string1.find(string2[x])
    while (pos != -1):
        string1Lista[pos] = string3[x]
        pos = string1.find(string2[x], pos + 1)
    
resultado = "".join(string1Lista)

print("Resultado:", resultado)