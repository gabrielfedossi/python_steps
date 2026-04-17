login_certo = "Gabriel"
senha_certa = 1234
contador = 3

while contador > 0:
    login = input("Login: ")
    senha = int(input("Senha: "))

    if login == login_certo and senha == senha_certa:
        print("Bem-vindo!")
    else:
        print("Tente mais uma vez.", end=" ")
        contador = contador - 1
        print(f"{contador} tentativa(s) restantes")
else:
    print("Conta bloqueada!")

    


