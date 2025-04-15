import unittest
from yatzy import Yatzy

class TestYatzy(unittest.TestCase):
    def setUp(self):
        self.game = Yatzy()
        self.game.dice = [1, 1, 2, 2, 2]  # Controlled roll for testing

    def test_ones(self):
        self.assertEqual(self.game.Ones(), 2)

    def test_threes(self):
        self.assertEqual(self.game.Threes(), 0)

    def test_three_alike(self):
        self.assertEqual(self.game.ThreeAlike(), 6)

    def test_two_pairs(self):
        self.assertEqual(self.game.TwoPairs(), 6)

if __name__ == '__main__':
    unittest.main()
