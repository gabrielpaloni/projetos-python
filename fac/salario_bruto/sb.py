ht = float(input('Digite as horas trabalhadas no mês: '))
vh = float(input('Digite o valor da hora aula: '))
tx = float(input('Digite o valor do percentual de desconto do INSS: '))
sb = ht * vh
print(f'O salário bruto é: R${sb:.2f}')
disc = sb * (tx / 100)
sl = sb - disc
print(f'O salário liquido é: R${sl:.2f}')
