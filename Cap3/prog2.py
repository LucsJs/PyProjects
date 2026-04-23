p1X = float(input("X do ponto 1: "))
p1Y = float(input("Y do ponto 1: "))

p2X = float(input("X do ponto 2: "))
p2Y = float(input("Y do ponto 2: "))

dist = ((p1X - p2X) ** 2 + (p1Y - p2Y) ** 2) ** (1/2)

print(f"A Distãnia entre os dois pontos é {dist:.1f}")