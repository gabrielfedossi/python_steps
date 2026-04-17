#  Leia uma frase e exiba:
#a) Quantidade de letras (desconsiderando espaços)
#b) Quantidade de espaços
#C) Quantidade de números presentes

texto = input("Insira uma frase: ")

letras = 0
espaços = 0
numeros = 0


for words in texto:
    if words.isalpha():
        letras =  letras + 1
    elif words == " ":
        espaços = espaços + 1
    elif words.isdigit:
        numeros = numeros + 1


print("Quantidade de letras: ", letras)
print("Quantidade de espaços: ", espaços)
print("Quantidade de números presentes: ", numeros)
