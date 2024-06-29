import unittest
from src.bgames import bgame

class TestBoardGame(unittest.TestCase):
    def test_description(self):
        class BoardGame(bgame):
            def description(self):
                return "Description"

            def calc_p(self):
                return 10

            def details(self):
                return "None"

        game = BoardGame("Game", "Publisher", 10)
        self.assertEqual(game.description(), "Description")
        self.assertEqual(game.calc_p(), 10)
        self.assertEqual(game.details(), "None")

if __name__ == '__main__':
    unittest.main()
