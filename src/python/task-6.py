import sqlite3

"""
Det skal lages et Pytonprogram (med bruk av SQL) som lar brukeren velge en av
flyplassene i databasen, ukedag og om hen er interessert avganger eller ankomster.
Programmet skal så finne alle flyruter inn eller ut fra denne flyplassen den valgte
ukedagen. Resultatet skal bestå av flyrutenummer, avgangs- eller ankomsttid og
flyplassene ruten skal besøke eller har vært innom
"""


ukeDag = 0
flyplassKode = ""
avgang = False
ankomst = False


def finnnFlyruterTilFLyplass(ukeDag, flyplassKode, avgang, ankomst):
    conn = sqlite3.connect()
    print("Connetion successful")

    cursor = conn.cursor()

    if avgang == True:
        cursor.execute(
            """
            SELECT 
                Flyrute.Flyrutenummer, 
                Flyrute.Ukedagskode, 
                Flyrute.PlanlagtAvgangstid, 
                FLyrute.StartFlyplass,
                Flyrute.SluttFlyplass 
            FROM 
                Flyrute
            WHERE 
                FLyrute.StartFlyplass = ?
                AND ? in Flyrute.Ukedagskode
                       
            """,
            [flyplassKode, ukeDag],
        )
    elif ankomst == True:
        cursor.execute(
            """
            SELECT 
                Flyrute.Flyrutenummer, 
                Flyrute.Ukedagskode, 
                Flyrute.PlanlagtAvgangstid, 
                FLyrute.StartFlyplass,
                Flyrute.SluttFlyplass 
            FROM 
            Flyrute
            WHERE FLyrute.StartFlyplass = '{flyplassKode}'
                       
            """
        )

    conn.close()


# "SELECT weight FROM Equipment WHERE name = :name AND price = :price",
#     {"name": "lead", "price": 24},
