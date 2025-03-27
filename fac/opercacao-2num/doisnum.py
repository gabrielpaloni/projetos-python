numero1 = float(input('Digite o primero número: '))
numero2 = float(input('Digite o segundo número: '))
print('1. Soma')
print('2. Subtração')
print('3. Multiplicação')
print('4. Divisão')
tipoDeOperacao = input('Escolha sua operação: (1, 2, 3 ou 4) ')
if tipoDeOperacao not in ['1', '2', '3', '4']:
    print("Escolha inválida!")
else:
    match tipoDeOperacao:
        case '1':
            resultado = numero1 + numero2
            print(f'O  resultado da soma é: {resultado} ')
        case '2':
            resultado = numero1 - numero2
            print(f'O  resultado da subtração é: {resultado} ')
        case '3':
            resultado = numero1 * numero2
            print(f'O  resultado da multiplicação é: {resultado} ')
        case '4':
            if numero2 == 0 or numero1 == 0:
                print('Não é possível dividir por 0. ')
            else:
                resultado = numero1 / numero2
                print(f'O  resultado da divisão é: {resultado} ')
                