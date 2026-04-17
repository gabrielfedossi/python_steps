# . Crie um programa que simule um sistema de login com bloqueio progressivo após tentativas incorretas.

while True:
    print("====== MENU ====")
    print("1 - Logar")
    print("0 - SAIR")

    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        for a in range(1,4):
            login = (input("Insira o Login: "))
            senha = int(input("Insira sua senha: "))
            contador = 0
        
            if (login == "Gabriel") and (senha == 1234):
                print("Bem vindo!")
                break
            else:
                print("Senha errada!")
        else:
            print("Senha Bloqueada!")
            break
    elif opcao == 0:
        break
    else:
        print("Insira uma opção válida")