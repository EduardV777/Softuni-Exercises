from .main_dish import MainDish

class Salmon(MainDish):
    grams = 22

    def __init__(self, name: str, price: float):
        super().__init__(name, price, self.grams)