import os
import sqlite3

"""
Det skal lages et Pytonprogram (med bruk av SQL) som lar brukeren velge en flyvning
(altså en flyrute på en bestemt dato) og som finner ledige seter på hver delflyvning.
Du trenger ikke legging inn bestilling, men kunne finne mulige seter til en tur.
"""

def path_to(slug):
    base_path = os.path.join(os.path.dirname(__file__), "../..")
    return os.path.abspath(os.path.join(base_path, slug))

db_path = path_to("flydb.sqlite")

def get_all_seats_from_configuration(configuration):
    SEAT_GROUP_DIVIDER = "-"
    UNAVAILABLE_SEAT = "*"
    result = []

    rows = configuration.split("|")
    
    for row_number, seat_row in enumerate(rows, start=1):
        clean_seats = seat_row.replace(SEAT_GROUP_DIVIDER, "").replace(UNAVAILABLE_SEAT, "")
        
        for seat in clean_seats:
            result.append(f"{row_number}{seat}")
    
    return result

seat_configuration_query = """
    SELECT
      sk.SeteKonfig
    FROM
      Setekonfigurasjon sk
      INNER JOIN Flytype ft ON sk.Id = ft.SetekonfigurasjonId
      INNER JOIN Flyrute fr ON ft.Navn = fr.Flytype
    WHERE
      fr.FlyruteId = :routeId
"""

taken_seats_query = """
    SELECT
      dib.Setenummer,
      dib.DelreiseId
    FROM
      DelreiseIBillettbestilling dib
    WHERE
      dib.FlyruteId = :routeId
      AND dib.Setenummer IS NOT NULL
"""

def find_avaiable_seats(flight_route_id, flight_sequence_number):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute(
        seat_configuration_query,
        {
            "routeId": flight_route_id
        }
    )

    seat_configuration_result = cursor.fetchone()
    
    if not seat_configuration_result:
        conn.close()
        return
        
    
    all_seats = get_all_seats_from_configuration(seat_configuration_result[0])
    
    cursor.execute(
        taken_seats_query,
        {
            "routeId": flight_route_id
        }
    )

    taken_seats_result = cursor.fetchall()

    available_seats = {}
    for seat_number, flight_segment in taken_seats_result:
        if flight_segment not in available_seats:
            available_seats[flight_segment] = all_seats.copy()
        
        available_seats[flight_segment].remove(seat_number)
        
    conn.close()
    
    return available_seats
