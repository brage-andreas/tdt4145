import os
import sqlite3

"""
Det skal lages et Pytonprogram (med bruk av SQL) som lar brukeren velge en av
flyplassene i databasen, ukedag og om hen er interessert avganger eller ankomster.
Programmet skal så finne alle flyruter inn eller ut fra denne flyplassen den valgte
ukedagen. Resultatet skal bestå av flyrutenummer, avgangs- eller ankomsttid og
flyplassene ruten skal besøke eller har vært innom
"""

def path_to(slug):
    base_path = os.path.join(os.path.dirname(__file__), "../..")
    return os.path.abspath(os.path.join(base_path, slug))

db_path = path_to("flydb.sqlite")

def find_flight_routes_to_airport(weekdayCode, airportCode, isDeparture, isArrival):
    query = f"""
        SELECT 
            Flyrute.Flyrutenummer, 
            Flyrute.Ukedagskode, 
            Flyrute.{"PlanlagtAnkomsttid" if isArrival else "PlanlagtAvgangstid"}, 
            FLyrute.StartFlyplass,
            Flyrute.SluttFlyplass 
        FROM 
            Flyrute
        WHERE 
            FLyrute.SluttFlyplass = :airport
            AND Flyrute.Ukedagskode LIKE :weekday
    """

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute(query, {"airport": airportCode, "weekday": f"%{weekdayCode}%"})
    results = cursor.fetchall()
    conn.close()
    return results
