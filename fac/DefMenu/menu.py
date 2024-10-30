import time

def menu():
    print('1. Fatorial')
    print('2. Tabuada')
    print('3. Par ou Impar')
    print('4. Sair')


def fatorial(numero):
    fat = 1
    for i in range(1, numero + 1):
        fat = fat * i
    return fat


def tabuada(numero):
    print(f'A tabuada de {numero}')
    for i in range(1, 11):
        print(f'{numero} x {i} = {numero * i}')


def ParImpar(numero):
    if numero % 2 == 0:
        return print(f'{numero} é par')
    else:
        return print(f'{numero} é ímpar')


def main():
    numero = int(input('Digite um número: '))
    
    while True:
        print('\nCarregando o menu, por favor, aguarde', end='')
        for _ in range(3):
            time.sleep(0.3)
            print('.', end='')
        print(' ') 
        print(' ')
        menu()
        
        opcao = input('Escolha uma opção (1-4): ')
        print(' ')
        match opcao:
            case '1':
                fatorial(numero)
                print(f'O fatorial de {numero} é:', fatorial(numero))
            case '2':
                tabuada(numero)
            case '3':
                ParImpar(numero)
            case '4':
                print('\nSaindo do sistema', end='')
                for _ in range(3):
                    time.sleep(0.5)
                    print('.', end='')
                break 
            case _:
                print('Opção inválida, por favor, tente novamente!')

if __name__ == "__main__":
    main()

    
    
    
