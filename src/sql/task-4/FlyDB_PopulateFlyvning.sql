INSERT INTO
  FlyvningStatus (StatusId, Status)
VALUES
  (1, 'PLANNED'),
  (2, 'ACTIVE'),
  (3, 'COMPLETED'),
  (4, 'CANCELLED');

INSERT INTO
  Flyvning (
    FlyruteId,
    Løpenummer,
    StatusId,
    FaktiskAvgangstid,
    FaktiskAnkomsttid,
    Avgangsdato,
    Ankomstdato,
    Flyregistreringsnummer
  )
VALUES
  (
    2,
    1,
    1, -- status planned
    NULL,
    NULL,
    '2025-04-01 00:00',
    '2025-04-01 00:00',
    'LN-WIA'
  ),
  (
    3,
    2,
    1, -- status planned
    NULL,
    NULL,
    '2025-04-01 00:00',
    '2025-04-01 00:00',
    'LN-ENR'
  ),
  (
    5,
    3,
    1, -- status planned
    NULL,
    NULL,
    '2025-04-01 00:00',
    '2025-04-01 00:00',
    'SE-RUB'
  ),
  (
    6,
    4,
    1, -- status planned
    NULL,
    NULL,
    '2025-04-01 00:00',
    '2025-04-01 00:00',
    'SE-RUB'
  ),
  (
    7,
    5,
    1, -- status planned
    NULL,
    NULL,
    '2025-04-01 00:00',
    '2025-04-01 00:00',
    'SE-RUB'
  );