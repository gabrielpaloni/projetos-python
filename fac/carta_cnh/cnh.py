ano = int(input('Digite o ano do seu nascimento: '))
ano_atual = int(input('Digite o ano atual: '))
niver = input('Você já fez aniversário esse ano? (s/n): ').strip().lower()
idade = ano_atual - ano
if niver == 'n':
    idade -= 1
if idade >= 18:
    print('Você pode tirar sua CNH.')
else:
    print('Você não pode tirar sua CNH ainda.')
