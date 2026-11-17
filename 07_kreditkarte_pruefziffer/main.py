# Prüfziffer einer 16-stelligen Kreditkartennummer prüfen (Luhn-Algorithmus)

kred_nr = input("16-stellige Kreditkartennummer (Enter = Beispiel): ").replace(" ", "")
if kred_nr == "":
    kred_nr = "9342571866701996"

if len(kred_nr) != 16 or not kred_nr.isdigit():
    print("Bitte genau 16 Ziffern eingeben.")
else:
    pruef_nr = int(kred_nr[-1])  # letzte Ziffer = Prüfziffer
    faktor = 2
    summe = 0

    # 1. Schleife: jede zweite Ziffer von rechts (ohne Prüfziffer) verdoppeln.
    # Ist das Ergebnis größer als 9, wird 9 abgezogen (entspricht der Quersumme).
    index = 14
    while index >= 0:
        ergebnis = int(kred_nr[index]) * faktor
        if ergebnis > 9:
            ergebnis -= 9
        summe += ergebnis
        index -= 2

    # 2. Schleife: die übrigen Ziffern unverändert addieren
    index = 13
    while index >= 1:
        summe += int(kred_nr[index])
        index -= 2

    # Die Prüfziffer ergänzt die Summe zum nächsten Vielfachen von 10
    erwartet = (10 - summe % 10) % 10

    print("Summe ohne Prüfziffer:", summe)
    print("Erwartete Prüfziffer:", erwartet, "| tatsächliche Prüfziffer:", pruef_nr)
    if erwartet == pruef_nr:
        print("Die Kreditkartennummer ist gültig.")
    else:
        print("Die Kreditkartennummer ist ungültig.")
