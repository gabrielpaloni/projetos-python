from math import pi,pow
raio = int(input('Digite o raio do círculo: '))
print('1. Diâmetro')
print('2. Comprimento')
print('3. Área')
escolhaDeCalculo = int(input('Escolha o cálculo desejado: '))

match escolhaDeCalculo:
    case 1:
        diametro = 2 * raio
        print(f'O diâmetro do círculo é {diametro:.2f}')
    case 2:
        comprimento = 2 * pi * raio
        print(f'O comprimento do círculo é {comprimento:.2f}')
    case 3:
        area = pi * (raio * raio)
        print(f'A área do círculo é {area:.2f}')
    case _:
        print('Escolha inválida')
        exit()
