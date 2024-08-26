km = float(input('Digite sua velocidade: '))
if km > 80:
    x = km - 80
    multa = 5 * x
    print(f'Sua multa é de R${multa:.2f}')
else:
    print('Você está na velocidade permitida!')
    
        