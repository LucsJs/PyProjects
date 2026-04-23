val = int(input("Informe o valor: R$"))
dinheiro = val

nota100 = 0
nota50 = 0
nota20 = 0
nota10 = 0
nota5 = 0
nota1 = 0

nota100 = dinheiro // 100
dinheiro %= 100

nota50 = dinheiro // 50
dinheiro %= 50

nota20 = dinheiro // 20
dinheiro %= 20

nota10 = dinheiro // 10
dinheiro %= 10

nota5 = dinheiro // 5
dinheiro %= 5

nota1 = dinheiro

print(f"Para pagar o valor de R${val:.2f} é necessário: ")

if (nota100 > 0):
    print(f"{nota100} notas de 100 reais")

if (nota50 > 0):
    print(f"{nota50} notas de 50 reais")

if (nota20 > 0):
    print(f"{nota20} notas de 20 reais")

if (nota10 > 0):
    print(f"{nota10} notas de 10 reais")

if (nota5 > 0):
    print(f"{nota5} notas de 5 reais")

if (nota1 > 0):
    print(f"{nota1} notas de 1 real")
