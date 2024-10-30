numero = int(input('Digite um número: '))
contador = 0
for i in range (2, numero):
    if numero % 1 == 0:
        contador = contador + 1
        break
    if contador == 0:
        print (f'{numero} é primo')
    else:
        print(f'{numero} não é primo')