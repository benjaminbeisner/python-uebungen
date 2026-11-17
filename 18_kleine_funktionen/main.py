from aufgaben import liter_umwandeln, lkw_maut, palindrom, perfekte_zahl, quadrieren, verketten

# Beispielwerte
for wert in (1.0, 0.42, 0.023, 0.0001):
    print(f"{wert} -> {liter_umwandeln(wert)}")

for klasse, achsen, km in (('A', 2, 13), ('D', 5, 13), ('X', 2, 13)):
    maut = lkw_maut(klasse, achsen, km)
    if maut is None:
        print(f"Schadstoffklasse {klasse}: ungültig")
    else:
        print(f"Schadstoffklasse {klasse}, {achsen} Achsen, {km} km: {maut:.1f} Eurocent")

print("OTTO ist ein Palindrom:", palindrom("OTTO"))
print("Hallo ist ein Palindrom:", palindrom("Hallo"))

for zahl in (6, 28, 10):
    print(f"Ist {zahl} eine perfekte Zahl? {perfekte_zahl(zahl)}")

print("5 zum Quadrat:", quadrieren(5))
print(verketten("Hans", "Maier"))
