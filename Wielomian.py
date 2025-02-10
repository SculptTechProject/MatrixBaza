import numpy as np


def create_equations(conditions):
    """
    Funkcja generuje macierz współczynników i wektor prawych stron
    na podstawie podanych warunków.
    """
    A = []
    b = []

    for condition in conditions:
        x, derivative_order, value = condition
        row = []

        # Generowanie współczynników dla wielomianu lub jego pochodnej
        for power in range(5, -1, -1):   # ZMIEN 5 JAK DANY WIELOMIAN JEST INNY NIZ STOPNIA MNIEJSZEGO BADZ ROWNEGO 5
            if derivative_order == 0:  # wartość wielomianu
                coeff = x ** power
            elif derivative_order == 1:  # pierwsza pochodna
                coeff = power * x ** (power - 1) if power >= 1 else 0
            elif derivative_order == 2:  # druga pochodna
                coeff = power * (power - 1) * x ** (power - 2) if power >= 2 else 0
            elif derivative_order == 3:  # trzecia pochodna
                coeff = power * (power - 1) * (power - 2) * x ** (power - 3) if power >= 3 else 0
            else:
                raise ValueError("Nieobsługiwany rząd pochodnej.")
            row.append(coeff)

        A.append(row)
        b.append(value)

    return np.array(A), np.array(b)


# Warunki zadania
conditions = [
    (-1, 0, 6),  # w(-1) = 6
    (3, 0, -670),  # w(3) = -670
    (-1, 1, -9),  # w'(-1) = -9
    (3, 1, -1209),  # w'(3) = -1209
    (-1, 2, 40),  # w''(-1) = 40
    (3, 3, -1674)  # w'''(3) = -1674
]

# Generowanie macierzy i wektora prawych stron
A, b = create_equations(conditions)

# Rozwiązanie układu równań
coefficients = np.linalg.solve(A, b)

# Zaokrąglenie współczynników do 6 miejsc po przecinku
coefficients_rounded = np.round(coefficients, 6)

# Wyświetlenie współczynników wielomianu
print("Współczynniki wielomianu w(x):")
for i, coeff in enumerate(coefficients_rounded):
    print(f"a{5 - i} = {coeff}")


# Funkcja obliczająca wartość wielomianu w(x)
def w(x, coeffs):
    return sum(coeff * x ** power for power, coeff in enumerate(coeffs[::-1]))

# Przykład użycia funkcji (opcjonalnie)
# x_value = 2
# print(f"w({x_value}) = {w(x_value, coefficients_rounded)}")