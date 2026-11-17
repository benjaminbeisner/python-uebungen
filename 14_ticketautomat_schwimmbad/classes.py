from __future__ import annotations
import random
from typing import Dict, Tuple, Optional
from enum import Enum
from datetime import datetime


# Enum defining available ticket types with duration (hours) and base price
class TicketOptions(Enum):
    short_term = (3, 2.50)
    long_term = (6, 4.00)
    day_pass = (14, 5.00)

    def __init__(self, duration_hours: int, price: float):
        self.duration_hours = duration_hours
        self.price = price

# Enum defining operational hours
class WorkingHours(Enum):
    opening = 8
    closing = 22


# Class representing the ticket vending machine (Automatic)
class Automatic():
    def __init__(self, number: int, cash: Dict[float, int]):
        self._serial: list = []                  # List storing created/sold Ticket instances
        self._number: int = number                # Machine identifier ID
        self._cash: Dict[float, int] = cash      # Internal cash inventory {denomination: count}

    # Calculates and dispenses change using available cash inventory
    def give_change(self, price: float, money: float) -> Tuple[bool, float]:
        if money < price:
            return False, 0.0
        change_needed = round(money - price, 2)
        total_change = change_needed

        # Greedy algorithm: deduct highest available denominations first
        for denom in sorted(self._cash.keys(), reverse=True):
            while change_needed >= denom and self._cash[denom] > 0:
                change_needed = round(change_needed - denom, 2)
                self._cash[denom] -= 1

        return True, total_change

    # Handles ticket sales, payment verification, cash inventory management, and ticket creation
    def sell(self, option: TicketOptions, money: Dict[float, int], hasSubscription: bool = False, create_at: int = 8,
             allowSauna: bool = False, client: Optional[int] = None) -> Optional[Ticket]:

        # Select ticket option and determine pricing based on subscription status
        selected_option = TicketOptions.day_pass if hasSubscription else option
        total_given = sum(denom * count for denom, count in money.items())
        base_price = 5.00 if hasSubscription else selected_option.price
        required_price = base_price + (1.50 if allowSauna else 0.0)

        # Temporarily accept inserted cash into inventory
        for denom, count in money.items():
            self._cash[denom] = self._cash.get(denom, 0) + count

        # Attempt to give change
        success, change = self.give_change(required_price, total_given)

        # Roll back cash transaction if payment/change processing fails
        if not success:
            for denom, count in money.items():
                self._cash[denom] -= count
            print(
                f"Fehler: unzureichende Zahlung! Gegeben: {total_given:.2f} Banana-Cash, Benötigt: {required_price:.2f} Banana-Cash")
            return None

        # Instantiate ticket object upon successful purchase
        ticket = Ticket(
            ticket_type=selected_option,
            created_at=create_at,
            allows_sauna=allowSauna,
            automatic=self._number,
            client=client
        )

        # Record ticket to sales history and trigger log output
        self._serial.append(ticket)
        ticket.log_ticket()

        print(f"Verkauf erfolgreich! Wechselgeld: {change:.2f} Banana-Cash")
        return ticket

    # Returns current cash dictionary
    def get_cash(self) -> Dict[float, int]:
        return self._cash

    # Calculates and returns total cash value inside the machine
    def report_cash(self) -> float:
        total = sum(denom * count for denom, count in self._cash.items())
        return round(total, 2)

    # String representation of the automatic machine state
    def __str__(self) -> str:
        return f"Automat ID: {self._number} | Aktueller Kassenbestand: {self.report_cash():.2f} Banana-Cash"

# Class representing individual tickets
class Ticket():
    _counter = 1000  # Class attribute used to generate incremental ticket numbers

    def __init__(self, ticket_type: Optional[TicketOptions] = None, created_at: int =0, allows_sauna: bool = False, automatic: Optional[int] = None, client: Optional[int] = None):

        Ticket._counter += 1
        self._ticket_number: int = Ticket._counter
        self._ticket_type: str = ticket_type.name if ticket_type else "Custom"
        self._ticket_code: int = random.randint(100000, 999999)
        self._description: str = "Zugang: Kinder, Schwimmbad" + (", Sauna" if allows_sauna else "")
        base_price = ticket_type.price if ticket_type else 0.0
        self._price: float = base_price + (1.50 if allows_sauna else 0.0)
        self._sauna: bool = allows_sauna
        self._created_at: datetime = datetime.now()
        self._start_hour: int = created_at
        # Calculate validity deadline capped at 22:00 closing time
        duration = ticket_type.duration_hours if ticket_type else 0
        self._deadline: int = min(created_at + duration, WorkingHours.closing.value)
        self._automatic: Optional[int] = automatic
        self._client: Optional[int] = client

    # Setter method for assigning machine ID
    def set_automatic(self, n: int) -> None:
        self._automatic = n

    # Recalculates deadline based on ticket type duration
    def set_deadline(self) -> None:
        if self._ticket_type in TicketOptions.__members__:
            duration = TicketOptions[self._ticket_type].duration_hours
            self._deadline = min(self._start_hour + duration, WorkingHours.closing.value)

    # Upgrades ticket to include sauna access
    def include_sauna(self) -> None:
        if not self._sauna:
            self._sauna = True
            self._price +=1.50
            self._description += ", Sauna"

    # Prints timestamp and generated ticket number
    def log_ticket(self) -> None:
        print(datetime.now().strftime("%H:%M:%S %d.%m.%Y"))
        print(f"Ticket-Nummer: #{self._ticket_number}")

    # Formats ticket attributes into a readable summary report
    def report(self) -> str:
        return (f"Ticket #{self._ticket_number} [{self._ticket_type}] | "
                f"Kunde: {self._client or "Anonym"} | Preis: {self._price:.2f} Banana-Cash | "
                f"Sauna: {"ja" if self._sauna else "nein"} | gültig bis: {self._deadline}:00 Uhr")

    # String representation of a Ticket object
    def __str__(self) -> str:
        return self.report()
