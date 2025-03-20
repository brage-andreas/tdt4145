import sqlite3
import subprocess
import sys
import os
import database
import queries

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
    print("FlyDB superprogram".center(50))
    print("-"*50)

def select_airport():
    airports = get_airports()
    
    print("\nMulige flyplasser:")
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

def select_flight_route():
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    routes = queries.get_all_flight_routes(cursor)

    conn.close()
    
    print("\nTilgjengelige flyruter:")
    for i, (route_id, route_number, company_code, start_airport, end_airport) in enumerate(routes, 1):
        print(f"{i}. {f'{company_code}{route_number}':<8} {start_airport} → {end_airport}")
    
    while True:
        try:
            choice = int(input(f"\nVelg flyrute (1-{len(routes)}): "))
            if 1 <= choice <= len(routes):
                return (routes[choice-1][0], routes[choice-1][1])
            else:
                print("Ugyldig valg. Prøv igjen.")
        except ValueError:
            print("Vennligst skriv inn et tall.")

def run_task_5():
    task_5_file = "src/sql/task-5/FlyDB_FindAirlinesAircraftCounts.sql"
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        with open(path_to(task_5_file), 'r', encoding='utf-8') as f:
            sql_script = f.read()
        cursor.execute(sql_script)
        results = cursor.fetchall()
        conn.close()
        
        print("\nViser flyselskaper og antall fly:\n")
        print(f"{'Flyselskap':<15}  {'Flytype':<20}  {'Antall fly':<10}")
        for row in results:
            print(f"{row[0]:<15}  {row[1]:<20}  {row[2]:<10}")
    except Exception as e:
        print("FlyDB_FindAirlinesAircraftCounts kan være feilkonfigurert.")

def run_task_6(airport_code, day_of_week, is_departure, is_arrival):
    try:
        import task_6
        
        results = task_6.get_flight_routes_to_airport_with_connected_airports(
            day_of_week,
            airport_code,
            is_departure,
            is_arrival
        )
        
        print(f"\nViser {"avganger" if is_departure else "ankomster"} for {airport_code} på {days[day_of_week].lower()}er.\n") 

        if results:
            print(f"{"Flyreise":<10}  {f"{"Avgangs" if is_departure else "Ankomst"}tid":<10}  {"Flyplasser":<30}")
            for row in results:
                print(f"{row[0]:<10}  {row[1]:<10}  {', '.join(row[2]):<30}")
        else:
            print("\nIngen resultater.")
    
    except Exception:
        print("task_6.py kan være feilkonfigurert.")

def run_task_8(flight_route_id, flight_route_number):
    try:
        import task_8
        
        route_number_string, results = task_8.get_available_seats(flight_route_id, flight_route_number)

        if not results:
            print("\nIngen resultater.")
            return

        print(f"\nViser ledige seter for flyreise {route_number_string}.\n")
        for i, [start_airport_code, end_airport_code, seats] in enumerate(results, 1):
            print(f"{i}.  {start_airport_code} → {end_airport_code}: {', '.join(seats)}")
        
    except Exception:
        print("task_8.py kan være feilkonfigurert.")

def main_menu():
    while True:
        clear_screen()
        display_header()
        print("1. Finn flyselskaper og antall fly  (opg. 5)")
        print("2. Finn flyreiser  (opg. 6)")
        print("3. Finn ledige seter  (opg. 8)")
        print("4. -")
        print("5. -")
        print("6. -")
        print("7. Slett og opprett tom database")
        print("8. Fyll databasen  (opg. 1, 2, 3, 4, 7)")
        print("9. Avslutt")
        
        try:
            choice = int(input("\nVelg (1-9): "))
            
            if choice == 1:
                run_task_5()

                input("\nTrykk Enter for å fortsette.")

            elif choice == 2:
                airport_code = select_airport()
                day_of_week = select_day_of_week()
                is_departure, is_arrival = select_flight_direction()
                
                run_task_6(airport_code, day_of_week, is_departure, is_arrival)
                
                input("\nTrykk Enter for å fortsette.")

            elif choice == 3:
                flight_route_id, flight_route_number = select_flight_route()

                run_task_8(flight_route_id, flight_route_number)

                input("\nTrykk Enter for å fortsette.")

            elif choice == 7:
                confirm = input("Er du sikker på at du vil slette og opprette en ny database? (j/n): ")
                if confirm.lower() == "j":
                    database.destroy()
                    database.create()
                else:
                    print("Avbrutt.")
                input("Trykk Enter for å fortsette.")

            elif choice == 8:
                confirm = input("Er du sikker på at du vil fylle databasen? (j/n): ")
                if confirm.lower() == "j":
                    database.populate()
                    database.check_data()
                else:
                    print("Avbrutt.")
                input("Trykk Enter for å fortsette.")

            elif choice == 9:
                print("\nHa en fin dag!")
                break
            
            else:
                print("Ugyldig valg. Prøv igjen.")
                input("Trykk Enter for å fortsette.")
        
        except ValueError as e:
            print(e)
            print("Vennligst skriv inn et tall.")
            input("Trykk Enter for å fortsette.")

def run():
    print("Sjekker om databasen eksisterer...")

    if not database.exists():
        print("Databasen finnes ikke.")
        if not database.create():
            sys.exit(1)
        else:
            input("Trykk Enter for å fortsette.")
    else:
        print("Databasen finnes.")
    
    print("Sjekker om databasen er tom...")
    if not database.check_data():
        confirm = input("Vil du fylle databasen nå? (j/n): ")
        if confirm.lower() == "j":
            database.populate()
            database.check_data()
        else:
            print("Avbrutt. Databasen er ikke fylt")
        input("Trykk Enter for å fortsette.")
    else:
        print("Databasen er ikke tom.")

    main_menu()

if __name__ == "__main__":
    run()
