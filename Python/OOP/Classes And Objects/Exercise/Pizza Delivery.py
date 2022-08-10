class PizzaDelivery:

    def __init__(self, name: str, price: float, ingredients: dict):
        self.name = name
        self.price = price
        self.ingredients = ingredients
        self.ordered = False

    def add_extra(self, ingredient: str, quantity: int, price_per_quantity: float):
        if self.ordered == True:
            return f"Pizza {self.name} already prepared, and we can't make any changes!"

        if ingredient in self.ingredients:
            self.ingredients[ingredient] += quantity
        else:
            self.ingredients[ingredient] = quantity

        self.price += quantity * price_per_quantity


    def remove_ingredient(self, ingredient: str, quantity: int, price_per_quantity: float):
        if self.ordered == True:
            return f"Pizza {self.name} already prepared, and we can't make any changes!"

        if not ingredient in self.ingredients:
            return f"Wrong ingredient selected! We do not use {ingredient} in {self.name}!"
        else:
            if quantity > self.ingredients[ingredient]:
                return f"Please check again the desired quantity of {ingredient}!"
            else:
                self.ingredients[ingredient] -= quantity
                self.price -= quantity * price_per_quantity

    def make_order(self):
        numberOfIngredients = len(self.ingredients.keys())
        self.ordered = True
        output = f"You've ordered pizza {self.name} prepared with "

        for ingr in self.ingredients:
            output += ingr + ": " + str(self.ingredients[ingr])
            if numberOfIngredients != 1:
                output += ", "

            numberOfIngredients -= 1

        output += f" and the price will be {self.price}lv."
        return output


#Test code

"""
margarita = PizzaDelivery('Margarita', 11, {'cheese': 2, 'tomatoes': 1})
margarita.add_extra('mozzarella', 1, 0.5)
margarita.add_extra('cheese', 1, 1)
margarita.remove_ingredient('cheese', 1, 1)
print(margarita.remove_ingredient('bacon', 1, 2.5))
print(margarita.remove_ingredient('tomatoes', 2, 0.5))
margarita.remove_ingredient('cheese', 2, 1)
print(margarita.make_order())
print(margarita.add_extra('cheese', 1, 1))
"""
