senha_correta = 1234
contador = 4

while contador > 0:
    try:
        senha = int(input("Digite sua senha de de 4 caracteres: "))

        if senha == senha_correta:
            print("Seja bem-vindo!")
            break
        else:
            contador = contador - 1
            print("Tente mais uma vez")
            print(f"{contador} chances restantes")
    except:
        print("Caracteres em números!")
else:
    print("Conta bloqueada")