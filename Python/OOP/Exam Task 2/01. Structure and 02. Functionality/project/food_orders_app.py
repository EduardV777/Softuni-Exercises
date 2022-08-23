from .client import Client
from .meals.dessert import Dessert
from .meals.starter import Starter
from .meals.main_dish import MainDish

class FoodOrdersApp:
    receipt_id = 0

    def __init__(self):
        self.menu = []
        self.clients_list = []

    def register_client(self, client_phone_number: str):
        for client in self.clients_list:
            if client_phone_number == client.phone_number:
                raise Exception("The client has already been registered!")
    
        self.clients_list.append(Client(client_phone_number))
        return f"Client {client_phone_number} registered successfully."

    def add_meals_to_menu(self, *args):
        for currMeal in args:
            if currMeal.__class__.__name__ == "Starter" or currMeal.__class__.__name__ == "MainDish" or currMeal.__class__.__name__ == "Dessert":
                self.menu.append(currMeal)

    def show_menu(self):
        output = ""

        if len(self.menu) < 5:
            raise Exception("The menu is not ready!")

        for k in range(0, len(self.menu)):
            output += self.menu[k].details()
            if k != len(self.menu) - 1:
                output += "\n"
        return output

    def add_meals_to_shopping_cart(self, client_phone_number: str, **kwargs):
        client = ""
        mealsNamesRequested = kwargs.keys()
        currBill = 0

        for currClient in self.clients_list:
            if currClient.phone_number == client_phone_number:
                client = currClient
                break
        
        if client == "":
            client = Client(client_phone_number)
            self.clients_list.append(client)

        for mealName in mealsNamesRequested:
            exists = False
            notEnough = False

            for meal in self.menu:
                if mealName == meal.name:
                    exists = True
                    if kwargs[mealName] > meal.quantity:
                        notEnough = True
            
            if exists == False:
                raise Exception(f"{mealName} is not on the menu!")
            if notEnough == True:
                raise Exception(f"Not enough quantity of {meal.__class__.__name__}: {meal.name}!")

        if len(self.menu) < 5:
            raise Exception("The menu is not ready!")


        for meal in kwargs:
            requestedQty = kwargs[meal]

            for menuMeal in self.menu:
                if menuMeal.name == meal:
                    currBill += menuMeal.price * requestedQty
                    if menuMeal.__class__.__name__ == "Starter":
                        client.shopping_cart.append(Starter(menuMeal.name, menuMeal.price, menuMeal.quantity))
                    elif menuMeal.__class__.__name__ == "MainDish":
                        client.shopping_cart.append(MainDish(menuMeal.name, menuMeal.price, menuMeal.quantity))
                    elif menuMeal.__class__.__name__ == "Dessert":
                        client.shopping_cart.append(Dessert(menuMeal.name, menuMeal.price, menuMeal.quantity))

                    menuMeal.quantity -= requestedQty
                    break
        
        client.bill += currBill
        return f"Client {client_phone_number} successfully ordered {','.join(mealsNamesRequested)} for {client.bill:.2f}lv."

    def cancel_order(self, client_phone_number: str):
        client = ""

        for currClient in self.clients_list:
            if currClient.phone_number == client_phone_number:
                client = currClient

        if len(client.shopping_cart) == 0:
            raise Exception("There are no ordered meals!")

        for meal in client.shopping_cart:
            mealQty = meal.quantity
            
            for menuMeal in self.menu:
                if menuMeal.name == meal.name:
                    menuMeal.quantity += mealQty
        
        client.bill = 0.0
        client.shopping_cart = []
        return f"Client {client.phone_number} successfully canceled his order."

    def finish_order(self, client_phone_number: str):
        client = ""

        for currClient in self.clients_list:
            if currClient.phone_number == client_phone_number:
                client = currClient

        if len(client.shopping_cart) == 0:
            raise Exception("There are no ordered meals!")
        
        cost = client.bill
        client.shopping_cart = []
        client.bill = 0.0

        self.receipt_id += 1
        return f"Receipt #{self.receipt_id} with total amount of {cost:.2f} was successfully paid for {client_phone_number}."


    def __str__(self):
        return f"Food Orders App has {len(self.menu)} meals on the menu and {len(self.clients_list)} clients."