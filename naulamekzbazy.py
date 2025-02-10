import re
import math


def parse_number(number_str, original_base):
    number_str = number_str.upper()
    pattern = r'^([0-9A-F]+),([0-9A-F]+)\(([^)]+)\)$'
    match = re.fullmatch(pattern, number_str)
    if not match:
        raise ValueError("Invalid number format")

    a_part, b_part, c_part = match.groups()

    a = int(a_part, original_base) if a_part else 0
    b = int(b_part, original_base) if b_part else 0
    c = int(c_part, original_base) if c_part else 0

    k = len(b_part)
    m = len(c_part)

    return a, b, c, k, m


def int_to_base(n, base):
    if n == 0:
        return '0'
    digits = []
    while n > 0:
        remainder = n % base
        if remainder < 10:
            digits.append(str(remainder))
        else:
            digits.append(chr(ord('A') + remainder - 10))
        n = n // base
    return ''.join(reversed(digits))


def convert_fraction(number_str, original_base, target_base):
    a, b, c, k, m = parse_number(number_str, original_base)

    # Obliczanie mianownika
    denom_part1 = (original_base ** m) - 1
    denom = denom_part1 * (original_base ** k)

    # Obliczanie licznika
    numerator = a * denom + b * denom_part1 + c

    # Skracanie ułamka
    gcd = math.gcd(numerator, denom)
    numerator_red = numerator // gcd
    denom_red = denom // gcd

    # Konwersja na docelową bazę
    numerator_str = int_to_base(numerator_red, target_base)
    denom_str = int_to_base(denom_red, target_base)

    return f"{numerator_str}/{denom_str}"


if __name__ == "__main__":
    number_input = input("Podaj liczbę (np. 4,2(401)): ")
    original_base = int(input("Podaj bazę wejściową (2-16): "))
    target_base = int(input("Podaj bazę wyjściową (2-16): "))

    try:
        result = convert_fraction(number_input, original_base, target_base)
        print(f"Ułamek w bazie {target_base}: {result}")
    except ValueError as e:
        print(f"Błąd: {e}")
