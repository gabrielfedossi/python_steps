# Você foi contratado para desenvolver um sistema simples de vendas para uma loja online.
# 📋 O SISTEMA DEVE PERMITIR:
# • Escolher um produto
# • Escolher a forma de entrega
# • Escolher a forma de pagamento
# • Ver o valor final da compra


entrega_escolhida = []
pagamento_escolhido = []
produto_escolhido = []
valor = 0
while True:
    print("====== LOJA ELETRONICA ======")
    print("1 - Fone Bluetooth - R$ 120.00")
    print("2 - Teclado Mecânico - R$ 250.00")
    print("3 - Mouse Gamer - R$ 80.00")
    print("4 - Webcam HD - R$ 150.00")
    print("0 - Sair")


    opcao = int(input("Selecione um produto: "))

    if opcao == 1:
        produto_escolhido.append("Fone Bluetooth")
        valor = valor + 120.00
        print("1 - Retirada na loja - Grátis")
        print("2 - Entrega em casa - R$20,00")
        print("0 - Cancelar pedido")

        opcao_entrega = int(input("Selecione a opção de entrega: "))

        if opcao_entrega == 1:
            entrega_escolhida.append("Retirada na loja")
            valor = valor + 0
            print("====== PAGAMENTO ======")
            print("1 - Pix --> 10% OFF")
            print("2 - Cartão de Crédito --> 5% Acréscimo")

            opcao_pagamento = int(input("Escolha a opção do pagamento: "))

            if opcao_pagamento == 1:
                pagamento_escolhido.append("Pix")
                desconto = valor * 0.1
                valor = valor - desconto
                break

            elif opcao_pagamento == 2:
                pagamento_escolhido.append("Cartão de Crédito")
                acrescimo = valor * 0.05
                valor = valor + acrescimo
                break
            else:
                print("Selecione uma opção válida")

        elif opcao_entrega == 2:
            entrega_escolhida.append("Entrega em casa")
            valor = valor + 20
            print("====== PAGAMENTO ======")
            print("1 - Pix --> 10% OFF")
            print("2 - Cartão de Crédito --> 5% Acréscimo")

            opcao_pagamento = int(input("Escolha a opção do pagamento: "))
            if opcao_pagamento == 1:
                pagamento_escolhido.append("Pix")
                desconto = valor * 0.1
                valor = valor - desconto
                break

            elif opcao_pagamento == 2:
                pagamento_escolhido.append("Cartão de Crédito")
                acrescimo = valor * 0.05
                valor = valor + acrescimo
                break
            else:
                print("Selecione uma opção válida")
        
    elif opcao == 2:
        produto_escolhido.append("Teclado Mecânico")
        valor = valor + 250
        print("1 - Retirada na loja - Grátis")
        print("2 - Entrega em casa - R$20,00")
        print("0 - Cancelar pedido")

        opcao_entrega = int(input("Selecione a opção de entrega: "))

        if opcao_entrega == 1:
            entrega_escolhida.append("Retirada na loja")
            valor = valor + 0
            print("====== PAGAMENTO ======")
            print("1 - Pix --> 10% OFF")
            print("2 - Cartão de Crédito --> 5% Acréscimo")

            opcao_pagamento = int(input("Escolha a opção do pagamento: "))

            if opcao_pagamento == 1:
                pagamento_escolhido.append("Pix")
                desconto = valor * 0.1
                valor = valor - desconto
                break

            elif opcao_pagamento == 2:
                pagamento_escolhido.append("Cartão de Crédito")
                acrescimo = valor * 0.05
                valor = valor + acrescimo
                break
            else:
                print("Selecione uma opção válida")

        elif opcao_entrega == 2:
            entrega_escolhida.append("Entrega em casa")
            valor = valor + 20
            print("====== PAGAMENTO ======")
            print("1 - Pix --> 10% OFF")
            print("2 - Cartão de Crédito --> 5% Acréscimo")

            opcao_pagamento = int(input("Escolha a opção do pagamento: "))
            if opcao_pagamento == 1:
                pagamento_escolhido.append("Pix")
                desconto = valor * 0.1
                valor = valor - desconto
                break

            elif opcao_pagamento == 2:
                pagamento_escolhido.append("Cartão de Crédito")
                acrescimo = valor * 0.05
                valor = valor + acrescimo
                break
            else:
                print("Selecione uma opção válida")
        
    elif opcao == 3:
        produto_escolhido.append("Mouse Gamer")
        valor = valor + 80.00
        print("1 - Retirada na loja - Grátis")
        print("2 - Entrega em casa - R$20,00")
        print("0 - Cancelar pedido")

        opcao_entrega = int(input("Selecione a opção de entrega: "))

        if opcao_entrega == 1:
            entrega_escolhida.append("Retirada na loja")
            valor = valor + 0
            print("====== PAGAMENTO ======")
            print("1 - Pix --> 10% OFF")
            print("2 - Cartão de Crédito --> 5% Acréscimo")

            opcao_pagamento = int(input("Escolha a opção do pagamento: "))

            if opcao_pagamento == 1:
                pagamento_escolhido.append("Pix")
                desconto = valor * 0.1
                valor = valor - desconto
                break

            elif opcao_pagamento == 2:
                pagamento_escolhido.append("Cartão de Crédito")
                acrescimo = valor * 0.05
                valor = valor + acrescimo
                break
            else:
                print("Selecione uma opção válida")

        elif opcao_entrega == 2:
            entrega_escolhida.append("Entrega em casa")
            valor = valor + 20
            print("====== PAGAMENTO ======")
            print("1 - Pix --> 10% OFF")
            print("2 - Cartão de Crédito --> 5% Acréscimo")

            opcao_pagamento = int(input("Escolha a opção do pagamento: "))
            if opcao_pagamento == 1:
                pagamento_escolhido.append("Pix")
                desconto = valor * 0.1
                valor = valor - desconto
                break

            elif opcao_pagamento == 2:
                pagamento_escolhido.append("Cartão de Crédito")
                acrescimo = valor * 0.05
                valor = valor + acrescimo
                break
            else:
                print("Selecione uma opção válida")
        
    elif opcao == 4:
        produto_escolhido.append("Webcam HD")
        valor = valor + 150.00
        print("1 - Retirada na loja - Grátis")
        print("2 - Entrega em casa - R$20,00")
        print("0 - Cancelar pedido")

        opcao_entrega = int(input("Selecione a opção de entrega: "))

        if opcao_entrega == 1:
            entrega_escolhida.append("Retirada na loja")
            valor = valor + 0
            print("====== PAGAMENTO ======")
            print("1 - Pix --> 10% OFF")
            print("2 - Cartão de Crédito --> 5% Acréscimo")

            opcao_pagamento = int(input("Escolha a opção do pagamento: "))

            if opcao_pagamento == 1:
                pagamento_escolhido.append("Pix")
                desconto = valor * 0.1
                valor = valor - desconto
                break

            elif opcao_pagamento == 2:
                pagamento_escolhido.append("Cartão de Crédito")
                acrescimo = valor * 0.05
                valor = valor + acrescimo
                break
            else:
                print("Selecione uma opção válida")

        elif opcao_entrega == 2:
            entrega_escolhida.append("Entrega em casa")
            valor = valor + 20
            print("====== PAGAMENTO ======")
            print("1 - Pix --> 10% OFF")
            print("2 - Cartão de Crédito --> 5% Acréscimo")

            opcao_pagamento = int(input("Escolha a opção do pagamento: "))
            if opcao_pagamento == 1:
                pagamento_escolhido.append("Pix")
                desconto = valor * 0.1
                valor = valor - desconto
                break

            elif opcao_pagamento == 2:
                pagamento_escolhido.append("Cartão de Crédito")
                acrescimo = valor * 0.05
                valor = valor + acrescimo
                break
            else:
                print("Selecione uma opção válida")
        
    elif opcao == 0:
        break
    else:
        print("Insira uma opção válida")


    
print("Produto:", produto_escolhido[0])
print("Forma de entrega:", entrega_escolhida[0])
print("Forma de pagamento:", pagamento_escolhido[0])
print("Valor total do pedido R$", valor)
print("======================= RECIBO =======================")

    






