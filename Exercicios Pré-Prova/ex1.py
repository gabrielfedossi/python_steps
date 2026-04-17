# 1 - Desenvolva um programa em Python que leia o preço de um produto e o valor de um desconto em reais.
#O programa deve verificar se o desconto é maior do que 30% do preço do produto.

#Se for, exiba: "Desconto inválido"
#Caso contrário, exiba: "Desconto aplicado"


produto = float(input("Insira o valor do produto R$: "))
desconto = float(input("Insira o valor de desconto R$: "))

porcentagem = (desconto * 100) / produto

if porcentagem > 30:
    print("Desconto inválido")
elif porcentagem < 30:
    print("Desconto aplicado")
else:
    print("Sem desconto")