import unittest
from classes import Automatic, TicketOptions, Ticket

# Test suite class for verifying the functionality of the Automatic ticket machine system
class TestAutomaticSystem(unittest.TestCase):

    # Setup fixture executed before each individual test method to ensure a clean test environment
    def setUp(self):
        """Executed before every single test to establish a fresh environment."""
        self.start_cash = {0.50: 10, 1.00: 10, 2.00: 10, 5.00: 5, 10.00: 2}
        self.automat = Automatic(number=1, cash=self.start_cash.copy())

    # Verifies initial cash sum calculation
    def test_kassenbestand_initialisierung(self):
        """Tests whether the initial cash inventory is calculated correctly."""
        # 10x0.50 + 10x1.00 + 10x2.00 + 5x5.00 + 2x10.00 = 5.0 + 10.0 + 20.0 + 25.0 + 20.0 = 80.0
        self.assertEqual(self.automat.report_cash(), 80.0)

    # Tests purchasing a short-term pass (2.50) with exact payment (no change)
    def test_erfolgreicher_kauf_exakt_bezahlt(self):
        """Purchase of a short-term pass (2.50) with exact payment and no change."""
        ticket = self.automat.sell(
            option=TicketOptions.short_term,
            money={2.00: 1, 0.50: 1}, # Exact payment of 2.50
            allowSauna=False,
            create_at=10,
            client=101
        )
        self.assertIsNotNone(ticket)
        self.assertIsInstance(ticket, Ticket)
        # Total cash must increase by exactly 2.50
        self.assertEqual(self.automat.report_cash(), 82.50)

    # Tests ticket purchase requiring change calculation and dispensation
    def test_erfolgreicher_kauf_mit_wechselgeld(self):
        """Purchase including sauna (2.50 + 1.50 = 4.00) with a 5.00 note -> 1.00 change."""
        initial_cash = self.automat.report_cash()
        ticket = self.automat.sell(
            option=TicketOptions.short_term,
            money={5.00: 1},
            allowSauna=True,
            create_at=10
        )
        self.assertIsNotNone(ticket)
        # Net increase in cash inventory must be 4.00 (+5.00 inserted, -1.00 change given)
        self.assertEqual(self.automat.report_cash(), initial_cash + 4.00)

    # Tests subscriber override logic (automatically upgrade to day pass)
    def test_kauf_abonnent_upgrade(self):
        """Subscribers automatically receive a day pass (5.00) at subscriber base price."""
        ticket = self.automat.sell(
            option=TicketOptions.short_term, # Overridden to day_pass by subscription status
            money={10.00: 1},
            hasSubscription=True,
            allowSauna=True, # 5.00 (Subscriber) + 1.50 (Sauna) = 6.50
            create_at=9
        )
        self.assertIsNotNone(ticket)
        self.assertEqual(ticket._ticket_type, TicketOptions.day_pass.name)
        self.assertEqual(ticket._price, 6.50)

    # Tests transaction rejection when payment provided is insufficient
    def test_fehlgeschlagener_kauf_zu_wenig_geld(self):
        """Attempt to buy a 6-hour pass (4.00) with only 2.00 provided."""
        initial_cash = self.automat.report_cash()
        ticket = self.automat.sell(
            option=TicketOptions.long_term,
            money={2.00: 1},
            create_at=12,
            client=103
        )
        # Transaction must be rejected
        self.assertIsNone(ticket)
        # Cash inventory must remain unchanged (inserted money is refunded)
        self.assertEqual(self.automat.report_cash(), initial_cash)

    # Verifies ticket validity deadline calculation and 22:00 closing time cap
    def test_ticket_deadline_berechnung(self):
        """Tests whether ticket deadline validity is calculated correctly and capped at 22:00."""
        # Standard case: Start at 10:00 + 3h duration = 13:00
        ticket_normal = Ticket(ticket_type=TicketOptions.short_term, created_at=10)
        self.assertEqual(ticket_normal._deadline, 13)

        # Capped case: Start at 18:00 + 6h (long_term) would be 24:00 -> MUST be capped at 22:00
        ticket_capped = Ticket(ticket_type=TicketOptions.long_term, created_at=18)
        self.assertEqual(ticket_capped._deadline, 22)


# Script entry point execution guard for unittest runner
if __name__ == '__main__':
    unittest.main()