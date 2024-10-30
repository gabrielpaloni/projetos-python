salario = float(input('Digite seu salário: '))
prestacaoEmprestimo = float(input('Digite o valor da prestação do empréstimo: '))
if prestacaoEmprestimo > salario * 0.20:
    print('Empréstimo não concedido.')
else:
    print('Empréstimo concedido.')