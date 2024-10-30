valorNumerico = int(input('Quantos números você vai adicionar? [no máximo 100] '))
numeros = []
for i in range(valorNumerico):
    num = float(input('Informe um número: '))
    numeros.append(num)        
print(f'O maior valor é: {max(numeros)}')