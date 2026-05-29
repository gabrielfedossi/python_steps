contatos = {
    "ana": "ana@example.com",
    "joao": "joao@example.com",
    "maria": "maria@example.com"
}

print("--- Busca no Dicionário de Contatos ---")

nome_busca = input("Digite o nome do contato que deseja buscar: ").strip().lower()

try:
   
    if nome_busca == "":
        raise ValueError("Nome vazio")
    

    email_encontrado = contatos[nome_busca]

except ValueError as erro_vazio:

    print(f"Erro: {erro_vazio}. Você deve digitar um nome para realizar a busca.")

except KeyError:

    print(f"Erro: O contato '{nome_busca}' não foi encontrado no sistema.")

else:

    print(f"Sucesso! O e-mail de {nome_busca.capitalize()} é: {email_encontrado}")

finally:

    print("Busca encerrada. Obrigado por utilizar o sistema de contatos!")
