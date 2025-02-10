import sympy as sp


def find_coefficients(extremum_x):
    # Definiujemy zmienne
    a, b, c = sp.symbols('a b c')
    x = extremum_x  # Punkt, w którym funkcja ma ekstremum

    # Pierwsza pochodna funkcji f(x) = x^3 + ax^2 + bx + c
    f_prime = 3 * x ** 2 + 2 * a * x + b

    # Warunek ekstremum: f'(x) = 0 w x = extremum_x
    eq1 = sp.Eq(f_prime, 0)

    # Druga pochodna f''(x) = 6x + 2a powinna być dodatnia
    f_double_prime = 6 * x + 2 * a

    # Rozwiązujemy równanie dla a w sposób poprawny
    a_value = sp.Symbol('a')
    a_solution = sp.solve(f_double_prime - 1, a)  # Wybieramy minimalne a zapewniające dodatnią drugą pochodną
    a_value = float(a_solution[
                        0]) if a_solution else 0  # Pobieramy pierwsze rozwiązanie i konwertujemy na liczbę zmiennoprzecinkową

    # Rozwiązujemy równanie dla b
    eq1 = eq1.subs(a, a_value)
    b_value = float(sp.solve(eq1, b)[0])

    # Wartość c może być dowolna, ponieważ nie wpływa na ekstremum
    c_value = sp.Symbol('c')  # Pozostaje ogólne

    return a_value, b_value, c_value


# Użycie funkcji
a, b, c = find_coefficients(3)
print(f"Współczynniki: a = {a}, b = {b}, c = {c}")
