kWhConsumida = float(input('Qual a quantidade de kWh consumida? '))
tipoDeInstalacao = str(input('A instalação utilizada foi Residêncial, indústrial ou Comercial? (R/I/C): ')).upper()
match tipoDeInstalacao:
    case 'R':
        if kWhConsumida <= 500:
            valor = kWhConsumida * 0.40
            print(f'O valor a pagar é de R${valor} ')
        else:
            kWhConsumida > 500
            valor = kWhConsumida * 0.65
            print(f'O valor a pagar é de R${valor} ')
    case 'I':
        if kWhConsumida <= 5000:
            valor = kWhConsumida * 0.55
            print(f'O valor a pagar é de R${valor} ')
        else:
            kWhConsumida > 5000
            valor = kWhConsumida * 0.60
            print(f'O valor a pagar é de R${valor} ')
    case 'C':
        if kWhConsumida <= 1000:
            valor = kWhConsumida * 0.55
            print(f'O valor a pagar é de R${valor} ')
        else:
            kWhConsumida > 1000
            valor = kWhConsumida * 0.60
            print(f'O valor a pagar é de R${valor} ')
    case _:
        print("Tipo de instalação inválida! ")
