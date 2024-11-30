def calcular_salario():
    
    valor_hora = float(input("Digite o valor da hora trabalhada: "))
    horas_trabalhadas = float(input("Digite o número de horas trabalhadas no mês: 1  "))

    # calc bruto
    salario_bruto = valor_hora * horas_trabalhadas

   
    tributo_irrf = 0.11
    tributo_inss = 0.08
    tributo_sindicato = 0.05

    # Calc descontos
    desconto_irrf = salario_bruto * tributo_irrf
    desconto_inss = salario_bruto * tributo_inss
    desconto_sindicato = salario_bruto * tributo_sindicato

    # Calc líquido
    salario_liquido = salario_bruto - desconto_irrf - desconto_inss - desconto_sindicato

    # lista 
    resultados = [
        (f"Salário Bruto: R$ {salario_bruto:.2f}"),
        (f"Valor pago ao IRRF: R$ {desconto_irrf:.2f}"),
        (f"Valor pago ao INSS: R$ {desconto_inss:.2f}"),
        (f"Valor pago ao Sindicato: R$ {desconto_sindicato:.2f}"),
        (f"Salário Líquido: R$ {salario_liquido:.2f}")
    ]

    
    for resultado in resultados:
        print(resultado)

#valor final
calcular_salario()