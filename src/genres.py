from .bgames import bgame

class CoopGames(bgame):
    def __init__(self, name, publisher, price, complexity):
        super().__init__(name, publisher, price)
        self._complexity = complexity

    def description(self):
        return f"{self.name} is a cooperative game published by {self.publisher}. Complexity: {self._complexity}."

    def calc_p(self):
        return self.price

    def details(self):
        return "Players work together to achieve a common goal! You all win or you all lose. Includes a rule book and all the tips for an enjoyable coop-game! "

class AbsStrategyGames(bgame):
    def __init__(self, name, publisher, price, strategy, complexity):
        super().__init__(name, publisher, price)
        self._strategy = strategy
        self._complexity = complexity

    def description(self):
        return f"{self.name} is an abstract strategy game published by {self.publisher} with {self._strategy} elements. Complexity: {self._complexity}."

    def calc_p(self):
        return self.price

    def details(self):
        return "There is no luck in this! Master your skills and win."

class KidsGames(bgame):
    def __init__(self, name, publisher, price, age_group, complexity):
        super().__init__(name, publisher, price)
        self._age_group = age_group
        self._complexity = complexity

    def description(self):
        return f"{self.name} is a kids' game published by {self.publisher}, suitable for ages {self._age_group}. Complexity: {self._complexity}."

    def calc_p(self):
        return self.price

    def details(self):
        return "Fun and engaging for the little ones!"

class WordGames(bgame):
    def __init__(self, name, publisher, price, complexity):
        super().__init__(name, publisher, price)
        self._complexity = complexity

    def description(self):
        return f"{self.name} is a word game published by {self.publisher}. Complexity: {self._complexity}."

    def calc_p(self):
        return self.price

    def details(self):
        return "Focuses on vocabulary and word construction."

class DeductionGames(bgame):
    def __init__(self, name, publisher, price, tips, complexity):
        super().__init__(name, publisher, price)
        self._tips = tips
        self._complexity = complexity

    def description(self):
        return f"{self.name} is a deduction game published by {self.publisher} for {self._tips}. Complexity: {self._complexity}."
    
    def calc_p(self):
        return self.price
    
    def details(self):
        return "Solve the mysteries, reveal the truth."
    
class AreaControlGames(bgame):
    def __init__(self, name, publisher, price, mechanics, complexity):
        super().__init__(name, publisher, price)
        self._mechanics = mechanics
        self._complexity = complexity

    def description(self):
        return f"{self.name} is an area-control game by {self.publisher} featuring {self._mechanics}. Complexity: {self._complexity}."
    
    def calc_p(self):
        return self.price
    
    def details(self):
        return "Conquer and defend!"
    
class FamilyGames(bgame):
    def __init__(self, name, publisher, price, age_rec, complexity):
        super().__init__(name, publisher, price)
        self._age_rec = age_rec
        self._complexity = complexity

    def description(self):
        return f"{self.name} is a family game by {self.publisher} recommended for ages {self._age_rec} and up. Complexity: {self._complexity}."
    
    def calc_p(self):
        return self.price
    
    def details(self):
        return "Best way to spend time and have fun with your family!"
    
class PartyGames(bgame):
    def __init__(self, name, publisher, price, max_p, complexity):
        super().__init__(name, publisher, price)
        self._max_p = max_p
        self._complexity = complexity

    def description(self):
        return  f"{self.name} is a party game by {self.publisher} for {self._max_p} people. Complexity: {self._complexity}."
    
    def calc_p(self):
        return self.price
    
    def details(self):
        return "Make your party fun with mini games! Be careful it might be tricky!"