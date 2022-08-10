from project.food.dessert import Dessert

class Cake(Dessert):
    calories = 1000
    grams = 250
    price = 5

    def __init__(self, name, price, grams):
        super().__init__(name, self.price, self.grams, self.calories)