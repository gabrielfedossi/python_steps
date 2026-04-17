saldo = 1000

while saldo > 0:
    saque = float(input("Insira o valor do saque R$: "))
    saldo = saldo - saque
    print("Saldo atual R$:", saldo)
else:
    print("Acabou o dinheiro!")
