import os
import sqlite3
import queries

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

def get_flight_routes_to_airport_with_connected_airports(weekdayCode, airportCode, isDeparture, isArrival):
    result = []
    
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    intermediate_result = queries.get_flight_routes_to_airport(
        cursor,
        weekdayCode,
        airportCode,
        isDeparture,
        isArrival
    )
    
    for route_number, company_code, time in intermediate_result:
        connected_airports = queries.get_connected_airports_by_route_number(cursor, route_number)

        airports = [airport[0] for airport in connected_airports]

        result.append((f"{company_code}{route_number}", time, airports))
    
    conn.close()
  
    return result
