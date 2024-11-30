# Programa para trocar erro de entrada de dados
nome = input("Informe o nome: ")
while True:
    sexo = input("Informe o sexo (M e F): ")
    if sexo == "M" or sexo == "F":
        break
    else:
        print("informe apenas M ou F para o sexo")
    while True:
        try:
            idade = int(input("Informe a idade :"))
        except ValueError:
            print("Verifique a idade digitada")
        else:    
            print(f"Seja bem vindo {nome}")
            break
    