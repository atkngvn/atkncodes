# Funktion zum Hinzufügen von zwei Zahlen
def add(x, y):
    return x + y

# Funktion zum Subtrahieren von zwei Zahlen
def subtract(x, y):
    return x - y

# Funktion zum Multiplizieren von zwei Zahlen
def multiply(x, y):
    return x * y

# Funktion zum Dividieren von zwei Zahlen
def divide(x, y):
    if y == 0:
        return "Division durch Null ist nicht erlaubt"
    return x / y

# Hauptfunktion für den Taschenrechner
def calculator():
    while True:  # Schleife, um nach jeder Berechnung erneut zu fragen
        print("Verfügbare Operationen:")
        print("1. Addition")
        print("2. Subtraktion")
        print("3. Multiplikation")
        print("4. Division")

        choice = input("Geben Sie die gewünschte Operation (1/2/3/4) ein: ")

        num1 = float(input("Geben Sie die erste Zahl ein: "))
        num2 = float(input("Geben Sie die zweite Zahl ein: "))

        if choice == '1':
            print("Ergebnis: ", add(num1, num2))
        elif choice == '2':
            print("Ergebnis: ", subtract(num1, num2))
        elif choice == '3':
            print("Ergebnis: ", multiply(num1, num2))
        elif choice == '4':
            print("Ergebnis: ", divide(num1, num2))
        else:
            print("Ungültige Eingabe")

        another_calculation = input("Möchten Sie eine weitere Berechnung durchführen? (Ja/Nein): ")
        if another_calculation.lower() != 'ja':
            break  # Die Schleife wird beendet, wenn der Benutzer "Nein" eingibt

# Den Taschenrechner aufrufen
calculator()
