class Weapon:
    def __init__(self,bullets):
        self.bulletCount=bullets
    def shoot(self):
        if self.bulletCount>0:
            self.bulletCount-=1
            return "shooting..."
        else:
            return "no bullets left"
    def __repr__(self):
        return f"Remaining bullets: {self.bulletCount}"

weapon = Weapon(5)
print(weapon.shoot())
print(weapon.shoot())
print(weapon)
print(weapon.shoot())
print(weapon.shoot())
print(weapon.shoot())
print(weapon.shoot())
print(weapon)
