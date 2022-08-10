class PlayerAbilities:

    def __init__(self, name, *args):
        self.playerName = name
        self.abilitiesToAdd = args
        self.abilities = [ability for ability in self.abilitiesToAdd]
    
    def __str__(self):
        return f"{self.playerName}'s abilities: \n{', '.join(self.abilities)}"
    
class CreateNewPlayer(PlayerAbilities):
    pass

player1 = CreateNewPlayer('Valanir', 'Shadow Strike', 'Soul shock')

print(player1)

# ______________________________________

#the super() method

class CreateNewPlayer(PlayerAbilities):
    
    def __init__(self, id, name, *args):
        super().__init__(name, *args)
        self.playerId = id

    def __str__(self):
        return f"{self.playerName}'s with id {self.playerId} abilities:\n {', '.join(self.abilities)}"

player2 = CreateNewPlayer(2,'Nick3242', 'Charge', 'Freeze')
print(player2, end = "\n\n\n\n\n")

#Single inheritance
print("Single inheritance")

class Account:

    def __init__(self, name, type):
        self.name = name
        self.type = type

    def __str__(self):
        return f"Account name: {self.name}\nAccount type: {self.type}"

class AccountManagement(Account):
    def __init__(self, name, type, banned = False):
        super().__init__(name,type)
        self.banned = banned

acc = AccountManagement("Eduard", "Bronze")

print(acc)
print(f"Banned: {acc.banned}", end = "\n\n\n\n")

#Multiple inheritance
print("Multiple inheritance")

class Father:

    def __init__(self):
        self.FatherName = "Evans"

    def get_name(self):
        return self.FatherName

class Mother:

    def __init__(self):
        self.MotherName = "Merry"

    def get_name(self):
        return self.MotherName

class Child(Father, Mother):

    def __init__(self, name):
        Father.__init__(self)
        Mother.__init__(self)
        self.name = name

    def get_parentsInfo(self):
        return f"Father: {self.FatherName}, Mother: {self.MotherName}, Child: {self.name}"

child1 = Child('Anna')

print(child1.get_parentsInfo(), end = "\n\n\n\n")


#Multilevel inheritance
print("Multilevel inheritance")

class Character:

    def __init__(self, name: str, level: int, xp: int):
        self.name = name
        self.level = level
        self.exp = xp
    
    def get_charInfo(self):
        return f"--------------------------\nName: {self.name}\nLevel: {self.level}\nExperience: {self.exp}\n--------------------------"

class CharacterAbilities(Character):

    def __init__(self, name: str, level: int, xp: int, abilities: list):
        super().__init__(name, level, xp)
        self.abilities = abilities
    
    def get_abilitiesInfo(self):
        super().get_charInfo()
        return f"{self.name}'s abilities:\n {', '.join(self.abilities)}"

class AbilitiesInfo(CharacterAbilities):

    def __init__(self, name: str, level: int, xp: int, abilities: list):
        super().__init__(name, level, xp, abilities)

    def getAbilitiesDetails(self):
        output = "-------------------\nAbilities details:\n-------------------\n"
        for ability in self.abilities:
            if ability == "Freeze":
                output += "  Freeze spell:\n   Type: Magic\n   Damage: 25\n   Effects: Stun\n   Cooldown: 10 seconds\n\n"
            elif ability == "Charge":
                output += "  Charge spell:\n   Type: Physical\n   Damage: 20\n   Effects: Stun\n   Cooldown: 30 seconds\n\n"
            elif ability == "Soul Shock":
                output += "  Soul Shock spell:\n   Type: Instant Magic\n   Damage: 30\n   Effects: N/A\n   Cooldown: 60 seconds\n\n"
        
        output += "-------------------\n"

        return output

createChar = AbilitiesInfo('EduardV777', 32, 3200, ['Freeze', 'Soul Shock'])

print(createChar.get_charInfo(), end = "\n")
print(createChar.get_abilitiesInfo(), end = "\n")
print(createChar.getAbilitiesDetails())