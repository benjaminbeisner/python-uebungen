import calendar


# Function to display the table header containing employee ID, month, year, and column labels
def schreibeKopfzeile(mitarbeiter, monat_name, jahr):
    print(f"\nMitarbeiter: {mitarbeiter}          {monat_name} {jahr}\n")
    print("Tag \tKommen \tGehen \tAnwesenheit \tBemerkung")
    print("===============================================================")

# Function to print a formatted single daily log entry row
def schreibeZeile(tag, kommen, gehen, anwesenheit, bemerkung):
    print(f"{tag:02d} \t\t{kommen} \t{gehen} \t{anwesenheit} \t\t\t\t\t{bemerkung}")


# Function to print the table footer showing total monthly attendance hours
def schreibeFusszeile(gesamtzeit):
    print("===============================================================")
    print(f"Summe Anwesenheit: \t\t{berechneGesamtzeit(gesamtzeit)}")


# Function to calculate worked duration and total elapsed minutes between arrival and departure times
def berechneArbeitszeit(kommen, gehen):
    std_kommen, min_kommen = map(int, kommen.split(":"))
    std_gehen, min_gehen = map(int, gehen.split(":"))
    kommen_min = std_kommen * 60 + min_kommen
    gehen_min = std_gehen * 60 + min_gehen
    diff = gehen_min - kommen_min
    std = diff // 60
    min = diff % 60
    anwesenheit = (f"{std:02d}:{min:02d}")
    return anwesenheit, diff


# Function to convert total minutes from midnight into a formatted 'HH:MM' time string
def berechneUhrzeit(rohdaten, arbeitstag):
    minuten = rohdaten[arbeitstag][1]
    stunden = minuten // 60
    restMinuten = minuten % 60
    uhrzeit = (f"{stunden:02d}:{restMinuten:02d}")
    return uhrzeit

# Function to format accumulated working time in minutes into an 'HH:MM' string
def berechneGesamtzeit(gesamtzeit):
    minuten = gesamtzeit
    stunden = minuten // 60
    restMinuten = minuten % 60
    summe = (f"{stunden:02d}:{restMinuten:02d}")
    return summe