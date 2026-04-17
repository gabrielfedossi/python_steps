#  Crie um programa em Python que converta temperaturas. O usuário deve:

#Informar um valor numérico (temperatura)
#Escolher a conversão desejada:
#1 – Celsius para Fahrenheit
#2 – Fahrenheit para Celsius
#3 – Celsius para Kelvin
#4 – Kelvin para Celsius
escolhido = 0
while True:
    print("========= MENU =======")
    print("1 - Celsius para Fahrenheit")
    print("2 - Fahrenheit para Celsius")
    print("3 - Celsius para Kelvin")
    print("4 - Kelvin para Celsius")

    opcao = int(input("Selecione uma opção: "))

    if opcao == 1:
        celsius = float(input("Insira a temperatura em Celsius: "))
        Fahrenheit = (celsius * 9/5) + 32
        escolhido = Fahrenheit
        break
    elif opcao == 2:
        Fahrenheit = float("Insira a temperatura em Fahrenheit: ")
        celsius = (Fahrenheit - 32) * 5/9
        escolhido = celsius
        break
    elif opcao == 3:
        celsius = float(input("Insira a temperatura em Celsius: "))
        Kelvin = celsius + 273.15
        escolhido = Kelvin
        break
    elif opcao == 4:
        Kelvin = float(input("Insira a temperatura em Kelvin: "))
        celsius = Kelvin - 273.15
        escolhido = celsius
        break

print(escolhido)


