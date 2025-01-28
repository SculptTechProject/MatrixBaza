import math

print("Wpisz współrzędne punktu w formacie 'liczbaX;liczbaY':")
punktStr = input()
x, y = (float(x) for x in punktStr.split(";"))

def wypisz():
    print(f"({x:.6f};{y:.6f})")

def menu():
    print("\nWybierz przekształcenie:")
    print("[X] Odbicie względem osi X")
    print("[Y] Odbicie względem osi Y")
    print("[Z] Odbicie względem początku układu")
    print("[O] Obrót o kąt")
    print("[S] Skalowanie")
    print("[P] Przesunięcie")
    print("[Q] Wyjście")

    
menu()
while True:
    print("Opcja: ", end="")
    wybor = input().upper()

    match wybor:
        case "X":
            y = -y
            wypisz()

        case "Y":
            x = -x
            wypisz()
        
        case "Z":
            x = -x
            y = -y
            wypisz()
        
        case "O":
            print("Wpisz kąt w stopniach: ", end="")
            kat = int(input())
            katRad = math.radians(kat)
            x2 = x * math.cos(katRad) - y * math.sin(katRad)
            y2 = x * math.sin(katRad) + y * math.cos(katRad)
            x = x2
            y = y2
            wypisz()
        
        case "S":
            print("Wpisz współczynniki skalowania w formacie 'liczbaX;liczbaY': ", end="")
            wspX, wspY = [float(x) for x in input().split(";")]
            x *= wspX
            y *= wspY
            wypisz()

        case "P":
            print("Wpisz współczynniki przesunięcia w formacie 'liczbaX;liczbaY': ", end="")
            wspX, wspY = [float(x) for x in input().split(";")]
            x += wspX
            y += wspY
            wypisz()

        case "Q":
            break

        case _:
            print("Niepoprawny wybór")
            menu()
    