import time 

def typewriter(text, delay=0.05):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)

typewriter('Olá, qual o seu nome? ')
nome = str(input()) 

typewriter(f'{nome}, escreva um número inteiro e positivo: ')
numeroInteiro = int(input()) 
x = 0
while x <= numeroInteiro:
    print(x, end=' ', flush=True)
    time.sleep(0.1)
    x = x + 1

print()
typewriter(f'Parei no {numeroInteiro} como foi solicitado.')