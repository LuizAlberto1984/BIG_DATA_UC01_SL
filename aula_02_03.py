import pandas as pd

serie1 = pd.Series([5, 12, 23, 36, 45, 56, 17, 28, 79, 10])
serie2 = pd.Series([10, 29, 38, 57, 46, 75, 84, 13, 22, 11])

# resultados
print("--- Soma das series ---")
print(serie1 + serie2)
print("\n--- subtração das series ---")
print(serie1 - serie2)
print("\n--- divisão das series ---")
print(serie1 / serie2)
print("\n--- multiplicação das series ---")
print(serie1 * serie2)

