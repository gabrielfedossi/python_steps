# 2) Solicite uma frase e, em seguida, uma palavra.
# Informe quantas vezes essa palavra aparece na frase.


frase = input("Insira uma frase: ")
palavra = input("Insira uma palavra: ")



if palavra in frase:
    junior = frase.count(palavra)
    
    print("Essa palavra está na frase", junior)
else:
    print("Essa palavra nao está na frase")

