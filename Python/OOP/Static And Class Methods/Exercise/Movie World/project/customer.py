class Customer:

    def __init__(self, name: str, age: int, id: int):
        self.name = name
        self.age = age
        self.id = id
        self.rented_dvds = list()

    def __repr__(self):
        listOfMovies = []

        for k in range(0, len(self.rented_dvds)):
            listOfMovies.append(self.rented_dvds[k].name)

        return f"{self.id}: {self.name} of age {self.age} has {len(self.rented_dvds)} rented DVD's ({', '.join(listOfMovies)})"