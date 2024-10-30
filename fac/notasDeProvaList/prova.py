numeroDeAlunos = int(input('Quantas notas você vai adicionar? [no máximo 50]: '))
soma = 0
maiorQueSete = 0
menorQueSete = 0
notas = []
for i in range(numeroDeAlunos):
    notas.append(float(input(f'Informe a {i + 1}a. nota: ')))
    soma += notas[i]
    if notas[i] >= 7:
        maiorQueSete += 1
    else:
        menorQueSete += 1
media = soma / numeroDeAlunos 
porcentagemMaior = maiorQueSete / numeroDeAlunos * 100
porcentagemMenor = menorQueSete / numeroDeAlunos * 100
print(f'As notas da turma são: {notas}')
print(f'A maior nota da turma é: {max(notas)}')
print(f'A menor nota da turma é: {min(notas)}')
print(f'A média da turma é: {media:.2f}')
print(f'A porcentagem de notas maiores ou iguais a 7 é: {porcentagemMaior:.2f}%')
print(f'A porcentagem de notas menores que 7 é: {porcentagemMenor:.2f}%')