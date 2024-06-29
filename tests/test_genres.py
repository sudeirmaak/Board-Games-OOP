import unittest
from src.genres import CoopGames, AbsStrategyGames, KidsGames, WordGames, DeductionGames, AreaControlGames, FamilyGames, PartyGames

class TestBoardGames(unittest.TestCase):
    
    def test_coop_games(self):
        game = CoopGames("Robinson Crusoe", "Portal Games", 55, "2/5")
        self.assertEqual(game.description(), "Robinson Crusoe is a cooperative game published by Portal Games. Complexity: 2/5.")
        self.assertEqual(game.calc_p(), 55)
        self.assertEqual(game.details(), "Players work together to achieve a common goal! You all win or you all lose. Includes a rule book and all the tips for an enjoyable coop-game! ")

    
    def test_abs_strategy_games(self):
        game = AbsStrategyGames("Azul", "Plan B Games", 30, "different combination and movement", "4/5")
        self.assertEqual(game.description(), "Azul is an abstract strategy game published by Plan B Games with different combination and movement elements. Complexity: 4/5.")
        self.assertEqual(game.calc_p(), 30)
        self.assertEqual(game.details(), "There is no luck in this! Master your skills and win.")
    
    def test_kids_games(self):
        game = KidsGames("Guess Who?", "Theora Design", 18, "6+", "1/5")
        self.assertEqual(game.description(), "Guess Who? is a kids' game published by Theora Design, suitable for ages 6+. Complexity: 1/5.")
        self.assertEqual(game.calc_p(), 18)
        self.assertEqual(game.details(), "Fun and engaging for the little ones!")
    
    def test_word_games(self):
        game = WordGames("Wordle", "Hasbro", 25, "3/5")
        self.assertEqual(game.description(), "Wordle is a word game published by Hasbro. Complexity: 3/5.")
        self.assertEqual(game.calc_p(), 25)
        self.assertEqual(game.details(), "Focuses on vocabulary and word construction.")
    
    def test_deduction_games(self):
        game = DeductionGames("Cluedo", "Hasbro", 45, "finding the murderer in the mansion", "5/5")
        self.assertEqual(game.description(), "Cluedo is a deduction game published by Hasbro for finding the murderer in the mansion. Complexity: 5/5.")
        self.assertEqual(game.calc_p(), 45)
        self.assertEqual(game.details(), "Solve the mysteries, reveal the truth.")
    
    def test_area_control_games(self):
        game = AreaControlGames("Risk", "Hasbro", 33, "diplomacy, conflict and conquest", "4/5")
        self.assertEqual(game.description(), "Risk is an area-control game by Hasbro featuring diplomacy, conflict and conquest. Complexity: 4/5.")
        self.assertEqual(game.calc_p(), 33)
        self.assertEqual(game.details(), "Conquer and defend!")
    
    def test_family_games(self):
        game = FamilyGames("Sushi Go!", "Adventureland Games", 12, "8-14", "2/5")
        self.assertEqual(game.description(), "Sushi Go! is a family game by Adventureland Games recommended for ages 8-14 and up. Complexity: 2/5.")
        self.assertEqual(game.calc_p(), 12)
        self.assertEqual(game.details(), "Best way to spend time and have fun with your family!")
    
    def test_party_games(self):
        game = PartyGames("Taboo", "Hasbro", 22, "6 to 12", "2/5")
        self.assertEqual(game.description(), "Taboo is a party game by Hasbro for 6 to 12 people. Complexity: 2/5.")
        self.assertEqual(game.calc_p(), 22)
        self.assertEqual(game.details(), "Make your party fun with mini games! Be careful it might be tricky!")

if __name__ == '__main__':
    unittest.main()
