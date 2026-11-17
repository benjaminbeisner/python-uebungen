# Initialize 2D list representing cinema seats (rows and seat ages; 0 = empty seat)
kinosaal = [
    [25, 34, 0, 18, 42],
    [0, 0, 51, 60, 33],
    [19, 22, 23, 0, 0],
    [45, 38, 0, 29, 31]
]

# Initialize variables and counters
sitzreihe = 0
belegte_sitze = 0
durchschnittsalter = 0
sitzplatzreihe0 = 0
sitzplatzreihe1 = 0
sitzplatzreihe2 = 0
sitzplatzreihe3 = 0

# Get grid dimensions (number of rows and seats per row)
anzahl_reihe = (len(kinosaal))
anzahl_sitze = (len(kinosaal[0]))

# Tasks 1 to 4: Iterate over each seat in every row
while sitzreihe < anzahl_reihe:
    sitzplatz = 0

    while sitzplatz < anzahl_sitze:
        # Check if the seat is occupied (age > 0)
        if kinosaal[sitzreihe][sitzplatz] > 0:
            belegte_sitze += 1

            # Task 3: Count occupied seats per specific row
            if sitzreihe == 0:
                sitzplatzreihe0 += 1
            if sitzreihe == 1:
                sitzplatzreihe1 += 1
            if sitzreihe == 2:
                sitzplatzreihe2 += 1
            if sitzreihe == 3:
                sitzplatzreihe3 += 1

            # Task 4: Find and print seats occupied by visitors under 21 years old
            if kinosaal[sitzreihe][sitzplatz] < 21:
                print("Aufgabe 4: Reihe:", sitzreihe + 1, "Platz:", sitzplatz + 1)

        # Accumulate total age for average calculation
        durchschnittsalter += kinosaal[sitzreihe][sitzplatz]
        sitzplatz += 1
    sitzreihe += 1

# Output results for Tasks 1 and 2
print("Aufgabe 1: Gesamtzahl der belegten Sitze:", belegte_sitze)
print(f"Aufgabe 2: Das Durchschnittsalter beträgt: {durchschnittsalter / belegte_sitze:.2f}")

# Task 3: Find and print the row(s) with the maximum number of occupied seats
max_wert = max(sitzplatzreihe0, sitzplatzreihe1, sitzplatzreihe2, sitzplatzreihe3)
if sitzplatzreihe0 == max_wert:
    print("Aufgabe 3: Reihe 1 hat die meisten belegten Sitze mit", sitzplatzreihe0, "belegten Sitzen")
if sitzplatzreihe1 == max_wert:
    print("Aufgabe 3: Reihe 2 hat die meisten belegten Sitze mit", sitzplatzreihe1, "belegten Sitzen")
if sitzplatzreihe2 == max_wert:
    print("Aufgabe 3: Reihe 3 hat die meisten belegten Sitze mit", sitzplatzreihe2, "belegten Sitzen")
if sitzplatzreihe3 == max_wert:
    print("Aufgabe 3: Reihe 4 hat die meisten belegten Sitze mit", sitzplatzreihe3, "belegten Sitzen")