class Weapon:

    def __init__(self, bullets: int):
        self.cap = bullets


    def shoot(self):
        if self.cap > 0:
            self.cap -= 1
            return "shooting..."

        else:
            return "no bullets left"

    def __repr__(self):
        return f"Remaining bullets: {self.cap}"


# weapon = Weapon(5)
# print(weapon.shoot())
# print(weapon.shoot())
# print(weapon)
# print(weapon.shoot())
# print(weapon.shoot())
# print(weapon.shoot())
# print(weapon.shoot())
# print(weapon)
