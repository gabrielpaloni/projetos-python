from math import pow
def potencia (numero1, numero2):
    return pow(numero1, numero2)

numero1 = float(input('Digite um número: '))
numero2 = float(input('Digite um outro número: '))

print('A potenciação do primeiro com o segundo número é:', potencia(numero1, numero2))