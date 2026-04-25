numeros = []
soma = 0


for i in range(10):
    num = int(input("Insira um número: "))
    numeros.append(num)


for num in numeros:
    print("Valor: ", num)
    soma = soma + num

media = soma/len(numeros)

maior = menor = numeros[0]
for i in numeros:
    if i > maior:
        maior = i
    if i < menor:
        menor = i
    
    

print(media)
print(max(numeros))
print(min(numeros))
print(maior)
print(menor)
