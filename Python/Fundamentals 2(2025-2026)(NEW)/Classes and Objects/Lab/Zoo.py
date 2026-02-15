class Zoo:
    __animals = 0

    def __init__(self, zooName):
        self.zooName = zooName
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animal(self):

        for k in range(0, self.animals):
            info = input().split(" ")

            if info[0] == "mammal":
                self.mammals.append(info[1])

            elif info[0] == "fish":
                self.fishes.append(info[1])

            elif info[0] == "bird":
                self.birds.append(info[1])


    def get_info(self):
        species = input()

        if species == "mammal":
            print(f"Mammals in {self.zooName}: {', '.join(self.mammals)}\nTotal animals: {self.animals}" )

        elif species == "fish":
            print(f"Fishes in {self.zooName}: {', '.join(self.fishes)}\nTotal animals: {self.animals}")

        elif species == "bird":
            print(f"Birds in {self.zooName}: {', '.join(self.birds)}\nTotal animals: {self.animals}")

name = input()
n = int(input())

zoo1 =  Zoo(name)
zoo1.animals = n

zoo1.add_animal()
zoo1.get_info()