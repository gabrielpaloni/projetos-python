def binary_addition(a, b):
    # Converte os números binários para inteiros
    int_a = int(a, 2)
    int_b = int(b, 2)
    
    # Soma os inteiros
    sum_result = int_a + int_b
    
    # Converte o resultado de volta para binário
    return bin(sum_result)[2:]

def binary_multiplication(a, b):
    # Converte os números binários para inteiros
    int_a = int(a, 2)
    int_b = int(b, 2)
    
    # Multiplica os inteiros
    product_result = int_a * int_b
    
    # Converte o resultado de volta para binário
    return bin(product_result)[2:]

def main():
    print("Calculadora Binária")
    print("Escolha a operação:")
    print("1. Soma")
    print("2. Multiplicação")
    
    choice = input("Digite 1 ou 2: ")
    
    if choice not in ['1', '2']:
        print("Escolha inválida!")
        return
    
    bin1 = input("Digite o primeiro número binário: ")
    bin2 = input("Digite o segundo número binário: ")
    
    # Validação básica de entrada
    if not all(c in '01' for c in bin1) or not all(c in '01' for c in bin2):
        print("Por favor, insira números binários válidos!")
        return
    
    if choice == '1':
        result = binary_addition(bin1, bin2)
        print(f"Soma de {bin1} e {bin2} é {result}")
    elif choice == '2':
        result = binary_multiplication(bin1, bin2)
        print(f"Multiplicação de {bin1} e {bin2} é {result}")

if __name__ == "__main__":
    main()
