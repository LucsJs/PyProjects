sal = float(input("Informe seu salário: R$"))
porc = float(input("Digite a porcentagem de aumento(%): "))
novoSal = sal * (1 + porc / 100) # -> sal + sal * porc / 100

print(f"Novo salário será: R${novoSal:.2f}")