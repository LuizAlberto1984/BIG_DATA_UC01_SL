# Programa Calcular Idade
import datetime # importa a biblioteca datetime
data_atual = datetime.date.today() # armazena na variavél a data completa
nasc = int(input('informe o ano de nascimento: '))
ano_atual = data_atual.year # Armazena na variavel o ano atual
idade = ano_atual - nasc
print(f'A sua idade é {idade} anos.')
