class rhombus():

    def __init__(self, n):
        self.size = n
        self.rhombusStr = self.createRhombus()

    def createRhombus(self):
        rhombus = ""

        for k in range(1, self.size + 1):
            rhombus += f"{' ' * (self.size - k)}{'* ' * k}"
            rhombus += "\n"

        for k2 in range(self.size - 1 , 0, -1):
            rhombus += f"{' ' * (self.size - k2)}{'* ' * k2}"

            if k != 1:
                rhombus += "\n"

        return rhombus

    def __repr__(self):
        return self.rhombusStr

n = int(input())

rhomb1 = rhombus(n)

print(rhomb1)