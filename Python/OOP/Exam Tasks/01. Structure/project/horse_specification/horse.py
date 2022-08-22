from abc import ABC, abstractmethod

class Horse(ABC):
    max_speed = None

    def __init__(self, name: str, speed: int):
        self.name = name
        self.speed = speed
        self.is_taken = False

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, val):
        if len(val) < 4:
            raise ValueError("Horse name {value} is less than 4 symbols!")
        else:
            self.__name = val

    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, val):
        if val > self.max_speed:
            raise ValueError("Horse speed is too high!")
        else:
            self.__speed = val

    @abstractmethod
    def train():
        pass