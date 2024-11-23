#Programa Média com Desvio

nome = input("Informe o nome do estudante :")
n1 = float(input("Informe a primeira nota: "))
n2 = float(input("Informe a segunda nota: "))
media = (n1 + n2) / 2
if media >= 70:
    print(f"Sr(a) {nome}, a sua média foi {media}, Portanto você está aprovado, Parabéns!")
elif media >= 30: 
 print(f"Sr(a) {nome}, a sua média foi {media}, Portanto você está em recuperação") 
else:
    print(f"Sr(a) {nome}, se a média foi {media}, Você está reprovado!")
