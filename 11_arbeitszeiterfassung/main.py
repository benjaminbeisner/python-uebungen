from functions import *
from data import *


schreibeKopfzeile(mitarbeiter, monat_name, jahr)

while tag <= tage:
    anwesenheit = ""
    kommen = "\t"
    gehen = ""
    bemerkung = ""


    if arbeitstag < stempeltag and daten_pool.get(mitarbeiter)[arbeitstag][0] == tag:
        kommen = berechneUhrzeit(daten_pool.get(mitarbeiter), arbeitstag)
        arbeitstag += 1

        if arbeitstag < stempeltag and daten_pool.get(mitarbeiter)[arbeitstag][0] == tag:
            gehen = berechneUhrzeit(daten_pool.get(mitarbeiter), arbeitstag)
            anwesenheit, diff = berechneArbeitszeit(kommen, gehen)
            schreibeZeile(tag, kommen, gehen, anwesenheit, bemerkung)
            gesamtzeit += diff
            arbeitstag += 1

        else:
            bemerkung = "eine Buchung fehlt"
            schreibeZeile(tag, kommen, gehen, anwesenheit, bemerkung)

    else:
        bemerkung = "nicht anwesend"
        schreibeZeile(tag, kommen, gehen, anwesenheit, bemerkung)
    tag += 1

schreibeFusszeile(gesamtzeit)