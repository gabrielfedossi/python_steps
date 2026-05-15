def EPrimo(n):
    
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


N = int(input("Digite a quantidade de números primos desejada (N): "))

lista_primos = []
numero_atual = 2


while len(lista_primos) < N:
    if EPrimo(numero_atual):
        lista_primos.append(numero_atual)
    numero_atual += 1


print(f"Os primeiros {N} números primos são:")
print(lista_primos)