class Circle:

    pi = 3.14

    def __init__(self, radius):
        self.radius = radius

    def set_radius(self, new_radius):
        self.radius = new_radius

    def get_area(self):
        return (self.radius * self.radius) * 3.14

    def get_circumference(self):
        return (2 * self.radius) * 3.14

#Test code

"""
circle = Circle(10)
circle.set_radius(12)
print(circle.get_area())
print(circle.get_circumference())
"""