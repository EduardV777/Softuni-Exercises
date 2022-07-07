class Cup:
    def __init__(self, size, quantity):
        self.size = size
        self.quantity = quantity

    def fill(self, ml): 
        if (ml + self.quantity <= self.size):
            self.quantity += ml

    def status(self):
        return self.size - self.quantity




#Test code

cup = Cup(100, 50)
print(cup.status())
cup.fill(40)
cup.fill(20)
print(cup.status())