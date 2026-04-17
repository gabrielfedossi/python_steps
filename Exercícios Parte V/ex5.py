#  Desenvolva um programa que gere um número aleatório de 1 a 100 e simule um jogo de
# adivinhação, informando se o palpite é maior ou menor e exibindo o número de tentativas.


import random

num_real = random.randint(1, 100)
tentativas = 0

print("====== JOGO DA ADIVINHAÇÃO ======")
print("Escolha um número de 1 a 100")

while True:
    num = int(input("Insira o número escolhido: "))
    tentativas = tentativas + 1

    if num == num_real:
        print("Parabéns! Você acertou o número!")
        print(f"Você conseguiu em {tentativas} tentativas")
        break
    elif num < num_real:
        print("O número é maior")
    else:
        print("O número é menor")
