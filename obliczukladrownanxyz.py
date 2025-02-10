import sympy as sp

# Definicja zmiennych
x, y, z = sp.symbols('x y z')

# Definicja układu równań
eq1 = -3*x + y - 2*z - (-4)
eq2 = 3*x - y + z - (-1)
eq3 = x - y - 3*z - (-19)

# Rozwiązanie układu równań
solution = sp.solve([eq1, eq2, eq3], (x, y, z))

# Wyświetlenie wyniku
print(f"x = {solution[x]}")
print(f"y = {solution[y]}")
print(f"z = {solution[z]}")