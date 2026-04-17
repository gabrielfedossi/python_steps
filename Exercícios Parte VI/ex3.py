# Crie um programa que leia uma frase e exiba ela invertida.
# OBS: Não utilizar funções prontas como [::-1].


frase = input("Insira um frase: ")

inverso = ""

for letra in frase:
    inverso = letra + inverso

print("Invertida é:", inverso)

