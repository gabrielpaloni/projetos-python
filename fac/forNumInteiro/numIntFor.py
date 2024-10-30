fatorial = 1
numero = int(input('Digite um número inteiro: '))
for i in range (numero, 0, -1):
    fatorial = fatorial * i
    print(f'O fatorial de {numero} x {i}')
    
print(f'é igual a {fatorial}')