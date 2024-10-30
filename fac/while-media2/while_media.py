turma = str(input('Digite o nome da turma: '))
soma = 0
contadorDeNotas = 0
print('AVISO!')
print('Digite "-1" para terminar a contagem das notas')

while True:
    valor = float(input(f'Digite a {contadorDeNotas + 1}ª nota: '))
    if valor == -1:
        break
    soma = soma + valor
    contadorDeNotas = contadorDeNotas + 1

if contadorDeNotas > 0:
    media = soma / contadorDeNotas
    print(f'A média da turma {turma} é: {media:.2f}')
else:
    print(f'Nenhuma nota foi registrada para a turma {turma}.')
