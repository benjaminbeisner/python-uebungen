# Import all required classes and enums from the external 'classes' module
from classes import *

# Function to execute the ticket machine simulation scenario
def run_simulation():
    print("\nStarten des Beispiel Szenarios")

    # Define initial cash inventory for the automatic machine {denomination: count}
    start_cash = {0.50: 10, 1.00: 10, 2.00: 10, 5.00: 5}
    # Instantiate the vending machine with ID 1 and starting cash
    automat = Automatic(number=1, cash=start_cash)
    print(f"Startzustand: {automat}")

    # Scenario 1: Customer 1 purchases a short-term pass + sauna (total 4.00) using a 5.00 coin
    print("\nKunde 1 kauft ein Kurzzeitticket für Eingangs-, Schwimm- und Kinderbereich inkl. Sauna")
    t1 = automat.sell(
        option=TicketOptions.short_term,
        money={5.00: 1},
        allowSauna=True,
        create_at=10,
        client=101
    )
    if t1: print(f"Erhaltenes Ticket: {t1}")

    # Scenario 2: Customer 2 is a subscriber purchasing a day pass + sauna using a 10.00 note
    print("\nKunde 2 ist Abonnent")
    t2 = automat.sell(
        option=TicketOptions.short_term,
        money={10.00: 1},
        allowSauna=True,
        hasSubscription=True,
        create_at=11,
        client=102
    )
    if t2: print(f"Erhaltenes Ticket: {t2}")

    # Scenario 3: Customer 3 attempts to buy a long-term pass (4.00) with insufficient funds (2.00)
    print("\nKunde 3 versucht 6-Stunden-Ticket (4.00 Banana Cash) mit zu wenig Geld zu kaufen")
    automat.sell(
        option=TicketOptions.long_term,
        money={2.00: 1},
        create_at=12,
        client=103
    )

    # Print final machine state showing updated cash inventory
    print(f"\nEndzustand: {automat}")
    print("Simulation beendet\n")

# Entry point guard to run simulation when script is executed directly
if __name__ == '__main__':
    run_simulation()