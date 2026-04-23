velocidade = float(input("Velocidade do motorista (Km/h): "))
if (velocidade > 80):
    excesso = velocidade - 80
    multa = excesso * 5
    
    print(f"O motorista deve pagar R${multa:.2f} de multa.")

if (velocidade <= 80):
    print("Motorista dentro do limite.")