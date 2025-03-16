import os
import sqlite3

def path_to(slug):
    base_path = os.path.join(os.path.dirname(__file__), "../..")
    return os.path.abspath(os.path.join(base_path, slug))

sql_schema_path = path_to("src/sql/FlyDB_CreateTables.sql")
db_path = path_to("flydb.sqlite")

def exists():
    try:
        if not os.path.exists(db_path):
            return False
            
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        
        # Check if any tables exist
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='Flyplass'")
        tables = cursor.fetchone()
        
        conn.close()
        return tables is not None
    except Exception as e:
        print(f"Feil ved databasesjekk: {e}")
        return False

def destroy():
    print("Sletter database...")
    try:
        os.remove(db_path)
        print("Database slettet.")
    except Exception as e:
        print(f"Feil ved sletting av database: {e}")

def create():
    try:
        print("Oppretter database...")
        
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        
        with open(sql_schema_path, 'r', encoding='utf-8') as f:
            sql_script = f.read()
            
        cursor.executescript(sql_script)
        conn.commit()
        conn.close()
        
        print("Database opprettet.")
        return True
    except Exception as e:
        print(f"Feil ved databaseopprettelse: {e}")
        print(f"Path: {sql_schema_path}")
        return False

def populate():
    sql_files = [
        "src/sql/task-1/FlyDB_PopulateFlyplass.sql",

        "src/sql/task-2/FlyDB_PopulateFlyselskap.sql", 
        "src/sql/task-2/FlyDB_PopulateFlytype.sql",
        "src/sql/task-2/FlyDB_PopulateFly.sql",

        "src/sql/task-3/FlyDB_PopulateFlyrute.sql",
        "src/sql/task-3/FlyDB_PopulateDelreise.sql",

        "src/sql/task-4/FlyDB_PopulateFlyvning.sql",

        "src/sql/task-5/FlyDB_FindAirlinesAircraftCounts.sql",

        "src/sql/task-7/FlyDB_PopulateBestillinger.sql",
    ]

    print("Fyller databasen med data...")

    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
                
        for sql_file in sql_files:
            file_path = path_to(sql_file)

            print(f"  - Kjører {sql_file}... ", end="")
            
            if not os.path.exists(file_path):
                print("Filen finnes ikke. Hopper over.")
                continue
                
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    sql_script = f.read()
                
                try:
                    cursor.executescript(sql_script)
                    conn.commit()
                    print("OK")
                except sqlite3.Error as e:
                    print(f"Feil:\n{" "*6}{e.args[0].replace("\n", f"\n{" "*6}")}")
                    
            except Exception as e:
                print(f"Kunne ikke lese fil:\n{" "*6}{e.args[0].replace("\n", f"\n{" "*6}")}")
        
        conn.close()
        print("Database fylt.")
        return True
        
    except Exception as e:
        print(f"Feil ved fylling av database: {e}")
        return False

def check_data():
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        
        tables = ["Flyplass", "Flyselskap", "Flytype", "Fly", "Flyrute"]
        
        has_data = True
        for table in tables:
            cursor.execute(f"SELECT COUNT(*) FROM {table}")
            count = cursor.fetchone()[0]
            if count == 0:
                has_data = False
                print(f"Tabell {table} er tom.")
                
        conn.close()
        return has_data
        
    except Exception as e:
        print(f"Feil ved datasjekk: {e}")
        return False
