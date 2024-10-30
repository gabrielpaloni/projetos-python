nome = str(input("Olá, qual o seu nome? "))
print(f"Bem vindo(a), {nome}!")
precoProduto = float(input("Qual o preço do produto? "))
metodoDePagamento = str(
    input("Qual será o método de pagamento? (PIX/CARTÃO DE CRÉDITO): ")).lower()
if metodoDePagamento == "pix":
    precoTotalPix = precoProduto - (precoProduto * (15/100))
    print(f"O preço total será de: R${precoTotalPix}")
else:
    parcelar = str(input("O pagamento será parcelado? (SIM/NÃO) ")).lower()
    if parcelar == "sim" or parcelar == "s":
        quantidadeDeParcelas = int(
            input("Em quantas vezes? (2 ou 3 vezes?): "))
        if quantidadeDeParcelas == 2:
            valorDaParcelaCartao = precoProduto / 2
            print(f"O valor da parcela será de: R${valorDaParcelaCartao:.2f}")
            print(f"O preço total será de: R${precoProduto}")
        else:
            precoTotalCartao = precoProduto + (precoProduto * (10/100))
            valorDaParcelaCartao = precoTotalCartao / 3
            print(f"O valor da parcela será de: R${valorDaParcelaCartao:.2f}")
            print(f"O preço total será de: R${precoTotalCartao}")
    else:
        precoTotalCartao = precoProduto - (precoProduto * (10/100))
        print(f"O preço total será de: R${precoTotalCartao}")
            