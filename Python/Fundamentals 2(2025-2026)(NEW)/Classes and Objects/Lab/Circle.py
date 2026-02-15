class Circle:
    __pi = 3.14

    def __init__(self, d):
        self.d = d

    def calculate_circumference(self):
        return round(self.d * self.__pi, 2)

    def calculate_area(self):
        r = self.d / 2
        return round((r * r) * self.__pi, 2)

    def calculate_area_of_sector(self, angle):
        return round((angle / 360) * self.calculate_circumference(), 2)

c1 = Circle(18)

# print(c1.calculate_area())
# print(c1.calculate_circumference())
# print(c1.calculate_area_of_sector(10))