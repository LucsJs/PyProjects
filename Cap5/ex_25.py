n = int(input("Digite um número a ser calculada a raiz quadrada: "))

b = 2
p = (b + (n / b)) / 2.0
print(p)
b = p

while (((n - (p ** 2)) ** 2) ** (1/2) >= 0.0001): # essa fórmula é pra ver se a diferença abs entre n e p² era >= 0.0001,
    p = (b + (n / b)) / 2.0                       # mas como não posso usar abs() então elevei a diferença ao quadrado e tirei a raiz
    print(p)
    b = p

print(f"A raiz quadrada de {n} é {p}")



