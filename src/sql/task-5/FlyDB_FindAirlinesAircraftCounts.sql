SELECT
  Flyselskap.Navn AS Flyselskap,
  Flytype.Navn AS Flytype,
  COUNT(Fly.Registreringsnummer) AS AntallFly
FROM
  Flyselskap
  JOIN Fly ON Flyselskap.Flyselskapkode = Fly.FlyselskapKode
  JOIN Flytype ON Fly.FlytypeNavn = Flytype.Navn
GROUP BY
  Flyselskap.Navn,
  Flytype.Navn
ORDER BY
  Flyselskap.Navn,
  Flytype.Navn;