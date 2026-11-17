# Aufgabe 3: Zwei weitere Länder über das Terminal abfragen
#            und das Dictionary in eine neue Datei schreiben

def laender_per_dialog(dictionary, anzahl=2):
    for i in range(1, anzahl + 1):
        land = ""
        while not land:
            land = input(f"Land {i}: ").strip()

        hauptstadt = ""
        while not hauptstadt:
            hauptstadt = input(f"Hauptstadt von {land}: ").strip()

        dictionary[land] = hauptstadt
    return dictionary

def dictionary_in_datei_schreiben(dictionary, dateipfad):
    with open(dateipfad, "w", encoding="utf-8") as datei:
        for land, hauptstadt in dictionary.items():
            datei.write(f"{land} {hauptstadt}\n")