import random

# Schleife: so lange neue Passwörter erzeugen, bis eines gültig ist
# oder der Benutzer abbricht
passwort_gueltig = False

while not passwort_gueltig:
    # Prüf-Flags für jedes neue Passwort zurücksetzen
    gross = False
    klein = False
    zahl = False
    sonderzeichen = False

    # 8 zufällige druckbare ASCII-Zeichen (33 bis 126) aneinanderhängen
    passwort = ""
    passwort_index = 0
    while passwort_index < 8:
        zufallszahl = random.randint(33, 126)
        passwort = passwort + chr(zufallszahl)
        passwort_index = passwort_index + 1

    # Prüfen, welche Zeichenarten vorkommen
    for zeichen in passwort:
        if zeichen.isupper():
            gross = True
        elif zeichen.islower():
            klein = True
        elif zeichen.isdigit():
            zahl = True
        else:
            sonderzeichen = True

    print("Passwort: ", passwort)

    # Gültig nur mit Groß- und Kleinbuchstabe, Zahl und Sonderzeichen
    if gross and klein and zahl and sonderzeichen:
        passwort_gueltig = True
        print("Passwort gültig")
    else:
        print("Passwort nicht gültig")
        neues_passwort = input("Neues Passwort generieren (j/n): ")
        if neues_passwort != "j":
            break
