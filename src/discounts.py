class Discounts:
    def __init__(self, discount_rate=0):
        self.discount_rate = discount_rate

    def apply_discount(self):
        discounted_price = self.price * (1 - self.discount_rate)
        return discounted_price

