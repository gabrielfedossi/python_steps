num1 = float(input("Insira o primeiro número: "))
num2 = float(input("Insira o segundo número: "))

if num1 > num2:
    print(f"O número {num1} é maior que {num2}.")
elif num2 > num1:
    print("O número", num2, "é maior que", num1)
else:
    print("Os dois números são iguais.")
