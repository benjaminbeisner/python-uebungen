# Assoziation: Eine EisMaschine erzeugt Softeis-Objekte

import random

Eissorten = ["Schokolade", "Vanille", "Erdbeere", "Zitrone", "Pistazie"]
Eisgroessen = ["klein", "mittel", "groß", "gigantisch"]
Eismaschinen = ["Froster7000", "Froster6000", "IceMaker6.0"]

class EisMaschine():
    # Konstruktor mit einem Attribut: Name der Maschine
    def __init__(self, name):
        self.name = name

    # Geheimes Kennwort: nur die Maschine darf Softeis erzeugen
    _produktions_kennwort = object()

    def produziere(self, sorte, groesse, Softeis_Anzahl):
        return Softeis(sorte, groesse, self.name, EisMaschine._produktions_kennwort) # erzeugt ein Softeis und gibt es als Objekt zurück

class Softeis():
    # Konstruktor: ohne gültiges Kennwort wird ein Fehler ausgelöst
    def __init__(self, sorte, groesse, EisMaschine_name, kennwort = None):
        if kennwort != EisMaschine._produktions_kennwort:
            raise PermissionError(
                "Ein Softeis kann nicht direkt hergestellt werden! \n"
                "Bitte nutze eine EisMaschine und die Methode .produziere()"
                )

        self.sorte = sorte
        self.groesse = groesse
        self.EisMaschine_name = EisMaschine_name

Softeis_Anzahl = 1

Anzahl_Softeis = int(input("Wieviele Eis möchtest Du haben? "))

while Softeis_Anzahl <= Anzahl_Softeis:
    zufall_EisMaschine = EisMaschine(random.choice(Eismaschinen))
    zufall_sorte = random.choice(Eissorten)
    zufall_groesse = random.choice(Eisgroessen)
    Eis = zufall_EisMaschine.produziere(zufall_sorte, zufall_groesse, Softeis_Anzahl)
    print(f"Das {Softeis_Anzahl}. Softeis ist {Eis.groesse} und hat die Geschmacksrichtung {Eis.sorte}. Hergestellt wurde es von: {Eis.EisMaschine_name}")
    Softeis_Anzahl += 1
