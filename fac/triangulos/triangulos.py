seg1 = float(input('Digite o primeiro segmento: '))
seg2 = float(input('Digite o segundo segmento: '))
seg3 = float(input('Digite o terceiro segmento: '))
if seg1 < seg2 + seg3 and seg2 < seg1 + seg3 and seg3 < seg1 + seg2:
    if seg1 == seg2 == seg3:
        print('Os segmentos formam um triângulo equilátero.')
    elif seg1 == seg2 or seg2 == seg3 or seg1 == seg3:
        print('Os segmentos formam um triângulo isósceles.')
    else:
        print('Os segmentos formam um triângulo escaleno.')
else:
    print('Os segmentos não podem formar um triângulo.')