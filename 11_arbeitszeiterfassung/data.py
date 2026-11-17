import calendar

# Dictionary mapping employee IDs to their respective timestamp log lists [day, minutes_from_midnight]
daten_pool = {
12345: [[2, 480], [2, 1040], [3, 470], [6, 480], [6, 960], [7, 990], [8, 480], [8, 960], [30, 990]],
67890: [[2, 480], [2, 1040], [3, 470], [5,490], [5,960], [6, 480], [6, 960], [7, 990], [8, 480], [8, 960], [10,470], [10,990], [12,460], [12,990], [13,990], [15,480], [15,960], [17,480], [18,480], [18,970], [20,460], [21,490], [21,1000], [23,450], [23,1010], [26,480], [26,980], [30, 990]]
}

# Date setup constants
jahr = 2026
monat = 4
tag = 1

# Prompt for employee ID and dynamically fetch dataset properties based on user input
mitarbeiter = 0
while mitarbeiter not in daten_pool:
    eingabe = input(f"Geben Sie Ihre Mitarbeiter-Nummer ein {list(daten_pool)}: ")
    if eingabe.isdigit():
        mitarbeiter = int(eingabe)
stempeltag = len(daten_pool.get(mitarbeiter))
daten = len(daten_pool.get(mitarbeiter, [0]))

# Loop counters and state variables
arbeitstag = 0
arbeit = 0
gehen = 0
bemerkung = ""

# Month metadata and total days calculation
monat_name = calendar.month_name[monat]
tage = calendar.monthrange(jahr, monat)[1]

# Accumulator for total monthly worked time
gesamtzeit = 0