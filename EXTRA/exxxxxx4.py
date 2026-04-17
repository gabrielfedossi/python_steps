print("BANCO CÓDIGO - SISTEMA BANCÁRIO")
print("BEM VINDO AO TERMINAL DE ATENDIMENTO")
print("Segurança, Rapidez, Confiança")





agencia = str(input("Digite sua agência: "))
conta = int(input("Digite sua conta: "))
senha = int(input("Digite sua senha: "))

if agencia == "Código" and conta == 2904 and senha == 1234:
        print("Acesso Permitido!")
        print("---- MENU DO BANCO ---")
        print("1 - Saldo")
        print("2 - Extrato")
        print("3 - Pagamento")
        print("4 - Saque")
        print("5 - Depósito")
        print("0 - Sair")
        while True:
            opcao = int(input("Escolha uma opção: "))
            match opcao:
                case 1:
                    print("Seu saldo é R$546,80")
                    break
                case 2:
                    print("Sem extrato")
                    break
                case 3:
                    print("Entrando em pagamento....")
                    break
                case 4:
                    print("Qual o valor do saque?")
                    break
                case 5:
                    print("Entrando em depósito....")
                    break
                case 0:
                    print("Saindo....")
                    break
                case _:
                    print("Insira um valor válido")
                

else:
    print("Erro de senha!")