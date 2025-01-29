import logging


logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def is_number(value):
    """Funkcja sprawdza, czy wartość jest liczbą."""
    try:
        float(value)
        return True
    except ValueError:
        return False

def get_number(prompt):
    """Pobierz liczbę od użytkownika, sprawdzając poprawność."""
    while True:
        value = input(prompt)
        if is_number(value):
            return float(value)
        else:
            print("Podana wartość nie jest liczbą. Spróbuj ponownie.")

def calculator():
    print("Podaj działanie, posługując się odpowiednią liczbą jak poniżej:")
    print("1. Dodawanie")
    print("2. Odejmowanie")
    print("3. Mnożenie")
    print("4. Dzielenie")

    operation = input("Wybierz działanie (1-4): ")
    if operation not in {"1", "2", "3", "4"}:
        print("Nieprawidłowy wybór. Uruchom program ponownie i podaj liczbę od 1 do 4.")
        return

    # Dodawanie i mnożenie mogą przyjmować więcej liczb
    if operation in {"1", "3"}:
        print("Wprowadź liczby, oddzielając je spacjami (np. '2 3 4').")
        numbers = input("Podaj liczby: ").split()
        if all(is_number(num) for num in numbers):
            numbers = [float(num) for num in numbers]
        else:
            print("Nie wszystkie podane wartości są liczbami. Spróbuj ponownie.")
            return
    else:
        # Odejmowanie i dzielenie przyjmują tylko dwie liczby
        num1 = get_number("Podaj liczbę 1: ")
        num2 = get_number("Podaj liczbę 2: ")
        numbers = [num1, num2]

    # Wykonanie wybranego działania
    if operation == "1":  # Dodawanie
        result = sum(numbers)
        logging.info(f"Dodaję: {' + '.join(map(str, numbers))}")
    elif operation == "2":  # Odejmowanie
        result = numbers[0] - numbers[1]
        logging.info(f"Odejmuję: {numbers[0]} - {numbers[1]}")
    elif operation == "3":  # Mnożenie
        result = 1
        for num in numbers:
            result *= num
        logging.info(f"Mnożę: {' x '.join(map(str, numbers))}")
    elif operation == "4":  # Dzielenie
        if numbers[1] == 0:
            print("Dzielenie przez zero jest niedozwolone.")
            return
        result = numbers[0] / numbers[1]
        logging.info(f"Dzielę: {numbers[0]} / {numbers[1]}")


    print(f"Wynik to: {result:.2f}")


calculator()
