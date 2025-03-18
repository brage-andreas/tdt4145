/*
Setekonfigurasjon (
Id INT NOT NULL,
Rader INT NOT NULL,
SeteKonfig VARCHAR(300) NOT NULL,
PRIMARY KEY (Id)
);
 */
INSERT INTO
  Setekonfigurasjon (Id, Rader, SeteKonfig)
VALUES
  (
    1,
    31,
    'ABC-DEF|ABC-DEF|ABC-DEF|ABC-DEF|ABC-DEF|ABC-DEF|ABC-DEF|ABC-DEF|ABC-DEF|ABC-DEF|ABC-DEF|ABC-DEF|ABC-DEF|ABC-DEF|ABC-DEF|ABC-DEF|ABC-DEF|ABC-DEF|ABC-DEF|ABC-DEF|ABC-DEF|ABC-DEF|ABC-DEF|ABC-DEF|ABC-DEF|ABC-DEF|ABC-DEF|ABC-DEF|ABC-DEF|ABC-DEF|ABC-DEF'
  ),
  (
    2,
    30,
    'ABC-DEF|ABC-DEF|ABC-DEF|ABC-DEF|ABC-DEF|ABC-DEF|ABC-DEF|ABC-DEF|ABC-DEF|ABC-DEF|ABC-DEF|ABC-DEF|ABC-DEF|ABC-DEF|ABC-DEF|ABC-DEF|ABC-DEF|ABC-DEF|ABC-DEF|ABC-DEF|ABC-DEF|ABC-DEF|ABC-DEF|ABC-DEF|ABC-DEF|ABC-DEF|ABC-DEF|ABC-DEF|ABC-DEF|ABC-DEF'
  ),
  (
    3,
    10,
    '**-CD|AB-CD|AB-CD|AB-CD|AB-CD|AB-CD|AB-CD|AB-CD|AB-CD|AB-CD'
  );

INSERT INTO
  Flytype (
    Navn,
    FørsteProdÅr,
    SisteProdÅr,
    SetekonfigurasjonId,
    FlyprodusentNavn
  )
VALUES
  (
    'Boeing 737 800',
    1997,
    2020,
    1,
    'The Boeing Company'
  ),
  ('Airbus a320neo', 2016, NULL, 2, 'Airbus Group'),
  (
    'Dash-8 100',
    1984,
    2005,
    3,
    'De Havilland Canada'
  );

INSERT INTO
  FlytypeEidAv (FlyselskapsKode, FlytypeNavn)
VALUES
  ('DY', 'Boeing 737 800'),
  ('SK', 'Airbus a320neo'),
  ('WF', 'Dash-8 100');