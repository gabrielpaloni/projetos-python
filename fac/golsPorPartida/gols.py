nomeTime1 = str(input('Olá, Qual o nome do time da Casa? '))
nomeTime2 = str(input('E qual o nome do time de fora? '))
time1 = int(input(f'Quantos gols o {nomeTime1} fez? '))
time2 = int(input(f'Quantos gols o {nomeTime2} fez? '))
if time1 > time2:
    numeroMaior = time1
    numeroMenor = time2
    timeVencedor = nomeTime1
else:
    numeroMaior = time2
    numeroMenor = time1
    timeVencedor = nomeTime2

diferencaDeGols = numeroMaior - numeroMenor

if diferencaDeGols == 0:
    print(f'O jogo resultou no empate de {nomeTime1} e {nomeTime2}!')
elif diferencaDeGols <= 3:
    print(f'A partida resultou num placar normal de jogo.')
    print(f'O resultado foi de {numeroMaior} a {numeroMenor} para o {timeVencedor}')
else:
    print(f'A partida resultou numa goleada!')
    print(f'O resultado foi de {numeroMaior} a {numeroMenor} para o {timeVencedor}')
