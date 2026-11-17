# Kleines Rechenspiel mit verschachtelten if-Abfragen
nochmal = "ja"

while nochmal == "ja":
    # Input
    print("Seid ihr bereit? (ja/nein)")
    bereit = input()

    # Check rule 1
    if bereit == "nein":
        print("!!! GAME OVER !!!")

    else:
        # Task 1
        print("Aufgabe 1: 12 x 12 = ?")
        Antwort1 = input()

        # Check task 1
        if Antwort1 == "144":
            print("Richtig!")

            # Task 2
            print("Aufgabe 2: 108 / 9 = ?")
            Antwort2 = input()

            # Check task 2
            if Antwort2 == "12":
                print("Richtig!")

                # Task 3
                print("Aufgabe 3: 60 x 7 + 3 x 19 + 2 x 12 = ?")
                Antwort3 = input()

                # Check task 3
                if Antwort3 == "501":
                    print("ALLES RICHTIG!!! Glückwunsch :-D")

                # End Task 3
                else:
                    print("!!! GAME OVER !!!")

            # End Task 2
            else:
                print("!!! GAME OVER !!!")

        # End Task 1
        else:
            print("!!! GAME OVER !!!")

    # Noch eine Runde?
    print("Möchtet ihr nochmal anfangen? (ja/nein)")
    nochmal = input()

print("Programm beendet")
