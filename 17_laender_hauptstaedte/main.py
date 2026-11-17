import os

from aufgabe1 import datei_einlesen, laender_ausgeben
from aufgabe2 import hauptstaedte_abfragen, dictionary_ausgeben
from aufgabe3 import laender_per_dialog, dictionary_in_datei_schreiben

ORDNER = os.path.dirname(os.path.abspath(__file__))
EINGABE_DATEI = os.path.join(ORDNER, "laender.txt")
AUSGABE_DATEI = os.path.join(ORDNER, "laender_hauptstaedte.txt")

def main():
    # Aufgabe 1
    print("--- Aufgabe 1: Inhalt der Datei ---")
    try:
        laender = datei_einlesen(EINGABE_DATEI)
    except FileNotFoundError:
        print(f"Datei nicht gefunden: {EINGABE_DATEI}")
        return
    laender_ausgeben(laender)

    # Aufgabe 2
    print("\n--- Aufgabe 2: Hauptstädte eingeben ---")
    dictionary = hauptstaedte_abfragen(laender)
    print("\nProtokoll:")
    dictionary_ausgeben(dictionary)

    # Aufgabe 3
    print("\n--- Aufgabe 3: Zwei weitere Länder eingeben ---")
    dictionary = laender_per_dialog(dictionary)
    dictionary_in_datei_schreiben(dictionary, AUSGABE_DATEI)
    print("Aktuelles Dictionary:")
    dictionary_ausgeben(dictionary)
    print(f"\nGespeichert in: {AUSGABE_DATEI}")

if __name__ == "__main__":
    main()