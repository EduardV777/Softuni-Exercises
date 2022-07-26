"""
[Liskov Substitution Principle]
Refactor the provided code so it is in line with the Liskov Substitution Principle.
"""

from abc import abstractmethod, ABC


class Duck(ABC):
    @staticmethod
    def quack():
        pass

    @staticmethod
    def walk():
        pass

    @staticmethod
    def fly():
        pass


class RubberDuck(Duck):
    @staticmethod
    def quack():
        return "Squeek"

    @staticmethod
    def walk():
        return 'I cannot walk by myself'

    @staticmethod
    def fly():
        return 'I cannot fly by myself'


class RobotDuck(Duck):
    HEIGHT = 50

    def __init__(self):
        self.height = 0

    @staticmethod
    def quack():
        return 'Robotic quacking'

    @staticmethod
    def walk():
        return 'Robotic walking'

    
    def fly(self):
        if self.height == self.HEIGHT:
            self.land()
            return "I have landed."
        else:
            self.goUp()
            return "I am flying."
        

    def land(self):
        self.height = 0

    def goUp(self):
        self.height += 1


rubDuck = RubberDuck()

print(rubDuck.quack())
print(rubDuck.walk())
print(rubDuck.fly())

print("\n")

robDuck = RobotDuck()

print(robDuck.quack())
print(robDuck.walk())
for k in range(0, 51):
    print(robDuck.fly())