import sqlite3
import database
import subprocess
import sys
import os

days = {
    1: "Mandag",
    2: "Tirsdag",
    3: "Onsdag", 
    4: "Torsdag",
    5: "Fredag",
    6: "Lørdag",
    7: "Søndag"
}

def path_to(slug):
    base_path = os.path.join(os.path.dirname(__file__), "../..")
    return os.path.abspath(os.path.join(base_path, slug))

db_path = path_to("flydb.sqlite")

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_airports():
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT Flyplasskode, FlyplassNavn FROM Flyplass")
        airports = cursor.fetchall()
        conn.close()
        return airports
    except Exception as e:
        print(f"Klarte ikke tilkoble databasen: {e}")

def display_header():
    print("-"*50)
    print("FlyDB supermegaprogram v2.3.9".center(50))
    print("-"*50)
    print()

def select_airport():
    airports = get_airports()
    
    print("Available airports:")
    for i, (code, name) in enumerate(airports, 1):
        print(f"{i}. {code} - {name}")
    
    while True:
        try:
            choice = int(input(f"\nVelg flyplass (1-{len(airports)}): "))
            if 1 <= choice <= len(airports):
                return airports[choice-1][0]
            else:
                print("Ugyldig valg. Prøv igjen.")
        except ValueError:
            print("Vennligst skriv inn et tall.")

def select_day_of_week():    
    print("\nUkedager:")
    for num, day in days.items():
        print(f"{num}. {day}")
    
    while True:
        try:
            choice = int(input("\nVelg dag (1-7): "))
            if 1 <= choice <= 7:
                return choice
            else:
                print("Ugyldig valg. Prøv igjen.")
        except ValueError:
            print("Vennligst skriv inn et tall.")

def select_flight_direction():
    print("\nVelg retning:")
    print("1. Avganger")
    print("2. Ankomster")
    
    while True:
        try:
            choice = int(input("\nVelg (1-2): "))
            if choice == 1:
                return True, False  # avgang=True, ankomst=False
            elif choice == 2:
                return False, True  # avgang=False, ankomst=True
            else:
                print("Ugyldig valg. Prøv igjen.")
        except ValueError:
            print("Vennligst skriv inn et tall.")

def run_task_6(airport_code, day_of_week, is_departure, is_arrival):
    try:
        import task_6
        
        results = task_6.find_flight_routes_to_airport(day_of_week, airport_code, is_departure, is_arrival)
        
        print(f"\nViser {"avganger" if is_departure else "ankomster"} for {airport_code} på {days[day_of_week].lower()}er.\n") 

        if results:
            print(f"{"Flyreise":<10}  {f"{"Avgangs" if is_departure else "Ankomst"}tid":<10}  {"Flyplasser":<30}")
            for row in results:
                print(f"{row[0]:<10}  {row[1]:<10}  {', '.join(row[2]):<30}")
        else:
            print("\nIngen resultater.")
    
    except Exception as e:
        print(f"Error: {e}")
        print("task_6.py kan være feilkonfigurert.")

def run_task_8(flight_route_id, flight_sequence_number):
    try:
        import task_8
        
        # dict<number, list<str>>
        results = task_8.find_avaiable_seats(flight_route_id, flight_sequence_number)

        if results:
            print(f"\nViser ledige seter for flyreise {flight_route_id}-{flight_sequence_number}.\n")
            for row_number, seats in results.items():
                print(f"Rad {row_number}: {', '.join(seats)}")
        else:
            print("\nIngen resultater.")
        
    except Exception as e:
        print(f"Error: {e}")
        print("task_8.py kan være feilkonfigurert.")

def main_menu():
    while True:
        display_header()
        print("1. Finn flyreiser")
        print("2. Finn ledige seter")
        print("3. -")
        print("4. -")
        print("5. -")
        print("6. -")
        print("7. Slett og opprett tom database")
        print("8. Fyll databasen")
        print("9. Avslutt")
        
        try:
            choice = int(input("\nVelg: "))
            
            if choice == 1:
                display_header()

                airport_code = select_airport()
                day_of_week = select_day_of_week()
                is_departure, is_arrival = select_flight_direction()
                
                run_task_6(airport_code, day_of_week, is_departure, is_arrival)
                
                input("\nTrykk Enter for å fortsette.")
                clear_screen()

            elif choice == 2:
                display_header()

                flight_route_id = 2
                flight_sequence_number = 2

                run_task_8(flight_route_id, flight_sequence_number)

                input("\nTrykk Enter for å fortsette.")
                clear_screen()

            elif choice == 7:
                display_header()
                confirm = input("Er du sikker på at du vil slette og opprette en ny database? (j/n): ")
                if confirm.lower() == "j":
                    database.destroy()
                    database.create()
                else:
                    print("Avbrutt.")
                input("Trykk Enter for å fortsette.")
                clear_screen()

            elif choice == 8:
                display_header()
                confirm = input("Er du sikker på at du vil fylle databasen? (j/n): ")
                if confirm.lower() == "j":
                    database.populate()
                    database.check_data()
                else:
                    print("Avbrutt.")
                input("Trykk Enter for å fortsette.")
                clear_screen()

            elif choice == 9:
                print("\nHa en fin dag!")
                break
            
            else:
                print("Ugyldig valg. Prøv igjen.")
                input("Trykk Enter for å fortsette.")
                clear_screen()
        
        except ValueError:
            print("Vennligst skriv inn et tall.")
            input("Trykk Enter for å fortsette.")
            clear_screen()

def run():
    clear_screen()
    print("Sjekker om databasen eksisterer...")

    if not database.exists():
        print("Databasen finnes ikke.")
        if not database.create():
            sys.exit(1)
        else:
            input("Trykk Enter for å fortsette.")
    else:
        print("Databasen finnes.")
    
    print("\n")
    main_menu()

if __name__ == "__main__":
    run()
