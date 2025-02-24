# o usuário pode colocar quantos números quiser na lista.

numeros = []

num = int(input("Informe um número(0 para sair): "))

while(num != 0):
    numeros.append(num)
    num = int(input("Informe um número(0 para sair): "))

cont = 0
while(cont < len(numeros)):
    print(numeros[cont])
    cont += 1
