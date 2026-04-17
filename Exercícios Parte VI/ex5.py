# Solicite uma frase e exiba apenas as palavras que começam com vogal.

frase = input("Insira um frase: ")

palavras = frase.split()
vogais = "aeiouAEIOU"


for palavra in palavras:
    if palavra[0] in vogais:
        print(palavra)
    