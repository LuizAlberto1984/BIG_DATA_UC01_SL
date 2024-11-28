# Gabarito da prova INCLUINDO AS QUESTÕES
gabarito = ['A', 'B', 'B', 'D', 'E']

# Inicializa o contador de acertos
acertos = 0


# Solicita as respostas do usuário
respostas_usuario = []
for i in range(5):
    resposta = input(f"Informe a resposta da questão {i+1} (A, B, C, D ou E): ").upper()
    respostas_usuario.append(resposta)

# Compara as respostas do usuário com o gabarito
for i in range(5):
    if respostas_usuario[i] == gabarito[i]:
        acertos += 1

# Imprime o resultado
print(f"Você acertou {acertos} questões.")