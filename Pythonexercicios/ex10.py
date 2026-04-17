nome_produto = input("Digite o nome do produto: ")
preco_produto = float(input("Digite o preço do produto: "))
quantidade = int(input("Digite a quantidade do produto: "))
total = preco_produto * quantidade
print("O total a pagar pelo produto", nome_produto, "é:", total)