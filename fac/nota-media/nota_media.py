nota1 = float(input('Digite sua primeira nota: '))
nota2 = float(input('Digite sua segunda nota: '))
media = (nota1 + nota2) / 2
if nota1 > 10 or nota2 > 10:
    print('Nota inválida.')
elif nota1 < 0 or nota2 < 0:
    print('Nota inválida.')   
elif media >= 7:
    print('Você está aprovado! ')
else:
    print('Você está reprovado! ')
