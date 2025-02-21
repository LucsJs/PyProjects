# Calcula novo salário com salário atual e a taxa de aumento

salario = float(input("Informe seu salário: "))
aum = float(input("Digite a taxa de aumento: "))

novo_sal = salario + salario * aum/100

print("Seu salário aumentado fica R$ %.2f" % novo_sal)