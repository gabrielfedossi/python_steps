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
     
       