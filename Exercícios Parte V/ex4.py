# Crie um programa que peça um número e verifique se ele é um palíndromo (ex: 121,
# 1331).

num = (input("Insira um número inteiro: "))


inverso = num[::-1]

if num == inverso:
    print("Esse número é palíndromo")
else:
    print("Esse número não é palíndromo")