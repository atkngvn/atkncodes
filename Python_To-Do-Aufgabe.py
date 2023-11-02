# Eine leere Liste für die To-Do-Aufgaben erstellen
tasks = []

# Funktion zum Hinzufügen einer Aufgabe zur Liste
def add_task():
    task = input("Geben Sie die Aufgabe ein: ")
    tasks.append(task)
    print("Aufgabe hinzugefügt.")

# Funktion zum Anzeigen der To-Do-Liste
def show_tasks():
    print("To-Do-Liste:")
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task}")

# Funktion zum Löschen einer Aufgabe aus der Liste
def delete_task():
    show_tasks()
    task_number = int(input("Geben Sie die Nummer der Aufgabe ein, die Sie löschen möchten: "))

    if 1 <= task_number <= len(tasks):
        deleted_task = tasks.pop(task_number - 1)
        print(f"Aufgabe '{deleted_task}' gelöscht.")
    else:
        print("Ungültige Aufgabennummer.")

# Hauptschleife
while True:
    print("\nWas möchten Sie tun?")
    print("1. Aufgabe hinzufügen")
    print("2. To-Do-Liste anzeigen")
    print("3. Aufgabe löschen")
    print("4. Beenden")

    choice = input("Ihre Wahl: ")

    if choice == "1":
        add_task()
    elif choice == "2":
        show_tasks()
    elif choice == "3":
        delete_task()
    elif choice == "4":
        print("Programm beendet.")
        break
    else:
        print("Ungültige Eingabe. Bitte wählen Sie eine der Optionen (1-4).")
