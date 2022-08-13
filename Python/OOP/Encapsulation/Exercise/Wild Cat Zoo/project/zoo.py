from .lion import Lion
from .cheetah import Cheetah
from .tiger import Tiger
from .caretaker import Caretaker
from .keeper import Keeper
from .vet import Vet

class Zoo:

    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal, price):
        if self.__budget >= price and self.__animal_capacity != 0:
            self.animals.append(animal)
            self.__animal_capacity -= 1
            self.__budget -= price
            return f"{animal.name} the {animal.__class__.__name__} added to the zoo"
        elif self.__animal_capacity != 0 and self.__budget < price:
            return "Not enough budget"
        else:
            return "Not enough space for animal"
        
    def hire_worker(self, worker):
        if self.__workers_capacity != 0:
            self.workers.append(worker)
            self.__workers_capacity -= 1
            return f"{worker.name} the {worker.__class__.__name__} hired successfully"
        else:
            return "Not enough space for worker"
    
    def fire_worker(self, worker_name):
        for k in range(0, len(self.workers)):
            if self.workers[k].name == worker_name:
                del self.workers[k]
                return f"{worker_name} fired successfully"
        
        return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        totalSalary = 0

        for worker in self.workers:
            totalSalary += worker.salary
        
        if totalSalary <= self.__budget:
            self.__budget -= totalSalary
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"
        else:
            return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        totalCosts = 0

        for animal in self.animals:
            totalCosts += animal.money_for_care
        
        if totalCosts <= self.__budget:
            self.__budget -= totalCosts
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        else:
            return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        lions = []
        tigers = []
        cheetahs = []

        for animal in self.animals:
            if isinstance(animal, Lion):
                lions.append(animal)
            elif isinstance(animal, Tiger):
                tigers.append(animal)
            elif isinstance(animal, Cheetah):
                cheetahs.append(animal)

        output = ""
        n = 0

        while n < 3:
            if n == 0:
                output += f"You have {len(self.animals)} animals\n----- {len(lions)} Lions:\n"
                for k in range(0, len(lions)):
                    output += lions[k].__repr__() + "\n"

            elif n == 1:
                output += f"----- {len(tigers)} Tigers:\n"
                for k in range(0, len(tigers)):
                    output += tigers[k].__repr__() + "\n"

            elif n == 2:
                output += f"----- {len(cheetahs)} Cheetahs:\n"
                for k in range(0, len(cheetahs)):
                    output += cheetahs[k].__repr__()

                    if k != len(cheetahs) - 1:
                        output += "\n"
            
            n += 1
        return output
                

    def workers_status(self):
        caretakers = []
        vets = []
        keepers = []
        output = ""

        for worker in self.workers:
            if isinstance(worker, Caretaker):
                caretakers.append(worker)
            elif isinstance(worker, Vet):
                vets.append(worker)
            elif isinstance(worker, Keeper):
                keepers.append(worker)
        
        n = 0

        while n < 3:
            if n == 0:
                output += f"You have {len(self.workers)} workers\n----- {len(keepers)} Keepers:\n"
                for k in range(0, len(keepers)):
                    output += keepers[k].__repr__() + "\n"

            elif n == 1:
                output += f"----- {len(caretakers)} Caretakers:\n"
                for k in range(0, len(caretakers)):
                    output += caretakers[k].__repr__() + "\n"

            elif n == 2:
                output += f"----- {len(vets)} Vets:\n"
                for k in range(0, len(vets)):
                    output += vets[k].__repr__()

                    if k != len(vets) - 1:
                        output += "\n"

            n += 1

        return output