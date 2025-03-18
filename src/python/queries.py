flight_routes_query = f"""
    SELECT
      fr.Flyrutenummer,
      ftea.FlyselskapsKode,
      CASE
        WHEN :isDeparture = 1 THEN fr.PlanlagtAvgangstid
        WHEN :isArrival = 1 THEN fr.PlanlagtAnkomsttid
      END AS Tid
    FROM
      Flyrute fr
      LEFT JOIN Flytype ft ON fr.Flytype = ft.Navn
      LEFT JOIN FlytypeEidAv ftea ON ftea.FlytypeNavn = ft.Navn
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
def get_flight_routes_to_airport(cursor, weekday_code, airport_code, is_departure, is_arrival):
    """
    Returns: List<(route_number, time)>
    """

    cursor.execute(
        flight_routes_query,
        {
            "weekday": f"%{weekday_code}%",
            "airport": airport_code,
            "isDeparture": is_departure,
            "isArrival": is_arrival
        }
    )

    return cursor.fetchall()

connected_airports_with_route_number_query = """
    SELECT DISTINCT
      fp.Flyplasskode, fp.FlyplassNavn
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
def get_connected_airports_by_route_number(cursor, route_number):
    """
    Returns: List<(airport_code, airport_name)>
    """

    cursor.execute(
        connected_airports_with_route_number_query,
        {
            "routeNumber": route_number
        }
    )

    return cursor.fetchall()

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
def get_seat_configuration(cursor, flight_route_id):
    """
    Returns: seat_configuration
    """

    cursor.execute(
        seat_configuration_query,
        {
            "routeId": flight_route_id
        }
    )

    result = cursor.fetchone()

    return result[0] if result else None

taken_seats_query = """
    SELECT
      Setenummer
    FROM
      DelreiseIBillettbestilling
    WHERE
      FlyruteId = :routeId
      AND DelreiseId = :sequenceNumber
      AND Setenummer IS NOT NULL
"""
def get_taken_seats(cursor, flight_route_id, sequence_number):
    """
    Returns: List<seat_number>
    """

    cursor.execute(
        taken_seats_query,
        {
            "routeId": flight_route_id,
            "sequenceNumber": sequence_number
        }
    )

    return [res[0] for res in cursor.fetchall()]

get_sequence_by_route_id_query = """
    SELECT
      DelreiseId,
      Startflyplasskode,
      Endeflyplasskode
    FROM
      Delreise
    WHERE
      FlyruteId = :routeId
"""
def get_sequence_by_route_id(cursor, flight_route_id):
    """
    Returns: List<sequence_number, start_airport_code, end_airport_code>
    """

    cursor.execute(
        get_sequence_by_route_id_query,
        {
            "routeId": flight_route_id
        }
    )

    return cursor.fetchall()

get_flight_routes_query = """
SELECT
  FlyruteId, Flyrutenummer
FROM
  Flyrute
"""
def get_flight_routes(cursor):
    """
    Returns: List<(route_id, route_number)>
    """

    cursor.execute(get_flight_routes_query)

    return cursor.fetchall()