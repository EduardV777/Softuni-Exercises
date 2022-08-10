from project.product import Product

class ProductRepository:

    def __init__(self):
        self.products = []


    def add(self, product: Product):
        self.products.append(product)

    def find(self, product_name: str):
        for k in range(0, len(self.products)):
            if self.products[k].name == product_name:
                return self.products[k]
    
    def remove(self, product_name: str):
        for k in range(0, len(self.products)):
            if self.products[k].name == product_name:
                del self.products[k]
                break
    
    def __repr__(self):
        output = ""

        for k in range(0, len(self.products)):
            output += f"{self.products[k].name}: {self.products[k].quantity}"

            if k != len(self.products) - 1:
                output += "\n"
        
        return output