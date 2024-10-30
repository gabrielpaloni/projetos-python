somaDosNumeros = 0
numeroMaior = -2
contadorDeRepeticoes = 1
nome = str(input('Olá, digite seu nome: '))
while contadorDeRepeticoes <= 5:
    valor = int(input(f'{nome}, digite o {contadorDeRepeticoes}º valor: '))
    somaDosNumeros = somaDosNumeros + valor
    if valor > numeroMaior:
        numeroMaior = valor
    contadorDeRepeticoes = contadorDeRepeticoes + 1
print(f'A soma dos valores é: {somaDosNumeros:.0f}')
print(f'O maior valor digitiado foi: {numeroMaior:.0f}')
