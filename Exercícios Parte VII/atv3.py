lista = [0,1,2,3,4,5,6,7,8,9,10]

print(lista[1:10])
print(lista[8:10])
print(lista[::2])
print(lista[1::2])
inverso = lista.sort(reverse=True)
print(lista)
normal = lista.sort()
print(lista)
print(len(lista))
print(sum(lista))

print(sum(lista) / len(lista))

