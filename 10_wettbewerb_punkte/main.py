import copy

# Initialize 2D list representing participants and their score categories
punkte = [[8,7,9,6], [5,6,5,4], [9,9,10,8], [3,4,2,5]]

# Create a deep copy of the original points list for modification in Task 4
punkte_neu = copy.deepcopy(punkte)

# Initialize total score variables per participant
teilnehmer0 = 0
teilnehmer1 = 0
teilnehmer2 = 0
teilnehmer3 = 0
teilnehmer = 0

# Initialize total score variables per category
kategorie0 = 0
kategorie1 = 0
kategorie2 = 0
kategorie3 = 0

# Get grid dimensions
anzahl_teilnehmer = (len(punkte))
anzahl_kategorie = (len(punkte[0]))

# Task 1: Calculate total scores for each participant
while teilnehmer < anzahl_teilnehmer:
    kategorie = 0
    while kategorie < anzahl_kategorie:
        if teilnehmer == 0:
            teilnehmer0 += punkte[teilnehmer][kategorie]
        if teilnehmer == 1:
            teilnehmer1 += punkte[teilnehmer][kategorie]
        if teilnehmer == 2:
            teilnehmer2 += punkte[teilnehmer][kategorie]
        if teilnehmer == 3:
            teilnehmer3 += punkte[teilnehmer][kategorie]
        kategorie += 1
    teilnehmer += 1

# Output Task 1 results
print("Aufgabe 1: Gesamtpunktzahl von Teilnehmer 1: ",teilnehmer0)
print("Aufgabe 1: Gesamtpunktzahl von Teilnehmer 2: ",teilnehmer1)
print("Aufgabe 1: Gesamtpunktzahl von Teilnehmer 3: ",teilnehmer2)
print("Aufgabe 1: Gesamtpunktzahl von Teilnehmer 4: ",teilnehmer3)

# Task 2: Determine and print participant(s) with the highest total score
max_wert = max(teilnehmer0,teilnehmer1,teilnehmer2,teilnehmer3)
if teilnehmer0 == max_wert:
    print("Aufgabe 2: Teilnehmer 1 hat die meisten Punkte mit", teilnehmer0, "Punkten")
if teilnehmer1 == max_wert:
    print("Aufgabe 2: Teilnehmer 2 hat die meisten Punkte mit", teilnehmer1, "Punkten")
if teilnehmer2 == max_wert:
    print("Aufgabe 2: Teilnehmer 3 hat die meisten Punkte mit", teilnehmer2, "Punkten")
if teilnehmer3 == max_wert:
    print("Aufgabe 2: Teilnehmer 4 hat die meisten Punkte mit", teilnehmer3, "Punkten")

# Task 3: Calculate sum of scores per category across all participants
kategorie = 0
while kategorie < anzahl_kategorie:
    teilnehmer = 0
    while teilnehmer < anzahl_teilnehmer:
        if kategorie == 0:
            kategorie0 += punkte[teilnehmer][kategorie]
        if kategorie == 1:
            kategorie1 += punkte[teilnehmer][kategorie]
        if kategorie == 2:
            kategorie2 += punkte[teilnehmer][kategorie]
        if kategorie == 3:
            kategorie3 += punkte[teilnehmer][kategorie]
        teilnehmer += 1
    kategorie += 1

# Output Task 3 results (average score per category)
print("Aufgabe 3: Durchschnittliche Punktzahl der Kategorie 1: ", kategorie0 / anzahl_teilnehmer)
print("Aufgabe 3: Durchschnittliche Punktzahl der Kategorie 2: ", kategorie1 / anzahl_teilnehmer)
print("Aufgabe 3: Durchschnittliche Punktzahl der Kategorie 3: ", kategorie2 / anzahl_teilnehmer)
print("Aufgabe 3: Durchschnittliche Punktzahl der Kategorie 4: ", kategorie3 / anzahl_teilnehmer)

# Task 4: Remove participants with total scores under 25 from the copied list
# NOTE: Deletions are intentionally performed in reverse index order (3 -> 0)
# to avoid index displacement issues when deleting list elements
if teilnehmer3 < 25:
    del punkte_neu[3]
if teilnehmer2 < 25:
    del punkte_neu[2]
if teilnehmer1 < 25:
    del punkte_neu[1]
if teilnehmer0 < 25:
    del punkte_neu[0]

# Output Task 4 result
print("Aufgabe 4: neue Liste: ", punkte_neu)
