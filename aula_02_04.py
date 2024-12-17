# Exibir dados sobre roubo e furto 
import pandas as pd
roubo = pd.Series([100,90,80,120,110,90,70])
furto = pd.Series([80,60,70,60,100,50,30])
rec = pd.Series([70,50,90,80,100,70,50])
print("--- Soma diaria de roubos e furto de veiculos ---")
print(roubo + furto)
print("\n--- percentual diario de recuperação de veiculos ---")
print((rec / roubo)* 100)
print("\n--- Total de roubo de veiculos ---")
print("\n--- Total de furtos de veiculos ---")
print("\n--- Total de recuperação de veiculos ---")
print("\n--- Percentual Total de recuperação de veiculos ---")

