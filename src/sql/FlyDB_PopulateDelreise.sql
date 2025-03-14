INSERT INTO
  Delreise (
    DelreiseId,
    FlyruteId,
    PlanlagtAvgangstid,
    PlanlagtAnkomsttid,
    Startflyplasskode,
    Endeflyplasskode,
  )
VALUES
  (1, 1, '15:15', '2025-10-03 16:20', 'TRD', 'BOO',),
  (2, 2, '2025-05-03 07:35', '2025-05-03 08:40', 'BOO', 'TRD',),
  (3, 3, '2025-10-03 10:20', '2025-10-03 11:15', 'TRD', 'OSL',),
  (4, 4, '2025-05-03 08:00', '2025-05-03 09:05', 'OSL', 'TRD',),
  (5, 5, '2025-01-03 10:00', '2025-01-03 12:10', 'TRD', 'SVG',),
  (6, 6, '2025-02-04 10:00', '2025-02-04 11:10', 'TRD', 'BGO',),
  (7, 7, '2025-02-04 11:40', '2025-02-04 12:10', 'BGO', 'SVG',);

INSERT INTO
  DelreiseBillettpris (FlyruteId, DelreiseId, BillettprisId)
VALUES
  (1, 1, 1),
  (1, 1, 2),
  (1, 1, 3),
  (2, 2, 4),
  (2, 2, 5),
  (2, 2, 6),
  (3, 3, 7),
  (3, 3, 8),
  (3, 3, 9),
  (4, 4, 10),
  (4, 4, 11),
  (4, 4, 12),
  (5, 5, 13),
  (5, 5, 14),
  (5, 5, 15),
  (6, 6, 16),
  (6, 6, 17),
  (6, 6, 18),
  (7, 7, 19),
  (7, 7, 20),
  (7, 7, 12);

INSERT INTO
  Billettpris (
    BillettprisId,
    TidOpprettet,
    Type
  )
VALUES
  (1, '2025-12-03 14:55', Premium),
  (2, '2025-12-03 14:55', Økonomi),
  (3, '2025-12-03 14:55', Budsjett),
  (4, '2025-12-03 14:55', Premium),
  (5, '2025-12-03 14:55', Økonomi),
  (6, '2025-12-03 14:55', Budsjett),
  (7, '2025-12-03 14:55', Premium),
  (8, '2025-12-03 14:55', Økonomi),
  (9, '2025-12-03 14:55', Budsjett),
  (10, '2025-12-03 14:55', Premium),
  (11, '2025-12-03 14:55', Økonomi),
  (12, '2025-12-03 14:55', Budsjett),
  (13, '2025-12-03 14:55', Premium),
  (14, '2025-12-03 14:55', Økonomi),
  (15, '2025-12-03 14:55', Budsjett),
  (16, '2025-12-03 14:55', Premium),
  (17, '2025-12-03 14:55', Økonomi),
  (18, '2025-12-03 14:55', Budsjett),
  (19, '2025-12-03 14:55', Premium),
  (20, '2025-12-03 14:55', Økonomi),
  (21, '2025-12-03 14:55', Budsjett);

;

INSERT INTO
  Økonomi (BillettprisId, Pris)
VALUES
  (2, 899),
  (5, 899),
  (8, 1000),
  (11, 1000),
  (14, 1500),
  (17, 700),
  (20, 1700);

INSERT INTO
  Budsjett (BillettprisId, Pris)
VALUES
  (3, 599),
  (6, 599),
  (9, 500),
  (12, 500),
  (15, 800),
  (18, 350),
  (21, 1000);

INSERT INTO
  Premium (BillettprisId, Pris)
VALUES
  (1, 2018),
  (4, 2018),
  (7, 1500),
  (10, 1500),
  (13, 2000),
  (16, 1000),
  (19, 2200);