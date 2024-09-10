idade = int(input('Digite a sua idade: '))
if idade < 16:
    print('Você não pode votar e nem dirigir.')
elif idade >= 16 and idade < 18:
    print('Você pode votar, mas não pode dirigir.')
else:
    print('Você pode votar e dirigir.')