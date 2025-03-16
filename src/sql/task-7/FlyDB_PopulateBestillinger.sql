INSERT INTO
  Kunde (
    Kundenummer,
    Navn,
    Telefonnummer,
    Epostadresse,
    Nasjonalitet
  )
VALUES
  (
    1,
    'Ola Nordmann',
    '12345678',
    'ola@nordmann.no',
    'Norge'
  );

INSERT INTO
  Billettbestilling (
    Referansenummer,
    TidKjøpt,
    Kundenummer,
    Type
  )
VALUES
  (1, '2025-04-01 00:00', 1, 'BUDSJETT'),
  (2, '2025-04-01 00:00', 1, 'BUDSJETT'),
  (3, '2025-04-01 00:00', 1, 'BUDSJETT'),
  (4, '2025-04-01 00:00', 1, 'OKONOMI'),
  (5, '2025-04-01 00:00', 1, 'OKONOMI'),
  (6, '2025-04-01 00:00', 1, 'OKONOMI'),
  (7, '2025-04-01 00:00', 1, 'OKONOMI'),
  (8, '2025-04-01 00:00', 1, 'PREMIUM'),
  (9, '2025-04-01 00:00', 1, 'PREMIUM'),
  (10, '2025-04-01 00:00', 1, 'PREMIUM');

INSERT INTO
  DelreiseIBillettbestilling (
    FlyruteId,
    DelreiseId,
    Referansenummer,
    Setenummer
  )
VALUES
  (2, 2, 1, '1C'),
  (2, 2, 2, '1D'),
  (2, 2, 3, '2A'),
  (2, 2, 4, '2B'),
  (2, 2, 5, '2C'),
  (2, 2, 6, '2D'),
  (2, 2, 7, '3A'),
  (2, 2, 8, '3B'),
  (2, 2, 9, '3C'),
  (2, 2, 10, '3D');