# Input (order value, prepayment)
# Python: input

# Conditional logic (rule-based logic)
# Python: if statement, logic

# Operators: +, -, *
# Logical operators: and, or, exclusive or

bestellwert = float(input("Bestellwert: "))
vorkasse = input("Vorkasse (j, n): ").strip().lower()  # j oder n

# Check rule 1
if bestellwert > 100 and vorkasse == "j":
    rabatt = bestellwert * 0.87
    print(f"Rechnungssumme: {rabatt:.2f} €")
    print("Du bekommst 13% Rabatt")

# Check rule 2
elif bestellwert > 100 and vorkasse =="n":
    rabatt = bestellwert * 0.90
    print(f"Rechnungssumme: {rabatt:.2f} €")
    print("Du bekommst 10 % Rabatt")

# Check rule 3
elif bestellwert <= 100 and vorkasse == "j":
    rabatt = bestellwert * 0.97
    print(f"Rechnungssumme: {rabatt:.2f} €")
    print("Du bekommst 3 % Rabatt")

# Check rule 4
elif bestellwert <= 100 and vorkasse == "n":
    print(f"Rechnungssumme: {bestellwert:.2f} €")
    print("Du bekommst keinen Rabatt")

# Ungültige Eingabe bei Vorkasse
else:
    print("Bitte bei Vorkasse nur j oder n eingeben.")
