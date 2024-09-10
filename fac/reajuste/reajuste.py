sl = float(input('Qual o seu salário? '))
if sl < 500:
    ns = sl * 1.15
elif sl <= 1000:
    ns = sl * 1.10
elif sl > 1000:
    ns = + sl * 1.05
else:
    print('Não haverá reajuste.')
print(f'O novo salário é R${ns:.2f}')
