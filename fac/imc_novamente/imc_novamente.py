from math import pow
peso = float(input('Digite seu peso (kg): '))
altura = float(input('Digite sua altura (m): '))
imc = peso / pow(altura, 2)
if imc < 18.5:
    print(f'Seu imc é {imc:.2f}')
    print('Você está abaixo do peso ideal.')
elif imc < 24.9:
    print(f'Seu imc é {imc:.2f}')
    print('Parabéns! Você está em seu peso normal!')
elif imc < 29.9:
    print(f'Seu imc é {imc:.2f}')
    print('Você está acima do seu peso (sobrepeso).')
elif imc < 34.9:
    print(f'Seu imc é {imc:.2f}')
    print('Obesidade grau I.')
elif imc < 39.9:
    print(f'Seu imc é {imc:.2f}')
    print('Obesidade grau II')
elif imc > 40.0:
    print(f'Seu imc é {imc:.2f}')
    print('Obesidade grau III')
else:
    print('Erro ao calcular o IMC')
