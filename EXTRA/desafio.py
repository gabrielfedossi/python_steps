# Você foi contratado para desenvolver um sistema simples de vendas para uma loja online.
# 📋 O SISTEMA DEVE PERMITIR:
# • Escolher um produto
# • Escolher a forma de entrega
# • Escolher a forma de pagamento
# • Ver o valor final da compra


entrega_escolhida = ""
pagamento_escolhido = ""
produto_escolhido = ""
valor = 0

while True:
    print("====== LOJA ELETRONICA ======")
    print("1 - Fone Bluetooth - R$ 120.00")
    print("2 - Teclado Mecânico - R$ 250.00")
    print("3 - Mouse Gamer - R$ 80.00")
    print("4 - Webcam HD - R$ 150.00")
    print("0 - Sair")

    try:
        opcao = int(input("Selecione um produto: "))
    except:
        print("Digite um número válido")
        continue

    if opcao == 0:
        break

    elif opcao == 1:
        produto_escolhido = "Fone Bluetooth"
        valor = valor + 120.00

    elif opcao == 2:
        produto_escolhido = "Teclado Mecânico"
        valor = valor + 250.00

    elif opcao == 3:
        produto_escolhido = "Mouse Gamer"
        valor = valor + 80.00

    elif opcao == 4:
        produto_escolhido = "Webcam HD"
        valor = valor + 150.00

    else:
        print("Insira uma opção válida")
        continue

  
    print("1 - Retirada na loja - Grátis")
    print("2 - Entrega em casa - R$20,00")

    try:
        opcao_entrega = int(input("Selecione a opção de entrega: "))
    except:
        print("Opção inválida")
        continue

    if opcao_entrega == 1:
        entrega_escolhida = "Retirada na loja"

    elif opcao_entrega == 2:
        entrega_escolhida = "Entrega em casa"
        valor = valor + 20

    else:
        print("Opção inválida")
        continue

    
    print("====== PAGAMENTO ======")
    print("1 - Pix --> 10% OFF")
    print("2 - Cartão de Crédito --> 5% Acréscimo")

    try:
        opcao_pagamento = int(input("Escolha a opção do pagamento: "))
    except:
        print("Opção inválida")
        continue

    if opcao_pagamento == 1:
        pagamento_escolhido = "Pix"
        valor = valor * 0.9

    elif opcao_pagamento == 2:
        pagamento_escolhido = "Cartão de Crédito"
        valor = valor * 1.05

    else:
        print("Opção inválida")
        continue

    break



if produto_escolhido != "":
    print("\n======================= RECIBO =======================")
    print("Produto:", produto_escolhido)
    print("Forma de entrega:", entrega_escolhida)
    print("Forma de pagamento:", pagamento_escolhido)
    print(f"Valor total do pedido: R$ {valor:.2f}")
else:
    print("Nenhuma compra realizada.")