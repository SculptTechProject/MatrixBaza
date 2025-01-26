import re
import math

mapa = "0123456789abcdefghijklmnopqrstuvwxyz"
def printBaza(x, b):
    xStr = ""
    while x > 0:
        xStr += mapa[x % b]
        x //= b
    print(xStr[::-1])

print("Wpisz originalną baze i oczekiwaną po spacji np. '15 8': ")
baza1, baza2 = (int(x) for x in input().split())

print("Wpisz liczbę do konwersji np. '8,A0(05)':")
liczbaStr = input().lower()


pattern = re.compile(r'([0-9a-z]+),([0-9a-z]+)\(([0-9a-z]+)\)')

match = pattern.match(liczbaStr)

if not match:
    print("Niepoprawny format liczby")
    exit()

liczba1 = match.group(1)
liczba2 = match.group(2)
liczba3 = match.group(3)

liczba1len = len(liczba1)
liczba2len = len(liczba2)
liczba3len = len(liczba3)

liczba1Dec = int(liczba1, base=baza1)
liczba2Dec = int(liczba2, base=baza1)
liczba3Dec = int(liczba3, base=baza1)

x1 = liczba1Dec * (baza1 ** liczba2len) + liczba2Dec
x2 = x1 * (baza1 ** liczba3len) + liczba3Dec

xLicznik = x2 - x1
xMianownik = (baza1 ** (liczba2len + liczba3len)) - (baza1 ** liczba2len)

print(f"Liczba w bazie {baza1}:")
printBaza(xLicznik, baza1)
print("----------------------")
printBaza(xMianownik, baza1)
print()

print(f"Liczba w bazie {baza2}:")
printBaza(xLicznik, baza2)
print("----------------------")
printBaza(xMianownik, baza2)
print()

NWD = math.gcd(xLicznik, xMianownik)
xLicznikSkrocony = xLicznik // NWD
xMianownikSkrocony = xMianownik // NWD

print(f"Liczba w bazie {baza2} po skróceniu:")
printBaza(xLicznikSkrocony, baza2)
print("----------------------")
printBaza(xMianownikSkrocony, baza2)


