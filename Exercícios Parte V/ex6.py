#  Faça um programa que leia vários números (até o usuário digitar &#39;sair&#39;) e mostre média, maior e menor valor e quantidade de números pares.
contador_soma = 0
contador_media = 0
numeros = []
numeros_pares = []
while True:
  
    
   print("======= MENU ========")
   print("1 - Inserir número")
   print("0 - Parar")

   escolha = int(input("Insira sua escolha: "))

   if escolha == 1:
      num = int(input("Insira o número: "))
      contador_soma = contador_soma + num
      contador_media = contador_media + 1
      numeros.append(num)
   elif escolha == 0:
      break
   else:
      print("Insira uma opção válida")

for i in numeros:
   if i % 2 == 0:
      numeros_pares.append(i)
   else:
      continue


print("======= RESULTADOS ======")
print(f"A média dos números é {contador_soma / contador_media}")
print(f"O maior número é {max(numeros)}")
print(f"O menor número é {min(numeros)}")
print(f"A quantidade de números pares é {len(numeros_pares)}")


   



        
        


