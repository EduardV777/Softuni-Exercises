class Circle:
    def __init__(self,d):
        self.diameter=d
        self.__pi=3.14
    def calculate_circumference(self):
        c=self.__pi*self.diameter
        return c
    def calculate_area(self):
        r=self.diameter/2
        return self.__pi*(r*r)
    def calculate_area_of_sector(self,angle):
        c=self.calculate_circumference(); r=self.diameter/2
        a=(angle*c)/360
        sectorS=(r/2)*a
        return sectorS

#test
circle1=Circle(10)
print(f"{circle1.calculate_circumference():.2f}\n{circle1.calculate_area():.2f}\n{circle1.calculate_area_of_sector(5):.2f}")
