try:
    num = int(input("Insira um valor inteiro: "))
    print(f"\nEsse é o valor inteiro digitado: {num}")

except ValueError:
    print("\nO valor inserido não é um número inteiro")