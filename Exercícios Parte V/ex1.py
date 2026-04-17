# Crie um programa que leia um número inteiro e verifique se ele é um número perfeito
#(um número é perfeito quando a soma de seus divisores, exceto ele mesmo, é igual a ele).

num = int(input("Digite um número inteiro: "))

soma = 0
for i in range(1, num):
    if num % i == 0:
        soma = soma + i
if soma == num:
    print(f"{num} é um número perfeito.")
else:
    print(f"{num} não é um número perfeito.")
