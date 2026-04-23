dias = int(input("Informe por quantos dias o carro foi alugado: "))
km = float(input("Digite quantos quilômetros o carro andou: "))

precoAPagar = dias * 60 +  0.15 * km

print(f"Total a pagar: R${precoAPagar:.2f}")