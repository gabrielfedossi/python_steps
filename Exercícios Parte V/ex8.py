#  Desenvolva um programa que verifique se uma sequência de números digitados está em ordem crescente.
numeros = []
while True:

    print("========= MENU ========")
    print("1 - Inserir número")
    print("0 - Sair")

    opcao = int(input("Insira uma opção: "))

    if opcao == 1:
        num = int(input("Insira um número: "))
        numeros.append(num)
    elif opcao == 0:
        break
    else:
        print("Insira uma opção válida")

    ordenada = sorted(numeros)


if ordenada == numeros:
    print("A ordem está crescente")
else:
    print("A ordem não está crescente")
