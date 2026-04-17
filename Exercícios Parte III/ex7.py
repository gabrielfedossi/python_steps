contador = 0
numeros = []

for i in range(1,6):
    num = int(input("Insira um número: "))
    numeros.append(num)
    contador = contador + 1
    if contador == 5:
        print("A soma dos números é", sum(numeros))
    else:
        continue
    
    
        