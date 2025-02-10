import sympy as sp
from fractions import Fraction


def convert_periodic_to_fraction(number_str, base):
    integer_part, fractional_part = number_str.split(',')
    non_periodic, periodic = fractional_part.split('(')
    periodic = periodic.rstrip(')')

    # Konwersja części całkowitej
    integer_value = int(integer_part, base)

    # Długości części nieokresowej i okresowej
    len_non_periodic = len(non_periodic)
    len_periodic = len(periodic)

    # Liczby całkowite odpowiadające częściom ułamkowym
    full_decimal = int(non_periodic + periodic, base)
    non_periodic_value = int(non_periodic, base) if non_periodic else 0

    # Tworzenie ułamka dla części okresowej
    numerator = full_decimal - non_periodic_value
    denominator = (base ** len_periodic - 1) * base ** len_non_periodic

    # Konwersja na ułamek zwykły
    fraction = Fraction(numerator, denominator)

    # Dodanie części całkowitej
    final_fraction = Fraction(integer_value * fraction.denominator + fraction.numerator, fraction.denominator)

    return final_fraction


# Pobieranie danych od użytkownika
base = int(input("Podaj bazę liczbową: "))
number_str = input("Podaj liczbę okresową w danej bazie (np. 4,2(401) dla bazy 11): ")

# Konwersja liczby
fraction = convert_periodic_to_fraction(number_str, base)
print(f"Liczba {number_str} w bazie {base} jako ułamek: {fraction.numerator}/{fraction.denominator}")