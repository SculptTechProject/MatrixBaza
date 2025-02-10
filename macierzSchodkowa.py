import numpy as np
import pandas as pd


# NA WSTEPIE MOWIE NIE WIEM CZY TO COS BEDZIE DAWAC XD
# LEPIEJ STRZELAC <3


# Macierz schodkowa rozszerzona (A | B)
A_ext = np.array([
    [1, 0, 0, -8, 9, 0, 0],
    [0, 1, 0, 2, 2, 0, 0],
    [0, 0, 1, -8, -16, 0, 10],
    [0, 0, 0, 0, 0, 1, -8],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0]
], dtype=float)

# Separacja macierzy współczynników i wektora wyników
A = A_ext[:, :-1]  # Wszystkie kolumny poza ostatnią
B = A_ext[:, -1]   # Ostatnia kolumna

# Liczba niewiadomych
num_vars = A.shape[1]

# Tworzymy listę zmiennych parametrycznych
T = np.zeros(num_vars)  # Domyślne wartości dla zmiennych
param_t = 1  # Możesz zmieniać t
param_u = 1  # Możesz zmieniać u

# Wyznaczanie wartości zmiennych zależnych
T[3] = param_t  # t jako parametr
T[4] = param_u  # u jako parametr
T[5] = -8       # v jest określone

# Obliczanie pozostałych wartości na podstawie macierzy schodkowej
T[0] = 8 * T[3] - 9 * T[4]  # x = 8t - 9u
T[1] = -2 * T[3] - 2 * T[4]  # y = -2t - 2u
T[2] = 8 * T[3] + 16 * T[4] + 10  # z = 8t + 16u + 10

# Tworzenie DataFrame do wyświetlenia wyników
df_result = pd.DataFrame([T], columns=["x", "y", "z", "t", "u", "v"])

# Wyświetlenie wyników w konsoli
print(df_result)
