tipo_instalacao = input("Tipo de instalação (R para residencial, I para industrial e C para comércio): ")

if (tipo_instalacao != "R" and 
    tipo_instalacao != "r" and 
    tipo_instalacao != "I" and 
    tipo_instalacao != "i" and 
    tipo_instalacao != "C" and 
    tipo_instalacao != "c"):
    print("Digite uma instalação válida(R, I ou C)!")

else: 
    kWh = float(input("Quantidade de kWh consumido: "))

    if (tipo_instalacao == "R" or tipo_instalacao == "r"):
        if (kWh <= 500):
            preco = 0.4
        else:
            preco = 0.65
    elif (tipo_instalacao == "I" or tipo_instalacao == "i"):
        if (kWh <= 1000):
            preco = 0.55
        else:
            preco = 0.60
    else:
        if (kWh <= 5000):
            preco = 0.55
        else:
            preco = 0.60

    tot_pagar = preco * kWh

    print(f"Total a pagar: R$ {tot_pagar:.2f}")

