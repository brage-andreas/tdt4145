# FlyDB

# Hvordan kjøre programmet

Du kan kjøre programmet med følgende kommando:

```bash
python src/main.py
# MacOS: python3 src/main.py
```

# Hvordan bruke programmet

Programmet viser en liste med valg fra 1 opp til 9. Du kan velge et valg ved å skrive inn nummeret (f.eks. 2) og trykke Enter.

Valgene er på formen:

-   Spørsmål? (1-<tall>): ...
-   Spørsmål? (j/n): ...

Da må du skrive inn en av 1, 2, 3, ..., <tall> dersom det er den øverste.
Ellers er det j for ja og n for nei.

## Eksempel på kjøring

Eksempel til tastetrykk for hver av oppgavene:

-   Oppgave 1-5 og 7: 7, J, Enter, 8, J
-   Oppgave 6: 1, 2, 1, 1
-   Oppgave 8: 2, 2

### Eksempel på oppgave 6

```
--------------------------------------------------
                FlyDB superprogram
--------------------------------------------------
1. Finn flyreiser
2. Finn ledige seter
3. -
4. -
5. -
6. -
7. Slett og opprett tom database
8. Fyll databasen
9. Avslutt

Velg: 1

Mulige flyplasser:
1. BOO - Bodø Lufthavn
2. BGO - Bergen lufthavn, Flesland
3. OSL - Oslo lufthavn, Gardermoen
4. SVG - Stavanger lufthavn, Sola
5. TRD - Trondheim lufthavn, Værnes

Velg flyplass (1-5): 2

Ukedager:
1. Mandag
2. Tirsdag
3. Onsdag
4. Torsdag
5. Fredag
6. Lørdag
7. Søndag

Velg dag (1-7): 1

Velg retning:
1. Avganger
2. Ankomster

Velg (1-2): 1

Viser avganger for BGO på mandager.

Flyreise    Avgangstid  Flyplasser
SK888       11:40       BGO, SVG, TRD

Trykk Enter for å fortsette.
```

### Eksempel på oppgave 8

```
--------------------------------------------------
                FlyDB superprogram
--------------------------------------------------
1. Finn flyreiser
2. Finn ledige seter
3. -
4. -
5. -
6. -
7. Slett og opprett tom database
8. Fyll databasen
9. Avslutt

Velg: 2

Tilgjengelige flyruter:
1. WF1311   TRD → BOO
2. WF1302   BOO → TRD
3. DY753    TRD → OSL
4. SK332    OSL → TRD
5. SK888    TRD → SVG

Velg flyrute (1-5): 2

Viser ledige seter for flyreise WF1302.

1.  BOO → TRD: 4A, 4B, 4C, 4D, 5A, 5B, 5C, 5D, 6A, 6B, 6C, 6D, 7A, 7B, 7C, 7D, 8A, 8B, 8C, 8D, 9A, 9B, 9C, 9D, 10A, 10B, 10C, 10D

Trykk Enter for å fortsette.
```
