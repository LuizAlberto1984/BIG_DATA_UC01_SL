#Programa para calcular a velocidade média e consumo médio por litro
cm = 12
d = int(input("informe a distância percorrida (km) :"))
t = float(input("informe o tempo de viagem (horas) :"))
vm = d / t
l = d / cm
print (f"A velocidade média do veiculo foi {vm} km/h. ")
print (f"A quantidade de combustivél foi {l} Litros. ")