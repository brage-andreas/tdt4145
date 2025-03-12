-- TODO: uferdig fil
--
INSERT INTO
  Flyrute (
    FlyruteId,
    Flyrutenummer,
    Ukedagskode,
    PlanlagtAvgangstid,
    PlanlagtAnkomsttid,
    StartFlyplass,
    SluttFlyplass,
    Flytype
  )
VALUES
  (
    1,
    1311,
    12345,
    '15:15',
    '16:20',
    'TRD',
    'BOO',
    'Dash-8 100'
  ),
  (
    2,
    1302,
    12345,
    '07:35',
    '08:40',
    'BOO',
    'TRD',
    'Dash-8 100'
  ),
  (
    3,
    753,
    1234567,
    '10:20',
    '11:15',
    'TRD',
    'OSL',
    'Boeing 737 800'
  ),
  (
    4,
    332,
    1234567,
    '08:00',
    '09:05',
    'OSL',
    'TRD',
    'Airbus a320neo'
  ),
  (
    4,
    888,
    12345,
    '10:00',
    '12:10',
    'TRD',
    'SVG',
    'Airbus a320neo'
  ),
  (
    5,
    888,
    12345,
    '10:00',
    '11:10',
    'TRD',
    'BGO',
    'Airbus a320neo'
  ),
  (
    6,
    888,
    12345,
    '11:40',
    '12:10',
    'BGO',
    'SVG',
    'Airbus a320neo'
  );

-- TODO: Mangler pga feil i modellen:
-- (888, 12345, '10:00', '11:10', 'TRD', 'BGO', 'Airbus a320neo')
--     Priser: 2000, 1500, 800. [reise: TRD-BGO]
-- (888, 12345, '11:40', '12:10', 'BGO', 'SVG', 'Airbus a320neo')
--     Priser: 1000, 700, 350. [reise: BGO-SVG]
--
INSERT INTO
  Billettpris (
    BillettprisId,
    TidOpprettet,
    Type
  )
VALUES
  (1, '2025-01-01', 'Økonomi'),
  (2, '2025-01-01', 'Økonomi'),
  (3, '2025-01-01', 'Økonomi'),
  (4, '2025-01-01', 'Økonomi'),
  (2, '2025-01-01', 'Budsjett'),
  (5, '2025-01-01', 'Budsjett'),
  (6, '2025-01-01', 'Budsjett'),
  (7, '2025-01-01', 'Budsjett');

INSERT INTO
  Budsjett (BillettprisId, Pris)
VALUES
  (1, 599),
  (1, 599),
  (2, 500),
  (2, 500),
  (3, 350),
  (4, 500),
  (4, 500),
  (2, 1000),
  (2, 1000),
  (5, 1000),
  (5, 1000),
  (6, 1500),
  (6, 1500),
  (7, 1700),
  (7, 1700);

INSERT INTO
  Økonomi (BillettprisId, Pris)
VALUES
  (1, 899),
  (1, 899),
  (2, 1000),
  (2, 1000),
  (3, 700),
  (4, 800),
  (4, 800),
  (2, 1500),
  (2, 1500),
  (5, 1500),
  (5, 1500),
  (6, 2000),
  (6, 2000),
  (7, 2200),
  (7, 2200);

INSERT INTO
  Premium (BillettprisId, Pris)
VALUES
  (1, 2018),
  (1, 2018),
  (2, 1500),
  (2, 1500),
  (3, 1000),
  (4, 1500),
  (4, 1500),
  (2, 2000),
  (2, 2000),
  (5, 1700),
  (5, 1700),
  (6, 2500),
  (6, 2500),
  (7, 2700),
  (7, 2700);