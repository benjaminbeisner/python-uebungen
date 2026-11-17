# Prompt user for years of service (as int) and monthly revenue (as float)
betriebszugehoerigkeit = int(input("Geben Sie die Jahre Ihrer Betriebszugehörigkeit ein: "))
monatsumsatz = float(input("Geben Sie Ihr Monatsumsatz ein: "))

# Calculate base salary based on years of service
if betriebszugehoerigkeit <= 5:
    gehalt = 1700
elif betriebszugehoerigkeit > 10:
    gehalt = 2700
else:
    gehalt = 2100

# Calculate bonus based on monthly revenue
if monatsumsatz <= 5000:
    gehaltszuschlag = monatsumsatz * 0.1
elif monatsumsatz > 10000:
    gehaltszuschlag = monatsumsatz * 0.23
else:
    gehaltszuschlag = monatsumsatz * 0.15

# Output calculated values
print(f"Gehalt: {gehalt:.2f} €")
print(f"Gehaltszuschlag: {gehaltszuschlag:.2f} €")
print(f"Auszahlungsbetrag: {gehalt + gehaltszuschlag:.2f} €")
