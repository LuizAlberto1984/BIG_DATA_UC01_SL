#Escreva um programa que, dados 2 números inteiros (n1 e n2), diga se eles são iguais ou diferentes, 
#Utilizando a estrutura do programa anterior, some os dois valores se forem diferentes e multiplique-os se forem iguais.

n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))

if n1 == n2:
    #resultado = n1 * n2
    print(f"Os números são iguais. O resultado da multiplicação é {n1 * n2}")
else:
    #soma = n1 + n2
    print(f"Os números são diferentes. O resultado da soma é { n1 + n2}")
