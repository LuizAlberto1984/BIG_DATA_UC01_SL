# programa para tratar divisão
while True:
    try: 
        n1 = int(input("Digite o primeiro número: "))
        n2 = int(input("Digite o segundo número: "))
        divisao = n1 / n2
    except ZeroDivisionError:
        print("verifique o segundo valor digitado, pois ele não pode ser zero")  
    else:      
        print(f"Oresultado da divisão é {divisao}")
        break

