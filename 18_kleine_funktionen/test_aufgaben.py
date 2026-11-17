import unittest
from aufgaben import liter_umwandeln, lkw_maut, palindrom, perfekte_zahl, quadrieren, verketten


class TestAufgaben(unittest.TestCase):

    def test_liter_umwandeln(self):
        self.assertEqual(liter_umwandeln(1.0), "1 l")
        self.assertEqual(liter_umwandeln(0.42), "42 cl")
        self.assertEqual(liter_umwandeln(0.023), "23 ml")
        self.assertEqual(liter_umwandeln(0.0001), "Wert zu klein")

    def test_lkw_maut(self):
        self.assertAlmostEqual(lkw_maut('A', 2, 13), 162.5)
        self.assertAlmostEqual(lkw_maut('D', 5, 13), 252.2)
        self.assertIsNone(lkw_maut('X', 2, 13))

    def test_palindrom(self):
        self.assertTrue(palindrom("Otto"))
        self.assertFalse(palindrom("Hallo"))

    def test_perfekte_zahl(self):
        self.assertTrue(perfekte_zahl(6))
        self.assertTrue(perfekte_zahl(28))
        self.assertFalse(perfekte_zahl(10))
        self.assertFalse(perfekte_zahl(1))

    def test_lambdas(self):
        self.assertEqual(quadrieren(5), 25)
        self.assertEqual(verketten("Hans", "Maier"), "**********\nHans Maier\n**********")


if __name__ == '__main__':
    unittest.main()
