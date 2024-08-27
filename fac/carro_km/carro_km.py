km = float(input('Digite a quantidade de quilômetros: '))
d = float(input('Digite a quantidade de dias alugados: '))
pt = (km * 0.20) + (d * 90)
print(f'O preço total a pagar é de R${pt:.2f}')