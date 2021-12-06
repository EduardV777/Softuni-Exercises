class Inventory:
    items=[]
    def __init__(self, __capacity: int):
        self.__cap=__capacity
        self.capCount=self.__cap
    def add_item(self,item: str):
        if self.capCount>0:
            self.items.append(item)
            self.capCount-=1
        else:
            return "not enough room in the inventory"
    def get_capacity(self):
        return self.__cap
    def __repr__(self):
        return f"Items: {', '.join(self.items)}\nCapacity left: {self.capCount}"

inventory = Inventory(2)
inventory.add_item("potion")
inventory.add_item("sword")
print(inventory.add_item("bottle"))
print(inventory.get_capacity())
print(inventory)
