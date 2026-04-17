# Escreva um programa em Python que leia o consumo de energia elétrica (em kWh) de uma      residência e calcule o valor da conta de acordo com a tabela:

#Até 100 kWh → R$ 0,50 por kWh
#De 101 a 200 kWh → R$ 0,75 por kWh
#Acima de 200 kWh → R$ 1,20 por kWh
#O programa deve calcular e exibir o valor total da conta.
preco_total = 0
while True:
    print("========== MENU ========")
    kwh = int(input("Insira o consumo de energia elétrica (em kWh) de sua residência: "))


    if kwh <= 100:
        preco = kwh * 0.50
        preco_total = preco
        break
    elif kwh >= 101 and kwh <= 200:
        preco = kwh * 0.75
        preco_total = preco
        break
    elif kwh > 200:
        preco = kwh * 1.20
        preco_total = preco
        break

print(f"O preço de sua conta será R${preco_total}")
