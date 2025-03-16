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

/*
CREATE TABLE
DelreiseIBillettbestilling (
FlyruteId INT NOT NULL,
DelreiseId INT NOT NULL,
Referansenummer INT NOT NULL,
Setenummer VARCHAR(10),
PRIMARY KEY (FlyruteId, DelreiseId, Referansenummer),
FOREIGN KEY (FlyruteId, DelreiseId) REFERENCES Delreise (FlyruteId, DelreiseId),
FOREIGN KEY (Referansenummer) REFERENCES Billettbestilling (Referansenummer)
);
 */
INSERT INTO
  DelreiseIBillettbestilling (
    FlyruteId,
    DelreiseId,
    Referansenummer,
    Setenummer
  )
VALUES
  (1, 1, 1, '1A'),
  (1, 1, 2, '1B'),
  (1, 1, 3, '1C'),
  (2, 2, 4, '1D'),
  (2, 2, 5, '1E'),
  (2, 2, 6, '1F'),
  (3, 3, 7, '2A'),
  (3, 3, 8, '2B'),
  (3, 3, 9, '2C'),
  (4, 4, 10, '2D'),
  (4, 4, 11, '2E'),
  (4, 4, 12, '2F'),
  (5, 5, 13, '3A'),
  (5, 5, 14, '3B'),
  (5, 5, 15, '3C'),
  (6, 6, 16, '3D'),
  (6, 6, 17, '3E'),
  (6, 6, 18, '3F'),
  (7, 7, 19, '4A'),
  (7, 7, 20, '4B'),
  (7, 7, 21, '4C');