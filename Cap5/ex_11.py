deposito = float(input("Depósito inicial: R$"))
taxa = float(input("Taxa de juros mensal (%): "))
dep_mensal = float(input("Valor de depósito mensal: R$"))

cont = 1
dinheiro = deposito
while (cont <= 24):
    dinheiro = dinheiro * (1 + taxa/100)
    print(f"Dinheiro no {cont}º mês: R${dinheiro:.2f}")
    cont = cont + 1
    dinheiro = dinheiro + dep_mensal

print(f"Total ganhado com juros foi R${dinheiro - deposito:.2f}")