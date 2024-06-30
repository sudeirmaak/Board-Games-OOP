import unittest
from src.genres import CoopGames, AbsStrategyGames, KidsGames, WordGames, DeductionGames, AreaControlGames, FamilyGames, PartyGames
from src.new_bgames import NewGames

class TesNewGames(unittest.TestCase):
    def test_create_coop_game(self):
        kwargs = {"name": "Game1", "publisher": "Game11", "price": 7, "complexity": "2/5"}
        game = NewGames.create_board_game("Cooperative", **kwargs)
        self.assertIsInstance(game, CoopGames)

    def test_create_abs_game(self):
        kwargs = {"name": "Game2", "publisher": "Game22", "price": 6, "strategy": "blablabla", "complexity": "2/5"}
        game = NewGames.create_board_game("Abstract Strategy", **kwargs)
        self.assertIsInstance(game, AbsStrategyGames)

    def test_create_kids_game(self):
        kwargs = {"name": "Game3", "publisher": "Game33", "price": 5, "age_group": "8+", "complexity": "2/5"}
        game = NewGames.create_board_game("Kids", **kwargs)
        self.assertIsInstance(game, KidsGames)

    def test_create_word_game(self):
        kwargs = {"name": "Game4", "publisher": "Game44", "price": 4, "complexity": "2/5"}
        game = NewGames.create_board_game("Word", **kwargs)
        self.assertIsInstance(game, WordGames)

    def test_create_deduction_game(self):
        kwargs = {"name": "Game5", "publisher": "Game55", "price": 3, "tips": "blablabla", "complexity": "2/5"}
        game = NewGames.create_board_game("Deduction", **kwargs)
        self.assertIsInstance(game, DeductionGames)

    def test_create_area_game(self):
        kwargs = {"name": "Game6", "publisher": "Game66", "price": 2, "mechanics": "ahahahahah", "complexity": "2/5"}
        game = NewGames.create_board_game("Area Control", **kwargs)
        self.assertIsInstance(game, AreaControlGames)

    def test_create_family_game(self):
        kwargs = {"name": "Game7", "publisher": "Game77", "price": 1, "age_rec": "6-14", "complexity": "2/5"}
        game = NewGames.create_board_game("Family", **kwargs)
        self.assertIsInstance(game, FamilyGames)

    def test_create_party_game(self):
        kwargs = {"name": "Game8", "publisher": "Game88", "price": 0, "max_p": "12", "complexity": "2/5"}
        game = NewGames.create_board_game("Party", **kwargs)
        self.assertIsInstance(game, PartyGames)

    def test_invalid_game_type(self):
        with self.assertRaises(ValueError):
            NewGames.create_board_game("Non-existing game type.")

if __name__ == '__main__':
    unittest.main()
