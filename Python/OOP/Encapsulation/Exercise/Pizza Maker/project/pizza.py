from project.dough import Dough
from project.topping import Topping


class Pizza:

    def __init__(self, name: str, dough: Dough, toppings_capacity: int):
        self.name = name
        self.dough = dough
        self.toppings_capacity = ""
        self.toppings_capacity = toppings_capacity
        self.toppings = dict()

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, val):
        if val == "":
            raise ValueError("The name cannot be an empty string")
        
        self.__name = val
    
    @property
    def dough(self):
        return self.__dough
    
    @dough.setter
    def dough(self, val):
        if type(val) == None:
            raise ValueError("You should add dough to the pizza")
        
        self.__dough = val

    @property
    def toppings_capacity(self):
        return self.__toppings_capacity

    @toppings_capacity.setter
    def toppings_capacity(self, val):
        if val != "":
            if val <= 0 and self.__toppings_capacity == "":
                raise ValueError("The topping's capacity cannot be less or equal to zero")
            
        self.__toppings_capacity = val

    def add_topping(self, topping: Topping):
        if self.toppings_capacity == 0:
            raise ValueError("Not enough space for another topping")
        
        currentToppings = self.toppings.keys()

        if topping.topping_type in currentToppings:
            self.toppings[topping.topping_type] += topping.weight
        else:
            self.toppings[topping.topping_type] = topping.weight
            self.toppings_capacity -= 1

    def calculate_total_weight(self):
        totalWeight = 0

        for top in self.toppings:
            totalWeight += self.toppings[top]
        
        totalWeight += self.dough.weight

        return totalWeight