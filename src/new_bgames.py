from src.genres import CoopGames, AbsStrategyGames, KidsGames, WordGames, DeductionGames, AreaControlGames, FamilyGames, PartyGames

class NewGames:
    @staticmethod
    def create_board_game(game_type, **kwargs):
        if game_type == "Cooperative":
            return CoopGames(**kwargs)
        elif game_type == "Abstract Strategy":
            return AbsStrategyGames(**kwargs)
        elif game_type == "Kids":
            return KidsGames(**kwargs)
        elif game_type == "Word":
            return WordGames(**kwargs)
        elif game_type == "Deduction":
            return DeductionGames(**kwargs)
        elif game_type == "Area Control":
            return AreaControlGames(**kwargs)
        elif game_type == "Family":
            return FamilyGames(**kwargs)
        elif game_type == "Party":
            return PartyGames(**kwargs)
        else:
            raise ValueError("Non-existing game type.")
