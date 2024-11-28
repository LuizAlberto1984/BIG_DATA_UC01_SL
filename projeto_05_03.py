#
nomes = []
idades = []
# Coletando os dados 
for i in range(5):
    nomes.append(input("Informe o nome: ")) # Comando append para guardar os nomes dentor do vetor
    idades.append(int(input("Informe a idade: ")))
    print("Listagem dos Usuários")
    # Listando os dados
    for i in range(len(nomes)):
        print(f"{nomes[i]} - {idades[i]}")
        