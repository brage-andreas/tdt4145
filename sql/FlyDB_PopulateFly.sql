/*
Norwegian flyr med Boeing 737 800. Vi begrenser oss til å registrere fire fly av denne
typen:
Serienummer 42069 med registreringsnummer LN-ENU. Flyet ble tatt i bruk i
2015.
 Serienummer 42093 med registreringsnummer LN-ENR. Flyet heter Jan Bålsrud
og ble tatt i bruk i 2018.
 Serienummer 39403 med registreringsnummer LN-NIQ. Flyet heter Max Manus
og ble tatt i bruk i 2011.
 Serienummer 42281 med registreringsnummer LN-ENS. Flyet ble tatt i bruk i
2017.

SAS flyr med Airbus a320neo. Vi begrenser oss til å registrere fire fly av denne typen:
 Serienummer 9518 som heter Birger Viking og ble tatt i bruk i 2020.
Registreringsnummer er SE-RUB.
 Serienummer 11421 som heter Nora Viking og ble tatt i bruk i 2023.
Registreringsnummer er SE-DIR.
 Serienummer 12066 som heter Ragnhild Viking og ble tatt i bruk i 2024.
Registreringsnummer er SE-RUP.
 Serienummer 12166 som heter Ebbe Viking og ble tatt i bruk i 2024.
Registreringsnummer er SE-RZE.

Widerøe flyr med Dash-8 100. Vi begrenser oss til å registrere tre fly av denne typen:
 Serienummer 383, registreringsnummer LN-WIH. Heter Oslo og ble tatt i bruk i
1994.
 Serienummer 359, registreringsnummer LN-WIA. Heter Nordland og ble tatt i
bruk i 1993.
 Serienummer 298, registreringsnummer LN-WIL. Heter Narvik og ble tatt i bruk i
1995.

Registreringsnummer VARCHAR(50) NOT NULL,
Serienummer         VARCHAR(50) NOT NULL,
Navn                VARCHAR(50),
Driftsår            INT,
FlyprodusentNavn    VARCHAR(50) NOT NULL,
FlytypeNavn         VARCHAR(50) NOT NULL,
FlyselskapKode      VARCHAR(10) NOT NULL,
 */
INSERT INTO
  Fly (
    Registreringsnummer,
    Serienummer,
    Navn,
    Driftsår,
    FlyprodusentNavn,
    FlytypeNavn,
    FlyselskapKode
  )
VALUES
  (
    'LN-ENU',
    '42069',
    NULL,
    2015,
    'The Boeing Company',
    'Boeing 737 800',
    'DY'
  ),
  (
    'LN-ENR',
    '42093',
    'Jan Bålsrud',
    2018,
    'The Boeing Company',
    'Boeing 737 800',
    'DY'
  ),
  (
    'LN-NIQ',
    '39403',
    'Max Manus',
    2011,
    'The Boeing Company',
    'Boeing 737 800',
    'DY'
  ),
  (
    'LN-ENS',
    '42281',
    NULL,
    2017,
    'The Boeing Company',
    'Boeing 737 800',
    'DY'
  ),
  (
    'SE-RUB',
    '9518',
    'Birger Viking',
    2020,
    'Airbus Group',
    'Airbus a320neo',
    'SK'
  ),
  (
    'SE-DIR',
    '11421',
    'Nora Viking',
    2023,
    'Airbus Group',
    'Airbus a320neo',
    'SK'
  ),
  (
    'SE-RUP',
    '12066',
    'Ragnhild Viking',
    2024,
    'Airbus Group',
    'Airbus a320neo',
    'SK'
  ),
  (
    'SE-RZE',
    '12166',
    'Ebbe Viking',
    2024,
    'Airbus Group',
    'Airbus a320neo',
    'SK'
  ),
  (
    'LN-WIH',
    '383',
    'Oslo',
    1994,
    'De Havilland Canada',
    'Dash-8 100',
    'WF'
  ),
  (
    'LN-WIA',
    '359',
    'Nordland',
    1993,
    'De Havilland Canada',
    'Dash-8 100',
    'WF'
  ),
  (
    'LN-WIL',
    '298',
    'Narvik',
    1995,
    'De Havilland Canada',
    'Dash-8 100',
    'WF'
  );