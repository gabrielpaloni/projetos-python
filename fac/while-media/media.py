nome = str(input('Olá, qual o seu nome? '))
soma = 0
contadorDeRepeticoes = 1
valor = 1
while valor != 0:
    valor = int(input(f'{nome}, digite o {contadorDeRepeticoes}º valor: '))
    if valor != 0:
        soma = soma + valor
        contadorDeRepeticoes = contadorDeRepeticoes + 1
media = soma / contadorDeRepeticoes
print(f'Sua média é: {media}')
print(f'A soma dos números é: {soma}')
