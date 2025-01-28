def parse_binary_operation():
    """Pobiera od użytkownika dane binarne i je analizuje."""
    print("Podaj działanie w formacie: liczba + liczba = wynik")
    operation = input("Działanie: ").strip()

    try:
        left, result = operation.split('=')
        num1, num2 = left.split('+')

        # Usuwamy spacje i sprawdzamy poprawność danych wejściowych
        num1 = num1.strip()
        num2 = num2.strip()
        result = result.strip()

        if not all(c in '01' for c in num1 + num2 + result):
            raise ValueError("Wszystkie liczby muszą być w systemie binarnym.")

        return num1, num2, result
    except ValueError as e:
        print(f"Błąd: {e}")
        return None
    except Exception:
        print("Nieprawidłowy format. Spróbuj ponownie.")
        return None

def to_decimal(binary, code_type):
    """Konwertuje liczbę binarną na dziesiętną w danym kodzie."""
    if code_type == "ZM":
        return int(binary[1:], 2) * (-1 if binary[0] == '1' else 1)
    elif code_type == "U1":
        if binary[0] == '1':
            inverted = ''.join('1' if b == '0' else '0' for b in binary)
            return -int(inverted, 2)
        else:
            return int(binary, 2)
    elif code_type == "U2":
        if binary[0] == '1':
            return -((1 << len(binary)) - int(binary, 2))
        else:
            return int(binary, 2)
    else:
        raise ValueError("Nieznany typ kodu.")

def check_operation(num1, num2, result):
    """Sprawdza, w jakim kodzie działa operacja."""
    for code_type in ["ZM", "U1", "U2"]:
        try:
            dec1 = to_decimal(num1, code_type)
            dec2 = to_decimal(num2, code_type)
            dec_result = to_decimal(result, code_type)

            if dec1 + dec2 == dec_result:
                return code_type
        except ValueError:
            continue

    return None

def main():
    print("Program do identyfikacji systemu kodowania binarnego.")
    while True:
        data = parse_binary_operation()
        if data:
            num1, num2, result = data
            code_type = check_operation(num1, num2, result)

            if code_type:
                print(f"Działanie jest poprawne w kodzie: {code_type}")
            else:
                print("Działanie nie jest poprawne w żadnym z kodów: ZM, U1, U2.")

        again = input("Czy chcesz spróbować ponownie? (tak/nie): ").strip().lower()
        if again != 'tak':
            break

if __name__ == "__main__":
    main()