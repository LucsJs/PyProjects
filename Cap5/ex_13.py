divida = float(input("Preço da dívida: R$"))
juros_mensal = float(input("Juros mensal (%): "))

pagamento_mensal = float(input("Valor a ser pago mensalmente: R$"))


if (divida * juros_mensal / 100 >= pagamento_mensal):
    print("Você nunca vai conseguir pagar essa dívida com esse valor pago mensalmente.")
else:
    meses = 0
    tot_a_pagar = divida

    while(tot_a_pagar >= 0):
        meses = meses + 1
        tot_a_pagar = tot_a_pagar + divida * juros_mensal / 100
        tot_a_pagar = tot_a_pagar - pagamento_mensal

    total_pago = meses * pagamento_mensal 
    tot_juros = total_pago - divida
    

    print(f"Você pagaŕa esta dívida em {meses} meses, pagará no total R${total_pago:.2f} e pagará R${tot_juros:.2f} de juros.")
        
