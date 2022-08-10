from project.beverage.hot_beverage import HotBeverage

class Coffee(HotBeverage):
    price = 3.50
    milliliters = 50
    def __init__(self, name: str, price: float, milliliters: float, caffeine: float):
        super().__init__(name, self.price, self.milliliters)
        self.caffeine = caffeine

    @property
    def caffeine(self):
        return self.__caffeine
    
    @caffeine.setter
    def caffeine(self, val):
        self.__caffeine = val