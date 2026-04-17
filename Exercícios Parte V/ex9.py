#Faça um programa com menu que permita adicionar números e depois mostrar soma, média, maior e menor valor.
numeros = []
calculo_soma = 0
calculo_media = 0
while True:
    print("====== MENU ======")
    print("1 - Adicionar número")
    print("0 - SAIR")


    opcao = int(input("Selecione sua opção: "))

    if opcao == 1:
        num = int(input("Insira seu número: "))
        numeros.append(num)
        calculo_soma = calculo_soma + num
        calculo_media = calculo_media + 1
    elif opcao == 0:
        break
    else:
        print("Insira uma opção válida")

    total = sum(numeros)
    


print("==== RESULTADOS ====")
print(f"A soma é {total}")
print(f"A média é {calculo_soma / calculo_media}")
print(f"O maior é {max(numeros)}")
print(f"O menor é {min(numeros)}")

