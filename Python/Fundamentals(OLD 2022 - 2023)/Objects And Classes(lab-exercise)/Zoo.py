class Zoo:
    def __init__(self,zooName):
        self.zooName=zooName
        self.__animals=0
        self.mammals=[]; self.fishes=[]; self.birds=[]
    def add_animal(self,species,name):
        if species=="mammal":
            self.mammals.append(name)
        elif species=="fish":
            self.fishes.append(name)
        elif species=="bird":
            self.birds.append(name)
        self.__animals+=1

    def get_info(self,species):
        if species=="mammal":
            return f"Mammals in {self.zooName}: {', '.join(self.mammals)}\nTotal animals: {self.__animals}"
        elif species=="fish":
            return f"Fishes in {self.zooName}: {', '.join(self.fishes)}\nTotal animals: {self.__animals}"
        elif species=="bird":
            return f"Birds in {self.zooName}: {', '.join(self.birds)}\nTotal animals: {self.__animals}"

nameOfZoo=input(); n=int(input())
zoo=Zoo(nameOfZoo)
for k in range(0,n):
    animalInfo=input()
    j=0; species=""; name=""; c=0
    while j<len(animalInfo):
        if animalInfo[j]!=" ":
            val=""
            for i in range(j,len(animalInfo)):
                if animalInfo[i]!=" ":
                    val+=animalInfo[i]
                    j+=1
                else:
                    break
            if c==0:
                species=val
            elif c==1:
                name=val
            c+=1
        else:
            j+=1
    zoo.add_animal(species,name)
species=input()
print(zoo.get_info(species))
