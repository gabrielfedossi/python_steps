
lista_fixa = [10, 20, 30, 40, 50]

print("-" * 10, "Consulta de Elementos na Lista", "-" * 10)
print(f"A lista possui {len(lista_fixa)} elementos (índices de 0 a 4).")

entrada_usuario = input("\nDigite a posição (índice) que deseja acessar: ")

try:
    posicao = int(entrada_usuario)
    print(posicao)
    
    valor_encontrado = lista_fixa[posicao]
    
    print(f"Sucesso! O valor na posição {posicao} é: {valor_encontrado}")

except ValueError:
    print("Erro: A entrada digitada não é um número inteiro válido")
    

except IndexError:
    print("Erro: A posição informada está fora da faixa da lista (índice inválido)")

finally:
    print("Consulta finalizada. Obrigado por utilizar o programa")