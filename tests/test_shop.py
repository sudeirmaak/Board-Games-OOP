import unittest
from src.shop import Shop
from src.genres import CoopGames, WordGames
class TestShop(unittest.TestCase):
    def setUp(self):
        self.shop = Shop()

    def test_add_game(self):
        game1 = CoopGames("Game1", "Publisher1", 50, "2/5")
        self.shop.add_game(game1)
        self.assertEqual(len(self.shop.inventory), 1)

    def test_list_inventory(self):
        game1 = CoopGames("Game1", "Publisher1", 50, "2/5")
        game2 = WordGames("Game2", "Publisher2", 30, "4/5")
        self.shop.add_game(game1)
        self.shop.add_game(game2)
        import sys
        from io import StringIO
        saved_stdout = sys.stdout
        try:
            out = StringIO()
            sys.stdout = out
            self.shop.list_inventory()
            output = out.getvalue().strip().split('\n')
            self.assertEqual(len(output), 2)  
        finally:
            sys.stdout = saved_stdout

    def test_sell_game(self):
        game1 = CoopGames("Game1", "Publisher1", 50, "2/5")
        self.shop.add_game(game1)
        price = self.shop.sell_game("Game1")
        self.assertEqual(price, 50)

    def test_total_inventory_value(self):
        game1 = CoopGames("Game1", "Publisher1", 50, "2/5")
        game2 = WordGames("Game2", "Publisher2", 30, "4/5")
        self.shop.add_game(game1)
        self.shop.add_game(game2)
        total_value = self.shop.total_inventory_value()
        self.assertEqual(total_value, 80)  

if __name__ == '__main__':
    unittest.main()
