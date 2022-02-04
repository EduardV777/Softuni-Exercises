class Storage:
    storage=[]; checkCap=0
    def __init__(self,capacity):
        self.cap=capacity
    def add_product(self,prodStr):
        if not self.checkCap>=self.cap:
            self.storage.append(prodStr)
            self.checkCap+=1
    def get_products(self):
        return self.storage

storage = Storage(4)
storage.add_product("apple")
storage.add_product("banana")
storage.add_product("potato")
storage.add_product("tomato")
storage.add_product("bread")
print(storage.get_products())
