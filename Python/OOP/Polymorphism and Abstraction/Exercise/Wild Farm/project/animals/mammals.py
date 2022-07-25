from abc import ABC, abstractmethod
from project.animals.animal import Animal
from project.food import *

class Mammal(Animal, ABC):
    
    def __init__(self, name: str, weight: float, living_region: str):
        super().__init__(name, weight)
        self.living_region = living_region

    def __repr__(self):
        return f"{self.__class__.__name__} [{self.name}, {self.weight}, {self.living_region}, {self.food_eaten}]"

class Mouse(Mammal):
    
    def __init__(self, name: str, weight: float, living_region: str):
        super().__init__(name, weight, living_region)


    def make_sound(self):
        return "Squeak"

    def feed(self, food):
        if food.__class__.__name__ != "Vegetable" and food.__class__.__name__ != "Fruit":
            return 	f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"
        else:
            self.weight += 0.10 * food.quantity
            self.food_eaten += food.quantity

class Dog(Mammal):

    def __init__(self, name: str, weight: float, living_region: str):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return "Woof!"

    def feed(self, food):
        if food.__class__.__name__ != "Meat":
            return 	f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"
        else:
            self.weight += 0.40 * food.quantity
            self.food_eaten += food.quantity    

class Cat(Mammal):

    def __init__(self, name: str, weight: float, living_region: str):
        super().__init__(name, weight, living_region)    

    
    def make_sound(self):
        return "Meow"

    def feed(self, food):
        if food.__class__.__name__ != "Meat" and food.__class__.__name__ != "Vegetable":
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"
        else:
            self.weight += 0.30 * food.quantity
            self.food_eaten += food.quantity

class Tiger(Mammal):
    
    def __init__(self, name: str, weight: float, living_region: str):
        super().__init__(name, weight, living_region)


    def make_sound(self):
        return "ROAR!!!"

    def feed(self, food):
        if food.__class__.__name__ != "Meat":
            return 	f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"
        else:
            self.weight += 1.00 * food.quantity
            self.food_eaten += food.quantity