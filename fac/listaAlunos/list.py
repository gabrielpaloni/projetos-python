numeroDeAlunos = int(input('Quantas notas você vai adicionar? [no máximo 50] '))
notas = []
maiorQueSete = []
for i in range(numeroDeAlunos):
    nota = float(input('Informe a nota do aluno: '))
    notas.append(nota)
    if nota >= 7:
        maiorQueSete.append(nota)        
print(f'A quantidade de alunos com média maior ou igual a 7 é: {len(maiorQueSete)}')