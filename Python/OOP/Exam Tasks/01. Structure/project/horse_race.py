from .jockey import Jockey

class HorseRace:
    
    def __init__(self, race_type: str):
        self.race_type = race_type
        self.jockeys = []
    
    @property
    def race_type(self):
        return self.__race_type
    
    @race_type.setter
    def race_type(self, val):
        if val != "Autumn" and val != "Summer" and val != "Winter" and val != "Spring":
            raise ValueError("Race type does not exist!")
        else:
            self.__race_type = val