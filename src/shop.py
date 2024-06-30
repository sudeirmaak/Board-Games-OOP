from .tracker import log_action

class Shop:
    def __init__(self):
        self.inventory = []

    @log_action("added")
    def add_game(self, game):
        self.inventory.append(game)

    def list_inventory(self):
        for game in self.inventory:
            print(game.description())

    @log_action("sold")
    def sell_game(self, game_name):
        for game in self.inventory:
            if game.name == game_name:
                self.inventory.remove(game)
                return game.calc_p()
        return f"{game_name} is not in stock."

    def total_inventory_value(self):
        total_value = 0
        for game in self.inventory:
            total_value += game.calc_p()
        return total_value
