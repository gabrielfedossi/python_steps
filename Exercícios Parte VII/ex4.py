nums = [1, 2, 3, 4, 5, 6, 7, 8]

print(nums[2])
print(nums[9-8])
print(nums[-2])
print(nums[-1])

print("\n")

frutas = ["maca", "laranja", "banana", "cereja"]
print("maca" in frutas, end=" ")
print("pera" in frutas)

print("\n")

print([1,2] + [3,4])
print(frutas + [6,7,8,9])

print(["teste"] * 4)
print([1,2,["ola", "adeus"]] * 2)

print("\n")

a = [1,2,3,4,5,6,7,8,9]

print(a)
print(max(a))
print(min(a))
print(sum(a))

print("\n")

frutas[0] = "pera"
frutas[-1] = "melancia"
frutas[1:3] = ["melao", "abacaxi"]
frutas[3:3] = ["limao"]
print(frutas)

print("\n")

del frutas[1]
print(frutas)
# ['pera', 'abacaxi', 'limao', 'melancia']
del frutas[1:3]
print(frutas)

print("\n")

numeros = [88,81,83,82]
print("Posição do Index do número 81 é:", numeros.index(81))
numeros.sort()
print(numeros)
numeros.sort(reverse=True)
print(numeros)


print("\n")

numeros_2 = [88, 81, 82, 83, 83, 83, 83, 95]

numeros_2.insert(1, 100) #POSIÇÃO, VALOR PARA INSERIR
print(numeros_2)
print(numeros_2.count(83)) #conta a quantidade de 83 que tem na lista

numeros_2.pop() # remove o ultimo valor da lista
print(numeros_2)
numeros_2.pop(1) # funciona igual o "del"
print(numeros_2)


print("\n")

numeros_3 = [1,2,3]
numeros_3.extend([4,5])
print(numeros_3)


# lista[0:4:2] inicio, fim, passo
