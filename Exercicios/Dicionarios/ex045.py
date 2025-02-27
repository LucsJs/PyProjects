# Transforma cada caractere de uma frase em uma chave de dicionário

dicionario = {}

frase = input("Digite uma frase: ")
for letra in frase:
    if (letra != ' '):
        dicionario[letra] = 1

print(dicionario)

