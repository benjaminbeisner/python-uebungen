# Aufgabe 2: Hauptstädte über die Konsole abfragen und im Dictionary speichern

def hauptstaedte_abfragen(laender):
    dictionary = {}
    for land in laender:
        hauptstadt = input(f"Hauptstadt von {land}: ").strip()
        dictionary[land] = hauptstadt
    return dictionary

def dictionary_ausgeben(dictionary):
    for land, hauptstadt in dictionary.items():
        print(f"{land} {hauptstadt}")