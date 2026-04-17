idade = int(input("Digite a idade: \n"))
peso = float(input("Digite o peso: \n"))
quanto_dormiu = float(input("Quantas horas dormiu? \n"))


if idade >= 16 and idade <= 69 and peso > 50 and quanto_dormiu >= 6:
    print("Você pode doar sangue.")
else:
    print(f"Você não pode doar sangue, seu peso é {peso} kg, sua idade é {idade} anos e você dormiu {quanto_dormiu} horas.", end=" ")
    print("Os requisitos para doar sangue são: idade entre 16 e 69 anos, pesar mais de 50kg, ter dormido pelo menos 6 horas.")