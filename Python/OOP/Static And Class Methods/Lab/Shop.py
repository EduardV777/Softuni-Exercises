class Shop:

    def __init__(self, name: str, type: str, capacity: int):
        self.name = name
        self.type = type
        self.capacity = capacity
        self.items = dict()

    @classmethod
    def small_shop(cls, name: str, type: str, capacity = 10):
        return Shop(name, type, capacity)

    def add_item(self, item_name:str):
        itemAdded = False

        if item_name in self.items:
            if self.capacity > 0:
                self.items[item_name] += 1
                self.capacity -= 1
                itemAdded = True
        else:
            if self.capacity > 0:
                self.items[item_name] = 1
                self.capacity -= 1
                itemAdded = True
        
        if itemAdded == True:
            return f"{item_name} added to the shop"
        else:
            return "Not enough capacity in the shop"

    def remove_item(self, item_name: str, amount: int):
        itemRemoved = False

        if item_name in self.items:
            if amount <= self.items[item_name]:
                self.items[item_name] -= amount
                self.capacity += amount

                if self.items[item_name] <= 0:
                    del self.items[item_name]
                
                itemRemoved = True

        if itemRemoved == True:
            return f"{amount} {item_name} removed from the shop"
        else:
            return f"Cannot remove {amount} {item_name}"

    def __repr__(self):
       return f"{self.name} of type {self.type} with capacity {self.capacity}"


fresh_shop = Shop("Fresh Shop", "Fruit and Veg", 50)
small_shop = Shop.small_shop("Fashion Boutique", "Clothes")
print(fresh_shop)
print(small_shop)

print(fresh_shop.add_item("Bananas"))
print(fresh_shop.remove_item("Tomatoes", 2))

print(small_shop.add_item("Jeans"))
print(small_shop.add_item("Jeans"))
print(small_shop.remove_item("Jeans", 2))
print(small_shop.items)
