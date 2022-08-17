from .horse_specification.appaloosa import Appaloosa
from .horse_specification.thoroughbred import Thoroughbred
from .jockey import Jockey
from .horse_race import HorseRace

class HorseRaceApp:

    def __init__(self):
        self.jockeys = []
        self.horses = []
        self.horse_races = []
    

    def doesRaceExist(self, race_type: str):
        for k in range(0, len(self.horse_races)):
            if self.horse_races[k].race_type == race_type:
                return k
        
        return -575

    def doesJockeyExist(self, jockey_name: str):
        for k in range(0, len(self.jockeys)):
            if self.jockeys[k].name == jockey_name:
                return k
        
        return -575
    
    def doesHorseExist(self, horse_type: str):
        for k in range(len(self.horses) - 1, -1, -1):
            if self.horses[k].__class__.__name__ == horse_type and self.horses[k].is_taken == False:
                return k

        return -575

    def add_horse(self, horse_type: str, horse_name: str, horse_speed: int):
        horseObj = None

        if horse_type  == "Appaloosa":
            horseObj = Appaloosa(horse_name, horse_speed)
        elif horse_type == "Thoroughbred":
            horseObj = Thoroughbred(horse_name, horse_speed)
        else:
            return

        for horse in self.horses:
            if horse.name == horse_name:
                raise Exception(f"Horse {horse_name} has been already added!")

        self.horses.append(horseObj)
        return f"{horse_type} horse {horse_name} is added."

    def add_jockey(self, jockey_name: str, age: int):
        for jockey in self.jockeys:
            if jockey.name == jockey_name:
                raise Exception(f"Jockey {jockey_name} has been already added!")
            
        jockeyObj = Jockey(jockey_name, age)
        self.jockeys.append(jockeyObj)
        return f"Jockey {jockey_name} is added."

    def create_horse_race(self, race_type: str):
        for race in self.horse_races:
            if race == race_type:
                raise Exception(f"Race {race_type} has been already created!")

        self.horse_races.append(HorseRace(race_type))
        return f"Race {race_type} is created."

    def add_horse_to_jockey(self, jockey_name: str, horse_type: str):
        jockeyId = self.doesJockeyExist(jockey_name)
        horseId = self.doesHorseExist(horse_type)

        if jockeyId == -575:
            raise Exception(f"Jockey {jockey_name} could not be found!")

        if horseId == -575:
            raise Exception(f"Horse breed {horse_type} could not be found!")

        if not self.jockeys[jockeyId].horse is None:
            return f"Jockey {jockey_name} already has a horse."
        else:
            self.jockeys[jockeyId].horse = self.horses[horseId]
            self.horses[horseId].is_taken = True
            return f"Jockey {jockey_name} will ride the horse {self.horses[horseId].name}."

    def add_jockey_to_horse_race(self, race_type: str, jockey_name: str):
        raceId = self.doesRaceExist(race_type)
        jockeyId = self.doesJockeyExist(jockey_name)
    
        if raceId == -575:
            raise Exception(f"Race {race_type} could not be found!")

        if jockeyId == -575:
            raise Exception(f"Jockey {jockey_name} could not be found!")

        if self.jockeys[jockeyId].horse is None:
            raise Exception(f"Jockey {jockey_name} cannot race without a horse!")
        
        for k in range(0, len(self.horse_races[raceId].jockeys)):
            if self.horse_races[raceId].jockeys[k].name == jockey_name:
                return f"Jockey {jockey_name} has been already added to the {race_type} race."

        self.horse_races[raceId].jockeys.append(self.jockeys[jockeyId])
        return f"Jockey {jockey_name} added to the {race_type} race."

    def start_horse_race(self, race_type: str):
        raceId = self.doesRaceExist(race_type)
        speedRadar = 0
        winner = None

        if raceId == -575:
            raise Exception(f"Race {race_type} could not be found!")

        if len(self.horse_races[raceId].jockeys) < 2:
            raise Exception(f"Horse race {race_type} needs at least two participants!")
        
        for participant in self.horse_races[raceId].jockeys:
            if participant.horse.speed > speedRadar:
                speedRadar = participant.horse.speed
                winner = participant

        return f"The winner of the {race_type} race, with a speed of {speedRadar}km/h is {winner.name}! Winner's horse: {winner.horse.name}."