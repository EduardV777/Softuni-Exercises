from abc import ABC, abstractmethod

class Meal(ABC):

    def __init__(self, name: str, price: float, quantity: int):
        self.name = name
        self.price = price
        self.quantity = quantity

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, val):
        if val == "":
            raise ValueError("Name cannot be an empty string!")
        else:
            self.__name = val

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, val):
        if val <= 0:
            raise ValueError("Invalid price!")
        else:
            self.__price = val

    @abstractmethod
    def details():
        pass