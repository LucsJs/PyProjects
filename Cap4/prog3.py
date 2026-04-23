#calcula imposto de renda

print("==-==-==-==-==-==-==-==-==-==-==")
print(" CALCULADOR DE IMPOSTO DE RENDA ")
print("==-==-==-==-==-==-==-==-==-==-==")

salario = float(input("Salário: R$"))
tot_pagar = 0

if (salario > 3000):
    excedente = salario - 3000
    tot_pagar = tot_pagar + excedente * 35 / 100
    salario = salario - excedente

if (salario <= 3000):
    excedente = salario - 1000
    tot_pagar = tot_pagar + excedente * 20 / 100

print(f"Total a pagar de imposto: R${tot_pagar:.2f}.")
    