valorNumerico = int(input('Quantos números inteiros você vai adicionar? [no máximo 50] '))
numeros = []
pares = []
impares = []
for i in range(valorNumerico):
    numeros.append(int(input(f'Informe o {i + 1}o. número: ')))
for i in range (valorNumerico):
    if numeros[i] % 2 == 0:
        pares.append(numeros[i])
    else:
        impares.append(numeros[i])
        
print(f'Todos os números: {numeros}')
print(f'Números pares: {pares}')
print(f'Números impares: {impares}')
