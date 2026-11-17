# Kleine Funktionsaufgaben vom 16.09.2026


def liter_umwandeln(liter):
    """Gibt eine Literangabe in l, cl oder ml zurück."""
    if liter >= 1.0:
        return f"{liter:g} l"
    elif liter >= 0.1:
        return f"{round(liter * 100, 2):g} cl"
    elif liter >= 0.001:
        return f"{round(liter * 1000, 2):g} ml"
    else:
        return "Wert zu klein"


def lkw_maut(schadstoffklasse, achsen, kilometer):
    """Berechnet die LKW-Maut in Eurocent oder gibt None bei ungültiger Klasse zurück."""
    # Tarife in Eurocent pro km: (bis 3 Achsen, ab 4 Achsen)
    tarife = {
        'A': (12.50, 13.10),
        'B': (14.60, 15.20),
        'C': (15.70, 16.30),
        'D': (18.80, 19.40),
        'E': (19.80, 20.40),
        'F': (20.80, 21.40)
    }
    if schadstoffklasse not in tarife:
        return None

    # Tarif-Index: 0 für bis 3 Achsen, 1 für ab 4 Achsen
    tarif_index = 0 if achsen <= 3 else 1
    return tarife[schadstoffklasse][tarif_index] * kilometer


def palindrom(text):
    """Prüft, ob ein Text vorwärts und rückwärts gleich ist (ohne Groß-/Kleinschreibung)."""
    text = text.upper()
    return text == text[::-1]


def perfekte_zahl(zahl):
    """Prüft, ob die Summe der echten Teiler gleich der Zahl ist."""
    if zahl < 2:
        return False
    teiler_summe = sum(i for i in range(1, zahl) if zahl % i == 0)
    return teiler_summe == zahl


# Lambda-Funktionen
quadrieren = lambda x: x ** 2

verketten = lambda vorname, nachname: (
    f"{'*' * len(vorname + ' ' + nachname)}\n"
    f"{vorname} {nachname}\n"
    f"{'*' * len(vorname + ' ' + nachname)}"
)
