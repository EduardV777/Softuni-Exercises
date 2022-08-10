"""
[Open / Closed Principle]
Refactor the provided code, 
so you do not need to make any changes in it when you want to add new species to the animals' list

    animals = [Animal('cat'), Animal('dog'), Animal('chicken')]
"""


class Animal:
    def __init__(self, species):
        self.species = species

    def get_species(self):
        return self.species


def animal_sound(animals: list):
    for animal in animals:
        if animal.species == 'cat':
        
            print('meow')
        elif animal.species == 'dog':
            print('woof-woof')

def addAnimalToList(animal: Animal, animalList: list):
    animalList.append(animal)

def showAllSpeciesInList(animalList: list):
    output = ""
    for k in range(0, len(animalList)):
        output += animalList[k].species
        if k != len(animalList) - 1:
            output += ", "

    return output


animals = [Animal('cat'), Animal('dog')]
animal_sound(animals)
print(showAllSpeciesInList(animals))

addAnimalToList(Animal('chicken'), animals)
print(showAllSpeciesInList(animals))
