import copy

# Initialize warehouse structure (3 shelves / rows, each with 4 product slots)
lager = [ [12, 4, 7, 0], [3, 15, 0, 9], [0, 2, 1, 8] ]

# Counters and initial variables
regal = 0
gesamtanzahl = 0
produktreihe0 = 0
produktreihe1 = 0
produktreihe2 = 0

# Get grid dimensions
anzahl_produkt = (len(lager[0]))
anzahl_regale = (len(lager))

# Create a deep copy of the warehouse array for Task 3.1
lagerNeu = copy.deepcopy(lager)

# Main loop: Iterate through each shelf (row)
while regal < anzahl_regale:
    produkt = 0

    # Task 3.1: Replace any stock quantity less than 5 with 0 in the deep copy (using list comprehension)
    lagerNeu[regal] = [0 if z < 5 else z for z in lagerNeu[regal]]

    # Inner loop: Iterate through each product slot in the current shelf
    while produkt < anzahl_produkt:
        # Task 1: Add up total products in the warehouse
        gesamtanzahl += (lager[regal][produkt])

        # Task 2: Sum products for each individual shelf
        if regal == 0:
            produktreihe0 += (lager[regal][produkt])
        if regal == 1:
            produktreihe1 += (lager[regal][produkt])
        if regal == 2:
            produktreihe2 += (lager[regal][produkt])

        # Task 3.2: Modify the original list — set low stock (< 5) to 0 in-place
        if lager[regal][produkt] < 5:
            lager[regal][produkt] = 0

        # Task 4: Report empty slots (quantities equal to 0 after low-stock cleanup)
        if lager[regal][produkt] == 0:
            print("Aufgabe 4: In Regal", regal + 1, "auf Produktplatz", produkt + 1, "ist kein Produkt")

        produkt += 1
    regal += 1

# Output Task 1 result
print("Aufgabe 1: Die Gesamtanzahl der Produkte in den Regalen beträgt: ", gesamtanzahl)

# Output Task 2 results (find and display shelf/shelves with maximum products)
max_wert = max(produktreihe0, produktreihe1, produktreihe2)
if produktreihe0 == max_wert:
    print("Aufgabe 2: Regal 1 hat die meisten Produkte mit", produktreihe0, "Produkten")
if produktreihe1 == max_wert:
    print("Aufgabe 2: Regal 2 hat die meisten Produkte mit", produktreihe1, "Produkten")
if produktreihe2 == max_wert:
    print("Aufgabe 2: Regal 3 hat die meisten Produkte mit", produktreihe2, "Produkten")

# Output Task 3 results
print("Aufgabe 3.1:", lagerNeu)
print("Aufgabe 3.2:", lager)