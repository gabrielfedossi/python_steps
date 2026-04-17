# Faça um programa que simule uma urna eletrônica simples: 3 candidatos, voto nulo e
#branco. Ao final, mostre total de votos por candidato, percentual de votos nulos e brancos e
#o candidato vencedor.

candidato1 = 0
candidato2 = 0 
candidato3 = 0
nulo = 0
branco = 0

while True:
    print("=========== MENU ===========")
    print("1 - Candidato 1")
    print("2 - Candidato 2")
    print("3 - Candidato 3")
    print("4 - Voto Nulo")
    print("5 - Voto Branco")
    print("0 - Encerrar")

    try:

        voto = int(input("Selecione sua opção: "))

        if voto == 1:
            candidato1 = candidato1 + 1
        elif voto == 2:
            candidato2 = candidato2 + 1
        elif voto == 3:
            candidato3 = candidato3 + 1
        elif voto == 4:
            nulo = nulo + 1
        elif voto == 5:
            branco = branco + 1
        elif voto == 0:
            break
        else:
            print("Voto Inválido")
    except:
        print("Insira uma das opções")
    
total = candidato1 + candidato2 + candidato3

if total > 0:
    porcentagem_nulo = (nulo / total) * 100
    porcentagem_branco = (branco / total) * 100
else:
    porcentagem_branco = 0
    porcentagem_nulo = 0



if candidato1 > candidato2 and candidato1 > candidato3:
    vencedor = "Candidato 1"
elif candidato2 > candidato1 and candidato2 > candidato3:
    vencedor = "Candidato 2"
elif candidato3 > candidato1 and candidato3 > candidato2:
    vencedor = "Candidato 3"
else:
    vencedor = "Empate"

print("========== RESULTADOS =========")
print("Candidato 1: ", candidato1)
print("Candidato 2: ", candidato2)
print("Candidato 3: ", candidato3)
print("Nulo: ", nulo)
print("Branco", branco)
print(f"Porcentagem de nulos: {porcentagem_nulo:.2f}")
print(f"Porcentagem de votos Brancos: {porcentagem_branco:.2f}")
print("Vencedor: ", vencedor)