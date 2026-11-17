def zeichne_weihnachtsbaum(hoehe, breite):
    print()
    for i in range(hoehe):
        sterne_anzahl = 2 * i + 1
        sterne = "*" * sterne_anzahl
        print(sterne.center(breite))

    stamm = "I"
    print(stamm.center(breite))
    print()

def main():
    baeume = []  # speichert (hoehe, breite) jedes gezeichneten Baums

    while True:
        try:
            hoehe = int(input("Bitte geben Sie die Höhe des Baumes ein (z.B. 5): "))
            breite = int(input("Bitte geben Sie die Breite des Baumes ein (z.B. 20): "))
        except ValueError:
            print("Ungültige Eingabe! Bitte geben Sie ganze Zahlen ein.")
            continue

        if hoehe < 1 or breite < 1:
            print("Höhe und Breite müssen größer als 0 sein.")
            continue

        zeichne_weihnachtsbaum(hoehe, breite)
        baeume.append((hoehe, breite))

        weiter = input("Möchten Sie einen weiteren Baum zeichnen? (j/n): ").strip().lower()
        if weiter != 'j':
            break

    print("-" * 40)
    print(f"Protokoll: Es wurde(n) insgesamt {len(baeume)} Weihnachtsbaum/Bäume auf der Konsole ausgegeben.")
    for nummer, (hoehe, breite) in enumerate(baeume, start=1):
        print(f"  Baum {nummer}: Höhe {hoehe}, Breite {breite}")
    print("-" * 40)

if __name__ == "__main__":
    main()