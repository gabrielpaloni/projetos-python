km = float(input('Qual a distância que deseja percorrer? (em km): '))
if km > 200:
    p = 0.45 * km
else:
    p = 0.50 * km
print(f'O valor total será de R${p:.2f}')
