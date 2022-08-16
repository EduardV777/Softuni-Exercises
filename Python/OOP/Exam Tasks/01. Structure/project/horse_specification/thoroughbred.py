from .horse import Horse

class Thoroughbred(Horse):

    def __init__(self, name: str, speed: int):
        super().__init__(name, speed)
        self.max_speed = 140

        if len(name) < 4:
            raise ValueError(f"Horse name {name} is less than 4 symbols!")

        if self.speed > self.max_speed:
            raise ValueError("The horse speed is too high!")


    def train(self):
        self.speed += 3

        if self.speed > self.max_speed:
            self.speed = self.max_speed