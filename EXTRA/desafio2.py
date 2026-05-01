# 📄 ENUNCIADO
# A lanchonete Burgão 2.0 implementou um novo sistema digital de pedidos, permitindo maior flexibilidade na escolha de produtos e personalização.


# 🧾 REQUISITOS DO SISTEMA
# • Permitir ao usuário selecionar: 1 lanche (obrigatório), 1 bebida (obrigatória), 0 ou mais adicionais (opcional)
# • Calcular o valor total do pedido considerando as regras
print("===== CARDÁPIO =======")
print("LANCHES:")
print("10 → Burgão Clássico → R$ 18.00")
print("11 → Burgão Duplo → R$ 25.00")
print("12 → Burgão Veggie → R$ 22.00")

print("BEBIDAS")
print("50 → Refrigerante → R$ 6.00")
print("51 → Suco Natural → R$ 8.00")
print("52 → Chá Gelado → R$ 7.00")





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
    print("ADICIONAIS:")
    print("30 → Queijo extra → R$ 3.00")
    print("31 → Bacon → R$ 4.50")
    print("32 → Molho especial → R$ 2.00")
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

total = total + frete


pag = input("Forma de pagamento (pix/credito): ")

if pag == "pix":
    total = total * 0.90  
elif pag == "credito":
    total = total * 1.05  


print(f"Total a pagar: R$ {total:.2f}")