
numeros = []
while True:
    try:
        num = int(input("Insira um número: "))
    
        if num == 0:
            print(sum(numeros))
            break
        else:
            numeros.append(num)
    except:
        print("Insira um valor inteiro")

