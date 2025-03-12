CREATE TABLE
  Flyprodusent (
    Navn VARCHAR(50) NOT NULL,
    Nasjonalitet VARCHAR(50),
    Stiftelsesår INT,
    PRIMARY KEY (Navn)
  );

CREATE TABLE
  Flyselskap (
    Flyselskapkode VARCHAR(10) NOT NULL,
    Navn VARCHAR(50),
    Land VARCHAR(50),
    PRIMARY KEY (Flyselskapkode)
  );

CREATE TABLE
  Flytype (
    Navn VARCHAR(50) NOT NULL,
    FørsteProdÅr INT,
    SisteProdÅr INT,
    SetekonfigurasjonId INT NOT NULL,
    FlyprodusentNavn VARCHAR(50) NOT NULL,
    PRIMARY KEY (Navn),
    FOREIGN KEY (FlyprodusentNavn) REFERENCES Flyprodusent (Navn) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (SetekonfigurasjonId) REFERENCES Setekonfigurasjon (Id)
  );

CREATE TABLE
  Setekonfigurasjon (
    Id INT NOT NULL,
    Rader INT NOT NULL,
    SeteKonfig VARCHAR(300) NOT NULL,
    PRIMARY KEY (Id)
  );

CREATE TABLE
  FlytypeEidAv (
    FlyselskapsKode VARCHAR(10) NOT NULL,
    FlytypeNavn VARCHAR(50) NOT NULL,
    PRIMARY KEY (FlyselskapsKode, FlytypeNavn),
    FOREIGN KEY (FlyselskapsKode) REFERENCES Flyselskap (FlyselskapKode),
    FOREIGN KEY (FlytypeNavn) REFERENCES Flytype (Navn)
  );

CREATE TABLE
  Flyplass (
    Flyplasskode VARCHAR(10) NOT NULL,
    FlyplassNavn VARCHAR(50),
    PRIMARY KEY (Flyplasskode)
  );

CREATE TABLE
  Flyrute (
    FlyruteId INT NOT NULL,
    Flyrutenummer INT NOT NULL,
    Ukedagskode INT,
    PlanlagtAvgangstid DATETIME,
    PlanlagtAnkomsttid DATETIME,
    StartFlyplass VARCHAR(10) NOT NULL,
    SluttFlyplass VARCHAR(10) NOT NULL,
    Flytype VARCHAR(50) NOT NULL,
    PRIMARY KEY (FlyruteId),
    FOREIGN KEY (StartFlyplass) REFERENCES Flyplass (Flyplasskode),
    FOREIGN KEY (SluttFlyplass) REFERENCES Flyplass (Flyplasskode),
    FOREIGN KEY (Flytype) REFERENCES Flytype (Navn)
  );

CREATE TABLE
  FlyvningStatus (
    StatusId INT NOT NULL,
    Status VARCHAR(50),
    PRIMARY KEY (StatusId)
  );

CREATE TABLE
  Fly (
    Registreringsnummer VARCHAR(50) NOT NULL,
    Serienummer VARCHAR(50) NOT NULL,
    Navn VARCHAR(50),
    Driftsår INT,
    FlytypeNavn VARCHAR(50) NOT NULL,
    FlyselskapKode VARCHAR(10) NOT NULL,
    PRIMARY KEY (Registreringsnummer),
    FOREIGN KEY (FlytypeNavn) REFERENCES Flytype (Navn),
    FOREIGN KEY (FlyselskapKode) REFERENCES Flyselskap (Flyselskapkode),
    UNIQUE (Serienummer, FlyselskapKode)
  );

CREATE TABLE
  Flyvning (
    FlyruteId INT NOT NULL,
    Løpenummer INT NOT NULL,
    StatusId INT NOT NULL,
    FaktiskAvgangstid DATETIME,
    FaktiskAnkomsttid DATETIME,
    Flyregistreringsnummer VARCHAR(50) NOT NULL,
    PRIMARY KEY (FlyruteId, Løpenummer),
    FOREIGN KEY (FlyruteId) REFERENCES Flyrute (FlyruteId),
    FOREIGN KEY (StatusId) REFERENCES FlyvningStatus (StatusId),
    FOREIGN KEY (Flyregistreringsnummer) REFERENCES Fly (Registreringsnummer)
  );

CREATE TABLE
  Kunde (
    Kundenummer INT NOT NULL,
    Navn VARCHAR(100),
    Telefonnummer VARCHAR(20),
    Epostadresse VARCHAR(100),
    Nasjonalitet VARCHAR(50),
    PRIMARY KEY (Kundenummer)
  );

CREATE TABLE
  Fordelsprogram (
    Referanse VARCHAR(50) NOT NULL,
    FlyselskapsKode VARCHAR(10) NOT NULL,
    PRIMARY KEY (Referanse),
    FOREIGN KEY (FlyselskapsKode) REFERENCES Flyselskap (Flyselskapkode)
  );

