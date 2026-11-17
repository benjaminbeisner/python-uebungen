# Aufgabe 1: Datei einlesen und auf der Konsole ausgeben

def datei_einlesen(dateipfad):
    laender = []
    with open(dateipfad, "r", encoding="utf-8") as datei:
        for zeile in datei:
            land = zeile.strip()
            if land:
                laender.append(land)
    return laender

def laender_ausgeben(laender):
    for land in laender:
        print(land)