cigarros_dia = float(input('Digite quantos cigarros você fuma por dia: '))
anos_fumando = float(input('Digite a quantos anos você fuma: '))
cigarros_totais = cigarros_dia * (365 * anos_fumando)
minutos_perdidos = cigarros_totais * 10
dias_perdidos = minutos_perdidos / 1440
print(f'Você perdeu {dias_perdidos:.0f} dias de vida.')