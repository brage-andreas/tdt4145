import os
import sqlite3
import queries

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

def get_available_seats(flight_route_id):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    sequences = queries.get_sequence_by_route_id(cursor, flight_route_id)

    available_seats = []

    for (sequence_id, start_airport, end_airport) in sequences:
        seat_configuration = queries.get_seat_configuration(cursor, flight_route_id)        
        taken_seats = queries.get_taken_seats(cursor, flight_route_id, sequence_id)
        all_seats = get_all_seats_from_configuration(seat_configuration)

        available_seats.append(
            [
                start_airport,
                end_airport,
                [seat for seat in all_seats if seat not in taken_seats]
            ]
        )

    conn.close()
    
    return available_seats
