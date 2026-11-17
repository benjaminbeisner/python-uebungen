# Set up correct login credentials
benutzername_korrekt = "admin"
passwort_korrekt = "123"

# Initialize attempt counters and status flag
falscheingabe = 0
max_versuche = 3
eingeloggt = False

# Loop until maximum attempts are reached or successful login occurs
while falscheingabe < max_versuche:
    # Prompt user for credentials
    eingabe_benutzername = input("Benutzername: ")
    eingabe_passwort = input("Passwort: ")

    # Check if input credentials match the correct ones
    if eingabe_benutzername == benutzername_korrekt and eingabe_passwort == passwort_korrekt:
        print("Eingabe korrekt. Herzlich Willkommen")
        eingeloggt = True
        break  # Exit the loop on successful login

    # If credentials are wrong, increment counter and display remaining attempts
    else:
        falscheingabe += 1
        verbleibend = max_versuche - falscheingabe
        print(f"falsche Eingabe! Verbleibende Versuche: {verbleibend}\n")

# Display lockout message if login was unsuccessful after max attempts
if not eingeloggt:
    print("Account für 24 Stunden gesperrt !!!")
