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
    def calc_p(self):
        pass

    @abstractmethod
    def details(self):
        pass
