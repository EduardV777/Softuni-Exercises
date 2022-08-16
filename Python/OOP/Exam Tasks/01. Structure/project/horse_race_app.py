from .jockey import Jockey
from .horse_race import HorseRace
from .horse_specification.appaloosa import Appaloosa
from .horse_specification.thoroughbred import Thoroughbred


class HorseRaceApp:

    def __init__(self):
        self.horses = []
        self.jockeys = []
        self.horse_races = []

    def add_horse(self, horse_type: str, horse_name: str, horse_speed: int):
        for horseObj in self.horses:
            if horseObj.name == horse_name:
                raise Exception(f"Horse {horse_name} has been already added!")
        
        if horse_type == "Appaloosa":
            self.horses.append(Appaloosa(horse_name, horse_speed))
        elif horse_type == "Thoroughbred":
            self.horses.append(Thoroughbred(horse_name, horse_speed))

        return f"{horse_type} horse {horse_name} is added."


    def add_jockey(self, jockey_name: str, age: int):
        for jockeyObj in self.jockeys:
            if jockeyObj.name == jockey_name:
                raise Exception(f"Jockey {jockey_name} has been already added!")

        self.jockeys.append(Jockey(jockey_name, age))
        return f"Jockey {jockey_name} is added."

    def create_horse_race(self, race_type: str):
        for raceObj in self.horse_races:
            if raceObj.race_type == race_type:
                raise Exception(f"Race {race_type} has been already created!")

        self.horse_races.append(HorseRace(race_type))
        return f"Race {race_type} is created."

    def add_horse_to_jockey(self, jockey_name: str, horse_type: str):
        jockeyId = -575
        horseId = -575

        for k in range(0, len(self.jockeys)):
            if self.jockeys[k].name == jockey_name:
                jockeyId = k

        if jockeyId == -575: #jockey not found
            raise Exception(f"Jockey {jockey_name} could not be found!")

        for k in range(len(self.horses) - 1, -1, -1):
            print(self.horses[k].__class__.__name__)
            if (self.horses[k].__class__.__name__ == horse_type) and (self.horses[k].is_taken == False):
                horseId = k

        if horseId == -575: #horse not found
            raise Exception(f"Horse breed {horse_type} could not be found!")
        else:
            if not self.jockeys[jockeyId].horse is None:
                return f"Jockey {jockey_name} already has a horse."
            else:
                self.jockeys[jockeyId].horse = self.horses[horseId]
                self.horses[horseId].is_taken = True
                return f"Jockey {jockey_name} will ride the horse {self.horses[horseId].name}."

    def add_jockey_to_horse_race(self, race_type: str, jockey_name: str):
        jockeyId = -575
        raceId = -575

        for k in range(0, len(self.horse_races)):
            if self.horse_races[k].race_type == race_type:
                raceId = k

        if raceId == -575:
            raise Exception(f"Race {race_type} could not be found!")

        for k in range(0, len(self.jockeys)):
            if self.jockeys[k].name == jockey_name:
                jockeyId = k

        if jockeyId == -575:
            raise Exception(f"Jockey {jockey_name} could not be found!")
        elif self.jockeys[jockeyId].horse is None:
            raise Exception(f"Jockey {jockey_name} cannot race without a horse!")
        else:
            for participant in self.horse_races[raceId].jockeys:
                if participant.name == jockey_name:
                    return f"Jockey {jockey_name} has been already added to the {race_type} race."
            
            self.horse_races[raceId].jockeys.append(self.jockeys[jockeyId])
            return f"Jockey {jockey_name} added to the {race_type} race."

    def start_horse_race(self, race_type: str):
        raceId = -575

        for k in range(0, len(self.horse_races)):
            if self.horse_races[k].race_type == race_type:
                raceId = k

        if raceId == -575:
            raise Exception(f"Race {race_type} could not be found!")

        if len(self.horse_races[raceId].jockeys) < 2:
            raise Exception(f"Horse race {race_type} needs at least two participants!")

        winner = ""
        maxSpeed = 0

        for participant in self.horse_races[raceId].jockeys:
            if participant.horse.speed > maxSpeed:
                winner = participant
                maxSpeed = winner.horse.speed

        return f"The winner of the {race_type} race, with a speed of {maxSpeed}km/h is {winner.name}! Winner's horse: {winner.horse.name}."