num = int(input("Digite um número inteiro de 1 a 7: "))


match num:
    case 1:
        print("Domingo")
    case 2:
        print("Segunda-feira")
    case 3:
        print("Terça-feira")
    case 4:
        print("Quarta-feira")
    case 5:
        print("Quinta-feira")
    case 6:
        print("Sexta-feira")
    case 7:
        print("Sábado")
    case _:
        print("Número inválido. Por favor, digite um número entre 1 e 7.")

# ou
# if num == 1:
#     print("Domingo")
# elif num == 2:
#     print("Segunda-feira")
# elif num == 3:
#     print("Terça-feira")
# elif num == 4:
#     print("Quarta-feira")
# elif num == 5:
#     print("Quinta-feira")
# elif num == 6:
#     print("Sexta-feira")
# elif num == 7:
#     print("Sábado")
# else:
#     print("Número inválido. Por favor, digite um número entre 1 e 7.")