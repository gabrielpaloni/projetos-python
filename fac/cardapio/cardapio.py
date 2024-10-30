CodigoProduto = int(input('Digite o código do produto: '))
quantidadeDoPedido = int(input(f'Quantos do produto {CodigoProduto} o cliente deseja? '))
listaProdutos = [CodigoProduto]
if CodigoProduto == 100 in listaProdutos:
    precoTotal = quantidadeDoPedido * 1.20
    print(f'O preço do pedido é: RS{precoTotal:.2f} ')
elif CodigoProduto == 101 in listaProdutos:
    precoTotal = quantidadeDoPedido * 1.30
    print(f'O preço do pedido é: RS{precoTotal:.2f} ')
elif CodigoProduto == 102 in listaProdutos:
    precoTotal = quantidadeDoPedido * 1.50
    print(f'O preço do pedido é: RS{precoTotal:.2f} ')
elif CodigoProduto == 103 in listaProdutos:
    precoTotal = quantidadeDoPedido * 1.20
    print(f'O preço do pedido é: RS{precoTotal:.2f} ')
elif CodigoProduto == 104 in listaProdutos:
    precoTotal = quantidadeDoPedido * 1.70
    print(f'O preço do pedido é: RS{precoTotal:.2f} ')
elif CodigoProduto == 105 in listaProdutos:
    precoTotal = quantidadeDoPedido * 2.20
    print(f'O preço do pedido é: RS{precoTotal:.2f} ')
elif CodigoProduto == 106 in listaProdutos:
    precoTotal = quantidadeDoPedido * 1.00
    print(f'O preço do pedido é: RS{precoTotal:.2f} ')
else:
    print('Produto não encontrado.')

