import unittest
from src.genres import CoopGames

class TestDiscount(unittest.TestCase):

    def setUp(self):
        self.game = CoopGames("Robinson Cruose", "Portal Games", 15, "2/5", discount_rate=0.5)

    def test_apply_discount(self):
        discounted_price = self.game.apply_discount()
        self.assertEqual(discounted_price, 7.5) 

if __name__ == '__main__':
    unittest.main()
