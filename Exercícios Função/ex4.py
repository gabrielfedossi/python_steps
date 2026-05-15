def paraBinario(x):
    
    binario = ""
    while x > 0:
        resto = x % 2
        binario = str(resto) + binario
        x = x // 2
    print(f"O número em binário é: {binario}")
    return


num = int(input("Digite um número inteiro: "))

paraBinario(num)