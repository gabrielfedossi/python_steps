valor = float(input("Digite o valor da compra: "))

if valor > 100:
    desconto = valor * 0.10
    valor_final = valor - desconto
    print(f"Valor da compra: R${valor:.2f}")
    print(f"Desconto aplicado: R${desconto:.2f}")
    print(f"Valor final a pagar: R${valor_final:.2f}")  
else:
    print(f"Valor da compra: R${valor:.2f}")
    print("Desconto aplicado: R$0.00")
    print(f"Valor final a pagar: R${valor:.2f}")