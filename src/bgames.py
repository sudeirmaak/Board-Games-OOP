from abc import ABC, abstractmethod

class bgame(ABC):
    def __init__(self, name, publisher, price):
        self.name = name
        self.publisher = publisher
        self.price = price

    @abstractmethod
    def description(self):
        pass

    @abstractmethod
    def calculate_price(self):
        pass

    @abstractmethod
    def special_features(self):
        pass
