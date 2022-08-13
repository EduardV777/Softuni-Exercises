from .dessert import Dessert

class Cake(Dessert):
    grams = 250
    calories = 1000
    price = 5
    
    def __init__(self, name: str):
        super().__init__(name, self.price, self.grams, self.calories)