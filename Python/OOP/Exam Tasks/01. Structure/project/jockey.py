class Jockey:

    def __init__(self, name: str, age: int):
        self.charsInName = False
        
        self.chars = list("qwertyuiopasdfghjklzxcvbnm")

        for ch in self.chars:
            if ch in name:
                self.charsInName = True
                break

        if name == "" or self.charsInName == False:
            raise ValueError("Name should contain at least one character!")

        self.name = name

        if age < 18:
            raise ValueError("Jockeys must be at least 18 to participate in the race!")
        else:
            self.age = age
        
        self.horse = None