class Storage:
    __storage = []

    def __init__(self, capacity):
        self.cap = capacity

    def get_products(self):
        return self.__storage

    def add_product(self, prod: str):
        if len(self.__storage) < self.cap:
            self.__storage.append(prod)

# storage = Storage(4)
# storage.add_product("apple")
# storage.add_product("banana")
# storage.add_product("potato")
# storage.add_product("tomato")
# storage.add_product("bread")
# print(storage.get_products())