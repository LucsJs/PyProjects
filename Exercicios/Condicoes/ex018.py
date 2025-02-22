# Pergunta salario e retorna valor do aumento
# salario>R$1250 aumento é de 10%, do contrário 15%

salario = float(input("Informe seu salário: R$ "))

if (salario > 1250):
    aum = 10

if (salario <= 1250):
    aum = 15

valorAumento = salario * aum/100
novoSalario = salario + valorAumento

print("Valor do aumento é R$ %.2f e salário aumentado fica R$ %.2f" % (valorAumento, novoSalario))