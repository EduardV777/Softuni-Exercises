class HorseRace:

    def __init__(self, race_type: str):
        if race_type == "Winter" or race_type == "Spring" or race_type == "Autumn" or race_type == "Summer":
            self.race_type = race_type
        else:
            raise ValueError("Race type does not exist!")

        self.jockeys = []