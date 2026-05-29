def opcao():
    print("=" * 30, "Programa", "=" * 30)
    print("1 - Começar")
    print("0 - Sair")
    op = int(input("Insira uma opção (1/0): "))
    return op


def opcao2():
    print("=" * 30, "Programa", "=" * 30)
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    op = int(input("Insira uma opção (1/2/3/4): "))
    return op


    


def soma(x,y):
    print(x + y)
    return
def sub(x,y):
    print(x - y)

    return
def mult(x,y):
    print(x * y)
    return
def div(x,y):
    print(x/y)
    return




while True:
    try:
        op = opcao()

        if op == 1:
            a = int(input("Insira o primeiro valor: "))
            b = int(input("Insira o segundo valor: "))
            op2 = opcao2()
            if op2 == 1:
                soma(a,b)
            elif op2 == 2:
                sub(a,b)
            elif op2 == 3:
                mult(a,b)
            elif op2 == 4:
                div(a,b)
            else:
                print("Valor inválido!")
        elif op == 0:
            break
        else:
            print("Insira um opcão válida")        
    except ValueError:
        print("\nINSIRA UM VALOR INTEIRO")
    except ZeroDivisionError:
        print("\nNúmero não divisivel")
        
        
            

            


        
        

    