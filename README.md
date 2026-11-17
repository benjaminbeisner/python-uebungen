# Python-Übungen · Python Exercises

[![Tests](https://github.com/benjaminbeisner/python-uebungen/actions/workflows/tests.yml/badge.svg)](https://github.com/benjaminbeisner/python-uebungen/actions/workflows/tests.yml)

🇩🇪 [Deutsch](#deutsch) · 🇬🇧 [English](#english)

<a name="deutsch"></a>
## 🇩🇪 Deutsch

18 meiner Python-Übungen aus der Umschulung zum Fachinformatiker für Anwendungsentwicklung (IBB, Hameln), von März bis September 2026. Die Reihenfolge zeigt meinen Lernweg: von Schleifen und Bedingungen über Listen und Dateien bis zu Klassen, GUI und Unit-Tests.

Die Programme habe ich im Unterricht selbst geschrieben. Für diese Veröffentlichung habe ich sie aufgeräumt und einzelne Fehler behoben.

| Nr. | Übung | Darum geht es | Schwerpunkte |
|---|---|---|---|
| 01 | [Entscheidungstabelle](01_entscheidungstabelle) | Rechnungsbetrag mit Rabatt je nach Bestellwert und Vorkasse | `if`/`elif`, logische Operatoren |
| 02 | [Mathespiel](02_mathespiel) | Drei Rechenaufgaben nacheinander, bei einem Fehler ist das Spiel vorbei | verschachtelte `if`, `while` |
| 03 | [Passwort-Eingabe](03_passwort_eingabe) | Anmeldung mit höchstens drei Versuchen und Sperre | `while`, `break`, Zähler |
| 04 | [Passwortgenerator](04_passwortgenerator) | Zufälliges Passwort erzeugen und auf Sicherheitsregeln prüfen | `while`, `for`, `random`, ASCII |
| 05 | [Teile sortieren](05_teile_sortieren) | Simuliert 1.000 Prüfungen von zwei Bauteilen und zählt defekte Teile | `random`, Zähler, Simulation |
| 06 | [Gehalt nach Betriebszugehörigkeit](06_gehalt_betriebszugehoerigkeit) | Grundgehalt nach Dienstjahren plus Umsatzprovision | `if`/`elif`, Typumwandlung |
| 07 | [Kreditkarten-Prüfziffer](07_kreditkarte_pruefziffer) | Prüfziffer nach dem Luhn-Algorithmus berechnen und prüfen | Strings, Indizes, Algorithmus |
| 08 | [Kinosaal-Auswertung](08_kinosaal_auswertung) | Belegung und Altersstruktur eines Kinosaals auswerten | 2D-Listen, verschachtelte Schleifen |
| 09 | [Lager eines chaotischen Supermarkts](09_supermarkt_lager) | Bestände summieren, Regale vergleichen, leere Plätze melden | 2D-Listen, `deepcopy`, List Comprehension |
| 10 | [Punktewertung im unfairen Wettbewerb](10_wettbewerb_punkte) | Punkte je Teilnehmer und Kategorie auswerten, Schwache aussortieren | 2D-Listen, `del`, `deepcopy` |
| 11 | [Arbeitszeiterfassung](11_arbeitszeiterfassung) | Monatsübersicht aus Stempelzeiten, nach einer IHK-Prüfungsaufgabe (Winter 2013) | Module, Funktionen, `calendar`, Dictionaries |
| 12 | [Wasserfahrzeuge (GUI)](12_wasserfahrzeuge_gui) | Schiff auswählen und Daten mit Bild anzeigen | Tkinter, Klassen, Fehlerbehandlung |
| 13 | [Eismaschine](13_eismaschine_oop) | Eine Maschine erzeugt Softeis-Objekte, direktes Erzeugen ist gesperrt | OOP, Assoziation, Exceptions |
| 14 | [Ticketautomat Schwimmbad](14_ticketautomat_schwimmbad) | Ticketverkauf mit Wechselgeld, Abo-Preis, Sauna-Zuschlag und Öffnungszeiten | OOP, Enums, Type Hints, **Unit-Tests** |
| 15 | [Blutalkohol](15_blutalkohol) | Blutalkohol nach der Widmark-Formel für mehrere Personen und Getränke | Funktionen, Dictionaries, f-Strings |
| 16 | [Weihnachtsbaum](16_weihnachtsbaum) | Zeichnet Bäume in wählbarer Größe auf der Konsole und führt ein Protokoll | Funktionen, `try`/`except`, Listen |
| 17 | [Länder und Hauptstädte](17_laender_hauptstaedte) | Länder aus einer Datei lesen, Hauptstädte abfragen und speichern | Dateien lesen/schreiben, Module |
| 18 | [Kleine Funktionen](18_kleine_funktionen) | Literumrechnung, LKW-Maut, Palindrom, perfekte Zahl, Lambdas | Funktionen, Lambdas, **Unit-Tests** |

### Ausführen

Python 3.10 oder neuer, keine weiteren Pakete nötig.

```bash
cd 14_ticketautomat_schwimmbad
python main.py                      # Programm starten
python -m unittest -v test_classes  # Tests ausführen
```

Die Tests laufen bei jedem Push automatisch mit GitHub Actions (siehe Badge oben).

---

<a name="english"></a>
## 🇬🇧 English

18 of my Python exercises from my retraining as an IT Specialist for Application Development (IBB, Hameln, Germany), written between March and September 2026. The order shows my learning path: from loops and conditions through lists and files to classes, GUI and unit tests.

I wrote these programs myself in class. For this publication I tidied them up and fixed a few bugs. Program output and variable names are in German.

| No. | Exercise | What it does | Focus |
|---|---|---|---|
| 01 | [Decision table](01_entscheidungstabelle) | Invoice total with a discount depending on order value and prepayment | `if`/`elif`, logical operators |
| 02 | [Maths game](02_mathespiel) | Three sums in a row; one mistake ends the game | nested `if`, `while` |
| 03 | [Login with attempts](03_passwort_eingabe) | Login with at most three attempts and lockout | `while`, `break`, counters |
| 04 | [Password generator](04_passwortgenerator) | Generates a random password and checks it against security rules | `while`, `for`, `random`, ASCII |
| 05 | [Sorting parts](05_teile_sortieren) | Simulates 1,000 inspections of two part types and counts defective ones | `random`, counters, simulation |
| 06 | [Salary by length of service](06_gehalt_betriebszugehoerigkeit) | Base salary by years of service plus sales commission | `if`/`elif`, type conversion |
| 07 | [Credit card check digit](07_kreditkarte_pruefziffer) | Calculates and checks the Luhn check digit | strings, indexing, algorithm |
| 08 | [Cinema analysis](08_kinosaal_auswertung) | Analyses seat occupancy and visitor ages | 2D lists, nested loops |
| 09 | [Chaotic supermarket warehouse](09_supermarkt_lager) | Sums stock, compares shelves, reports empty slots | 2D lists, `deepcopy`, list comprehension |
| 10 | [Scoring an unfair competition](10_wettbewerb_punkte) | Scores per participant and category, weak ones removed | 2D lists, `del`, `deepcopy` |
| 11 | [Time tracking](11_arbeitszeiterfassung) | Monthly report from clock-in data, based on a German IHK exam task (winter 2013) | modules, functions, `calendar`, dictionaries |
| 12 | [Watercraft (GUI)](12_wasserfahrzeuge_gui) | Select a ship and show its data and picture | Tkinter, classes, error handling |
| 13 | [Ice cream machine](13_eismaschine_oop) | A machine creates soft-serve objects; creating them directly is blocked | OOP, association, exceptions |
| 14 | [Swimming pool ticket machine](14_ticketautomat_schwimmbad) | Ticket sales with change, subscription price, sauna surcharge and opening hours | OOP, enums, type hints, **unit tests** |
| 15 | [Blood alcohol](15_blutalkohol) | Blood alcohol with the Widmark formula for several people and drinks | functions, dictionaries, f-strings |
| 16 | [Christmas tree](16_weihnachtsbaum) | Draws trees of any size on the console and keeps a log | functions, `try`/`except`, lists |
| 17 | [Countries and capitals](17_laender_hauptstaedte) | Reads countries from a file, asks for capitals and saves them | file I/O, modules |
| 18 | [Small functions](18_kleine_funktionen) | Litre conversion, truck toll, palindrome, perfect number, lambdas | functions, lambdas, **unit tests** |

### Running

Python 3.10 or newer, no extra packages needed.

```bash
cd 14_ticketautomat_schwimmbad
python main.py                      # run the program
python -m unittest -v test_classes  # run the tests
```

The tests run automatically on every push with GitHub Actions (see badge above).
