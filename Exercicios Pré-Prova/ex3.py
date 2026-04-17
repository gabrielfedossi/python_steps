#Faça um programa em Python que leia uma senha (número inteiro).

#     O programa deve continuar solicitando a senha até que o usuário digite o valor correto (1234).

#Se a senha estiver correta, exiba: "Acesso Permitido"
#Caso contrário, exiba: "Acesso Negado" e peça a senha novamente
#   Obrigatório o uso de estrutura de repetição (while).

while True:
    print("======== MENU ========")
  
    senha = int(input("Insira sua senha (4 digitos): "))


    if senha == 1234:
        print("Acesso permitido")
        break
    else:
        print("Acesso Negado! Por favor digite novamente.")
