import unittest
from src.bgames import bgame

class TestBoardGame(unittest.TestCase):
    def test_description(self):
        class BoardGame(bgame):
            def description(self):
                return "Description"

            def calculate_price(self):
                return 10

            def special_features(self):
                return "None"

        game = BoardGame("Game", "Publisher", 10)
        self.assertEqual(game.description(), "Description")
        self.assertEqual(game.calculate_price(), 10)
        self.assertEqual(game.special_features(), "None")

if __name__ == '__main__':
    unittest.main()
