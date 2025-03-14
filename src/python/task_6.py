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

flight_routes_query = f"""
    SELECT
      fr.Flyrutenummer,
      CASE
        WHEN :isDeparture = 1 THEN fr.PlanlagtAvgangstid
        WHEN :isArrival = 1 THEN fr.PlanlagtAnkomsttid
      END AS Tid
    FROM
      Flyrute fr
    WHERE
      fr.Ukedagskode LIKE :weekday
      AND (
        (
          :isDeparture = 1
          AND fr.StartFlyplass = :airport
        )
        OR (
          :isArrival = 1
          AND fr.SluttFlyplass = :airport
        )
      );
"""

connected_airports_query = """
    SELECT DISTINCT
      fp.Flyplasskode
    FROM
      Flyplass fp
    WHERE
      fp.Flyplasskode IN (
        SELECT
          StartFlyplass
        FROM
          Flyrute
        WHERE
          Flyrutenummer = :routeNumber
        UNION
        SELECT
          SluttFlyplass
        FROM
          Flyrute
        WHERE
          Flyrutenummer = :routeNumber
      );
"""

def find_flight_routes_to_airport(weekdayCode, airportCode, isDeparture, isArrival):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute(
        flight_routes_query,
        {
            "airport": airportCode,
            "weekday": f"%{weekdayCode}%",
            "isArrival": isArrival,
            "isDeparture": isDeparture
        }
    )

    intermediate_result = cursor.fetchall()
    result = []

    for row in intermediate_result:
        cursor.execute(connected_airports_query, {"routeNumber": row[0]})
        connected_airports = cursor.fetchall()

        route_number = row[0]
        time = row[1]
        airports = [airport[0] for airport in connected_airports]

        result.append((route_number, time, airports))
    
    conn.close()
    return result
