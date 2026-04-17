# Crie um programa que simule um caixa eletrônico, mostrando a quantidade mínima de notas para um saque (100, 50, 20, 10, 5, 2)

saldo = 1500
valor_saque = 0

while True:

    print("======= BANCO ========")
    print("1 - Sacar")
    print("0 - Sair")

    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        
        print("Opções de Saque:")
        print("1 - R$100")
        print("2 - R$50")
        print("3 - R$20")
        print("4 - R$10")
        print("5 - R$5")
        print("6 - R$2")
        print("0 - SAIR")
        opcao_saque = int(input("Insira a opção de saque: "))
        try:
            match opcao_saque:
                case 1:
                    novo_saldo = saldo - 100
                    valor_saque = 100
                case 2:
                    novo_saldo = saldo - 50
                    valor_saque = 50
                case 3:
                    novo_saldo = saldo - 20
                    valor_saque = 20
                case 4:
                    novo_saldo = saldo - 10
                    valor_saque = 10
                case 5:
                    novo_saldo = saldo - 5
                    valor_saque = 5
                case 6:
                    novo_saldo = saldo - 2
                    valor_saque = 2
                case 0:
                    break
                case _:
                    print("Selecione uma opção válida")
        except:
            print("Insira a opção númerica")
        
    elif opcao == 0:
        break
    else:
        print("Selecione uma opção válida")

        

try:
    print(f"Seu saldo atual R${novo_saldo}")
    print(f"Valor do saque R${valor_saque}")
except:
    print("Volte Sempre!")