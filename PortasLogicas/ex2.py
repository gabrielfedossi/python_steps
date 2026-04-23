a = True
b = True
c = False
d = False


print("Tabela verdade - AND")
print("0   AND    0: ", c and d)
print("0   AND    1: ", c and a)
print("1   AND    0: ", a and d)
print("1   AND    1: ", a and b)


print("\n")


print("Tabela verdade - NAND")
print("0   AND    0: ", not(c and d))
print("0   AND    1: ", not(c and a))
print("1   AND    0: ", not(a and d))
print("1   AND    1: ", not(a and b))