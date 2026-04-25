numeros = []


for i in range(10):
    num = int(input("Insira um número: "))
    numeros.append(num)


verificar = int(input("Insira um número para verificar: "))

if verificar in numeros:
    print("O número está na lista")
else:
    print("O número não está na lista")


# achou = False
# for i in numeros:
#   if verificar == i:
#   achou = True

#if achou:
#    print("O número foi encontrado")
#else:
#    print("O número não foi encontrado")



