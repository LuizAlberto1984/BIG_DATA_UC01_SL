#Programa com desvio e conectivo
nome = input("Informe o nome: ")
sexo = input("Informe o sexo (M e F): ")
idade = int(input("Informe a idade :"))
if (idade >= 18) and (sexo == "M" or sexo == "m"): #testar mais de uma variavel na mesma linha, and ou && é como se estivesse um if dentro do outro
    print("Você é maior de idade")
    certificado = int(input("Informe o certificado de reservista: "))
elif idade >= 18:
    print("Você é maior de idade")
else:
    print("Você é menor de idade")