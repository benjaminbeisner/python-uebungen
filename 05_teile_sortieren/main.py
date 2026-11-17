import random

# Initialize counters for parts, defective parts, and storage box damage
anzahlTeil1 = 0
anzahlTeil2 = 0
anzahldefektTeil1 = 0
anzahldefektTeil2 = 0
lagerungsboxSchaden = 0
i = 0

# Loop to simulate 1,000 part inspections
while i < 1000:
    # Randomly simulate condition scans (True = intact, False = defective)
    scanZustandTeil1 = random.choice([True, False])
    scanZustandTeil2 = random.choice([True, False])

    # Randomly select part type (1 for Part 1, 0 for Part 2)
    scanTeileID = random.randint(0, 1)
    teileID = scanTeileID

    # Process Part 1
    if teileID == 1:
        anzahlTeil1 = anzahlTeil1 + 1
        # Check if Part 1 is defective
        if scanZustandTeil1 == False:
            lagerungsboxSchaden = lagerungsboxSchaden + 1
            anzahldefektTeil1 = anzahldefektTeil1 + 1

    # Process Part 2
    else:
        anzahlTeil2 = anzahlTeil2 + 1
        # Check if Part 2 is defective
        if scanZustandTeil2 == False:
            lagerungsboxSchaden = lagerungsboxSchaden + 1
            anzahldefektTeil2 = anzahldefektTeil2 + 1

    # Increment loop counter
    i = i + 1

# Output final statistics for Part 1
print("Gesamtanzahl Teile1: ", anzahlTeil1)
print("Gesamtanzahl schadhafte Teile1: ", anzahldefektTeil1)

# Output final statistics for Part 2
print("Gesamtanzahl Teile2: ", anzahlTeil2)
print("Gesamtanzahl schadhafte Teile2: ", anzahldefektTeil2)