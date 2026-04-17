num = 1
total_pares = []
impar = []

while num <= 50:
    if num % 2 == 0:
        total_pares.append(num)
    else:
        impar.append(num)
    
    num = num + 1
print(len(total_pares), "total de números pares")