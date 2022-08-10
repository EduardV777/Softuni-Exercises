class Zoo:

    animals = []
    workers = []

    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity

    def add_animal(self, animal, price):
        if self.__budget >= price and self.__animal_capacity > 0:
            typeOfAnimal = ""

            if animal.__class__.__name__ == "Lion":
                typeOfAnimal = "Lion"
            elif animal.__class__.__name__ == "Tiger":
                typeOfAnimal = "Tiger"
            elif animal.__class__.__name__ == "Cheetah":
                typeOfAnimal = "Cheetah"

            self.animals.append(animal)
            self.__animal_capacity -= 1
            self.__budget -= price
            return f"{animal.name} the {typeOfAnimal} added to the zoo"
        
        elif self.__budget >= price and self.__animal_capacity == 0:
            return "Not enough space for animal"
        
        elif self.__budget < price and self.__animal_capacity > 0:
            return "Not enough budget"

    def hire_worker(self, worker):
        if self.__workers_capacity > 0:
            typeOfWorker = ""
            self.workers.append(worker)
            self.__workers_capacity -= 1

            if worker.__class__.__name__ == "Keeper":
                typeOfWorker = "Keeper"
            elif worker.__class__.__name__ == "Vet":
                typeOfWorker = "Vet"
            elif worker.__class__.__name__ == "Caretaker":
                typeOfWorker = "Caretaker"

            return f"{worker.name} the {typeOfWorker} hired successfully"

        else:
            return "Not enough space for worker"

    def fire_worker(self, worker_name):
        
        for k in range(0, len(self.workers)):
            if self.workers[k].name == worker_name:
                del self.workers[k]
                return f"{worker_name} fired successfully"
            
            if k == len(self.workers) - 1:
                return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        totalSalaryPayment = 0

        for worker in self.workers:
            totalSalaryPayment += worker.salary

        if self.__budget >= totalSalaryPayment:
            self.__budget -= totalSalaryPayment
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"
        
        else:
            return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        totalCareExpenses = 0

        for animal in self.animals:
            totalCareExpenses += animal.money_for_care
        
        if self.__budget >= totalCareExpenses:
            self.__budget -= totalCareExpenses
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
            if animal.__class__.__name__ == "Lion":
                lions.append(animal)
            elif animal.__class__.__name__ == "Tiger":
                tigers.append(animal)
            elif animal.__class__.__name__ == "Cheetah":
                cheetahs.append(animal)

        output = f"You have {len(self.animals)} animals\n----- {len(lions)} Lions:\n"

        for k in range(0, len(lions)):
            output += lions[k].__repr__() + "\n"

        output += f"----- {len(tigers)} Tigers:\n"

        for k in range(0, len(tigers)):
            output += tigers[k].__repr__() + "\n"

        output += f"----- {len(cheetahs)} Cheetahs:\n"

        for k in range(0, len(cheetahs)):
            output += cheetahs[k].__repr__()

            if k != len(cheetahs) - 1:
                output += "\n"
        
        return output


    def workers_status(self):
        caretakers = []
        vets = []
        keepers = []

        for worker in self.workers:
            if worker.__class__.__name__ == "Keeper":
                keepers.append(worker)
            elif worker.__class__.__name__ == "Caretaker":
                caretakers.append(worker)
            elif worker.__class__.__name__ == "Vet":
                vets.append(worker)

        output = f"You have {len(self.workers)} workers\n----- {len(keepers)} Keepers:\n"

        for k in range(0, len(keepers)):
            output += keepers[k].__repr__()+"\n"

        output += f"----- {len(caretakers)} Caretakers:\n"

        for k in range(0, len(caretakers)):
            output += caretakers[k].__repr__()+"\n"

        output += f"----- {len(vets)} Vets:\n"

        for k in range(0, len(vets)):
            output += vets[k].__repr__()

            if k != len(vets) - 1:
                output += "\n"

        return output