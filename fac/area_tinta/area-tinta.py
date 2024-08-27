L = float(input('Digite a largura: '))
H = float(input('Digite a altura: '))
A = H * L
print(f'Área é: {A}m²')
tinta = A / 2
if tinta % 1 != 0:
    tinta = int(tinta) + 1
else:
    tinta = int(tinta)
print(f'A quantidade de baldes de tinta necessária é: {tinta} baldes')

