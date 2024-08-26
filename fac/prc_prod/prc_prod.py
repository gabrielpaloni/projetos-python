Preco_produto = float(input('Digite o preço do produto: '))
Preco_real = Preco_produto * (5/100)
resultado = Preco_produto - Preco_real
print(f'O preço com 5% de desconto é: {resultado:.2f}R$')