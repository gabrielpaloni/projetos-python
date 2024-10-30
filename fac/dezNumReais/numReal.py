nome = str(input('Olá, qual o seu nome? '))
contadorDeRepeticoes = 1
soma = 0
while contadorDeRepeticoes <= 10:
    valor = float(input(f'{nome}, digite o {contadorDeRepeticoes}º valor: '))
    contadorDeRepeticoes = contadorDeRepeticoes + 1
    if valor % 2 == 0:
        soma = soma + valor
print(f'A soma dos números pares é: {soma}')
        