salario = float(input("Informe seu salário: R$ "))

if (salario <= 1250):
    aum = 15

if (salario > 1250):
    aum = 10

salario_aum = salario + salario * aum / 100

print(f"Salário com aumento fica R$ {salario_aum:.2f}")