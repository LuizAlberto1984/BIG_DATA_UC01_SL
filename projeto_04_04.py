#
for i in range(3):
    nome = input("Informe o nome do estudante: ")
    nota1 = float(input("Informe a primeira nota: "))
    nota2 = float(input("Informe a segunda nota: "))
    media = (nota1 + nota2) / 2
    if media >= 70:
        print(f"{nome}, você está em aprovado: ")
    elif media >= 30:
        print(f"{nome}, você está em recuperação: ")
    else:
        print(f"{nome}, você está reprovado. ")