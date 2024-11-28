# Programa para determinara quantidade de valores pares e impares

qtd_par = 0
qtd_impar = 0
numeros = [10,15,12,13,11,21,22,50,30,45]
num_sort = []
num_reverse = []
for i in range(len(numeros)):
    if numeros[i] % 2 == 0:
       qtd_par += 1

else:
    qtd_impar += 1 
    print(f"A quantidade de numeros pares é: {qtd_par}")
    print(f"A quantidade de numeros impares é: {qtd_impar}")
    print("Ordem de criação")
    print(numeros)
    print("Ordem de crescente")
    num_sort = numeros.sort()
    print(num_sort)
    print("Ordem Inversa")
    num_reverse =  numeros.reverse()
    print(num_reverse)
    


