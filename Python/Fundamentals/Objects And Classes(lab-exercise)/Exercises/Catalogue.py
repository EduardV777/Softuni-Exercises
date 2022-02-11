class Catalogue:
    products=[]
    def __init__(self, name):
        self.name=name
    def add_product(self, product_name: str):
        self.products.append(product_name)
    def get_by_letter(self, first_letter: str):
        newList=[e for e in self.products if e[0]==first_letter]
        return newList
    def __repr__(self):
        self.products.sort()
        items="\n".join(self.products)
        return f'Items in the {self.name} catalogue:\n{items}'
    
# catalogue = Catalogue("Furniture")
# catalogue.add_product("Sofa")
# catalogue.add_product("Mirror")
# catalogue.add_product("Desk")
# catalogue.add_product("Chair")
# catalogue.add_product("Carpet")
# print(catalogue.get_by_letter("C"))
# print(catalogue)
