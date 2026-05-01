# 📄 ENUNCIADO
# A lanchonete Burgão 2.0 implementou um novo sistema digital de pedidos, permitindo maior flexibilidade na escolha de produtos e personalização.


# 🧾 REQUISITOS DO SISTEMA
# • Permitir ao usuário selecionar: 1 lanche (obrigatório), 1 bebida (obrigatória), 0 ou mais adicionais (opcional)
# • Calcular o valor total do pedido considerando as regras



lanches = {
    10: 18.00,
    11: 25.00,
    12: 22.00
}

bebidas = {
    50: 6.00,
    51: 8.00,
    52: 7.00
}

adicionais = {
    30: 3.00,
    31: 4.50,
    32: 2.00
}


lanche = int(input("Código do lanche: "))
bebida = int(input("Código da bebida: "))

total_lanche_bebida = lanches[lanche] + bebidas[bebida]


desconto_combo = total_lanche_bebida * 0.05
total = total_lanche_bebida - desconto_combo


while True:
    add = input("Adicionar extra? (s/n): ")
    if add.lower() == 'n':
        break
    cod = int(input("Código do adicional: "))
    total = total + adicionais[cod]


tipo = input("Entrega ou retirada? (e/r): ")

if tipo == 'e':
    if total > 60:
        frete = 0
    else:
        frete = 10
else:
    frete = 0

total += frete


pag = input("Forma de pagamento (pix/credito): ")

if pag == "pix":
    total *= 0.90  
elif pag == "credito":
    total *= 1.05  


print(f"Total a pagar: R$ {total:.2f}")