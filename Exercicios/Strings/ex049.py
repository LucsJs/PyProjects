# informa quantas vezes cada caractere aparece na string 

letras = {}

string = input("String: ")

for letra in string:
    if (letra not in letras):
        letras[letra] = string.count(letra)

for caractere, quantidade in letras.items():
    print("%c: %dx" % (caractere, quantidade))