import os
import tkinter

# Bilder relativ zum Skript laden, egal aus welchem Ordner es gestartet wird
ORDNER = os.path.dirname(os.path.abspath(__file__))

# Function to close and destroy the GUI window
def ende():
    fenster.destroy()

# Function triggered by the "Ausgabe" button to display ship details and image
def ausgabe():
    # Retrieve the currently active/selected item from the listbox
    ausgewählter_name = liAuswahl.get("active")

    # Check if the selected name exists in the dictionary
    if ausgewählter_name in fahrzeuge_dict:
        schiff = fahrzeuge_dict[ausgewählter_name]

        # Format ship properties into a single display string using tabs and newlines
        info_text = (f"Name: \t\t{schiff.name}\n"f"Tiefgang: \t{schiff.tiefgang} cm\n"f"Breite: \t\t{schiff.breite} m\n"f"Länge: \t\t{schiff.laenge} m\n"f"Laufleistung: \t{schiff.laufleistung} sm\n"f"Baujahr: \t\t{schiff.baujahr}\n"f"Besitzer: \t\t{schiff.besitzer}")

        # Update the text label with the formatted information
        lbAusgabe["text"] = info_text

        # Try to load and display the image corresponding to the selected ship
        try:
            neues_bild = tkinter.PhotoImage(file=os.path.join(ORDNER, schiff.bild_pfad))
            lbBild["image"] = neues_bild
            lbBild.image = neues_bild  # Keep a reference to prevent garbage collection

        # Fallback if image file is missing or unreadable
        except tkinter.TclError:
            lbBild["image"] = ""
            lbBild["text"] = "[Bild nicht gefunden]"

# Class definition representing a watercraft object
class wasserfahrzeug:
    def __init__(self, name, tiefgang, breite, laenge, laufleistung, baujahr, besitzer, bild_pfad):
        self.name = name
        self.tiefgang = tiefgang
        self.breite = breite
        self.laenge = laenge
        self.laufleistung = laufleistung
        self.baujahr = baujahr
        self.besitzer = besitzer
        self.bild_pfad = bild_pfad

# Instantiate watercraft objects
wasserfahrzeug1 = wasserfahrzeug("Airwave", 150, 10, 25, 50000, 1930, "Maier", "Airwave.png")
wasserfahrzeug2 = wasserfahrzeug("Meeresluft", 125, 7, 10, 500000, 1980, "Müller", "Meeresluft.png")
wasserfahrzeug3 = wasserfahrzeug("Royal", 115, 8, 15, 2000, 2020, "Schulze", "Royal.png")

# Store instances in a dictionary using their names as keys
fahrzeuge_dict = {wasserfahrzeug1.name: wasserfahrzeug1, wasserfahrzeug2.name: wasserfahrzeug2, wasserfahrzeug3.name: wasserfahrzeug3}

# Main application window setup
fenster = tkinter.Tk()
fenster.title("Wasserfahrzeuge")
fenster.resizable(0, 0)  # Disable window resizing

# Label above the selection box
lbAuswahl = tkinter.Label(fenster, text="Wasserfahrzeug auswählen:")
lbAuswahl.grid(row=1, column=0, sticky="w", padx=5, pady=5)

# Frame container for Listbox and Scrollbar
frAuswahl = tkinter.Frame(fenster)
frAuswahl.grid(row=2, column=0, padx=5, pady=5)

# Create vertical scrollbar and link it to the listbox
sbAuswahl = tkinter.Scrollbar(frAuswahl, orient="vertical")
liAuswahl = tkinter.Listbox(frAuswahl, height=4, yscrollcommand=sbAuswahl.set)
sbAuswahl["command"] = liAuswahl.yview

# Populate Listbox dynamically from dictionary keys
for s in fahrzeuge_dict.keys():
    liAuswahl.insert("end", s)
liAuswahl.grid(row=0, column=0)
sbAuswahl.grid(row=0, column=1, sticky="sn")

# Button to trigger details output
buAusgabe = tkinter.Button(fenster, text="Ausgabe", command=ausgabe, width=10)
buAusgabe.grid(row=4, column=0, sticky="w", padx=5, pady=5)

# Label to output text details
lbAusgabe = tkinter.Label(fenster, text="(leer)", justify="left")
lbAusgabe.grid(row=5, column=0, sticky="nw", padx=5, pady=5)

# Label to hold and display the image
lbBild = tkinter.Label(fenster)
lbBild.grid(row=5, column=1, sticky="nw", padx=20, pady=5)

# Exit button to close the application
buEnde = tkinter.Button(fenster, text="Ende", command=ende, width=10)
buEnde.grid(row=8, column=2, padx=5, pady=5)

# Start the Tkinter event loop
fenster.mainloop()