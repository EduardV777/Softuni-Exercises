from project.product import Product

class Food(Product):

    def __init__(self, name: str, price: str, grams: float):
        super().__init__(name, price)
        self.grams = grams

    @property
    def grams(self):
        return self.__grams

    @grams.setter
    def grams(self, val):
        self.__grams = val