CREATE TABLE
  FordelsProgramMedlem (
    Kundenummer INT NOT NULL,
    FordelsProgramReferanse VARCHAR(50) NOT NULL,
    PRIMARY KEY (Kundenummer, FordelsProgramReferanse),
    FOREIGN KEY (Kundenummer) REFERENCES Kunde (Kundenummer),
    FOREIGN KEY (FordelsProgramReferanse) REFERENCES Fordelsprogram (Referanse)
  );

CREATE TABLE
  Billettbestilling (
    Referansenummer INT NOT NULL,
    TidKjøpt DATETIME,
    Kundenummer INT NOT NULL,
    PRIMARY KEY (Referansenummer),
    FOREIGN KEY (Kundenummer) REFERENCES Kunde (Kundenummer)
    -- TODO: Mangler foreign key til billettpris 💀
  );

-- Superklasse --
CREATE TABLE
  Billettpris (
    BillettprisId INT NOT NULL,
    TidOpprettet DATETIME,
    Type VARCHAR(20),
    PRIMARY KEY (BillettprisId)
  );

-- Subklasse ----
CREATE TABLE
  Budsjett (
    BillettprisId INT NOT NULL,
    Pris DECIMAL(10, 2),
    PRIMARY KEY (BillettprisId),
    FOREIGN KEY (BillettprisId) REFERENCES Billettpris (BillettprisId)
  );

-- Subklasse ----
CREATE TABLE
  Økonomi (
    BillettprisId INT NOT NULL,
    Pris DECIMAL(10, 2),
    PRIMARY KEY (BillettprisId),
    FOREIGN KEY (BillettprisId) REFERENCES Billettpris (BillettprisId)
  );

-- Subklasse ----
CREATE TABLE
  Premium (
    BillettprisId INT NOT NULL,
    Pris DECIMAL(10, 2),
    PRIMARY KEY (BillettprisId),
    FOREIGN KEY (BillettprisId) REFERENCES Billettpris (BillettprisId)
  );

CREATE TABLE
  Delreise (
    DelreiseId INT NOT NULL,
    FlyruteId INT NOT NULL,
    PlanlagtAvgangstid DATETIME NOT NULL,
    PlanlagtAnkomsttid DATETIME NOT NULL,
    Startflyplasskode VARCHAR(10) NOT NULL,
    Endeflyplasskode VARCHAR(10) NOT NULL,
    Bagasjeregistreringsnummer VARCHAR(50) NOT NULL,
    PRIMARY KEY (FlyruteId, DelreiseId),
    FOREIGN KEY (FlyruteId) REFERENCES Flyrute (FlyruteId),
    FOREIGN KEY (Startflyplasskode) REFERENCES Flyplass (Flyplasskode),
    FOREIGN KEY (Endeflyplasskode) REFERENCES Flyplass (Flyplasskode),
    FOREIGN KEY (Bagasjeregistreringsnummer) REFERENCES Bagasje (Registreringsnummer)
  );

CREATE TABLE
  DelreiseBillettpris (
    FlyruteId INT NOT NULL,
    DelreiseId INT NOT NULL,
    BillettprisId INT NOT NULL,
    PRIMARY KEY (FlyruteId, DelreiseId, BillettprisId),
    FOREIGN KEY (FlyruteId, DelreiseId) REFERENCES Delreise (FlyruteId, DelreiseId),
    FOREIGN KEY (BillettprisId) REFERENCES Billettpris (BillettprisId)
  );

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

CREATE TABLE
  Bagasje (
    Registreringsnummer VARCHAR(20) NOT NULL,
    Vekt DECIMAL(10, 2),
    Innleveringstidspunkt DATETIME,
    PRIMARY KEY (Registreringsnummer)
  );

CREATE TABLE
  Setereservasjon (
    Setenummer VARCHAR(10) NOT NULL,
    FlyruteId INT NOT NULL,
    DelreiseId INT NOT NULL,
    PRIMARY KEY (Setenummer, FlyruteId, DelreiseId),
    FOREIGN KEY (FlyruteId, DelreiseId) REFERENCES Delreise (FlyruteId, DelreiseId)
  );

CREATE TABLE
  BillettFlyvning (
    FlyruteId INT NOT NULL,
    Løpenummer INT NOT NULL,
    BillettReferanseNummer INT NOT NULL,
    PRIMARY KEY (FlyruteId, Løpenummer, BillettReferanseNummer),
    FOREIGN KEY (FlyruteId, Løpenummer) REFERENCES Flyvning (FlyruteId, Løpenummer),
    FOREIGN KEY (BillettReferanseNummer) REFERENCES Billettbestilling (Referansenummer)
  );