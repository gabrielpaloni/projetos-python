altura = float(input('Digite a altura da pessoa em metros (ex: 1.75): '))
sexo = input('Digite o sexo da pessoa ("F" para Feminino, "M" para Masculino: ').upper()
if sexo == "M":
    peso_ideal = (72.7 * altura) - 58
    print(f'O peso ideal para um homem de {altura:.2f}m é: {peso_ideal:.2f}kg.')
elif sexo == "F":
    peso_ideal = (62.1 * altura) - 44.7
    print(f'O peso ideal para uma mulher de {altura:.2f}m é: {peso_ideal:.2f}kg.')
else:
    print('Sexo inválido. Por favor, insira "F" para Feminino ou "M" para Masculino.')
