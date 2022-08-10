"""
[LSP]
You are provided with a code containing a class Prisoner and a class Person. A prisoner is obviously a person,
but since a prisoner is not free to move an arbitrary distance, the Person class can be named FreePerson, then
the idea that a Prisoner inherits FreePerson is wrong. Rewrite the code and apply the LSP (Liskov
Substitution Principle).
"""
from abc import ABC, abstractmethod
import copy

class Person(ABC):
    
    def __init__(self, position):
        self.position = position

    @abstractmethod
    def walk_north(self, dist):
        pass

    @abstractmethod
    def walk_east(self, dist):
        pass

class PrisonerPerson(Person):

    def __init__(self, position = [0, 0]):
        self.position = position

    def walk_north(self, dist):
        self.position[1] += dist

    def walk_east(self, dist):
        self.position[0] += dist

class FreePerson(PrisonerPerson):
    
    def __init__(self, position = [0, 0]):
        super().__init__(position)


class Prisoner(PrisonerPerson):
    PRISON_LOCATION = [3, 3]

    def __init__(self):
        super(Prisoner, self).__init__(copy.copy(self.PRISON_LOCATION))
        self.is_free = False


prisoner = Prisoner()
print("The prisoner trying to walk to north by 10 and east by -3.")

try:
    if prisoner.is_free == True:
        prisoner.walk_north(10)
        prisoner.walk_east(-3)
    else:
        raise Exception("A prisoner that is not free cannot move freely!")
except Exception:
    print("--- A prisoner cannot move freely! ---")

print(f"The location of the prison: {prisoner.PRISON_LOCATION}")
print(f"The current position of the prisoner: {prisoner.position}")
