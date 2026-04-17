somador = 0
contador = 0
while True:

    
    numero = float(input("Insira um número: "))
    if numero == 0:
        break
    
    somador = somador + numero
    contador = contador + 1
    
if contador == 0:
    print("Nenhum número foi inserido")
else:   
    media = somador / contador
    print(f"{media:.2f}")
