

while True:
    try:
        num = int(input("Insira um valor inteiro: "))
        valor_num = int(num)
        print(f"Número digitado: {valor_num}")
        break
    except ValueError:
        print("\nEsse valor não é inteiro")

    