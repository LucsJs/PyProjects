# Calcula redução de vida de um fumante, pergunta quantos anos fumando e quantos cigarros por dia
#10min/cigarro  e exibir total em dias

ano = int(input("Informe a quantos anos você fuma: "))
cigDia = int(input("Digite a quantidade de cigarros fumados por dia: "))

cigarros = ano * 365 * cigDia
minutos = cigarros * 10
dias = (minutos / 60) / 24

print("Você perdeu %.0f dias de vida" % dias)