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
