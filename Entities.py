from random import randint

class characters:

    def __init__(self) -> None:
        self.hp = 100
        self.maxhp = 100
        self.strength = 0
        self.agility = 1
        self.weapon = 1
        self.speed = 10
        self.shield = 0
        self.damage = self.strength * self.weapon
        self.eberseg = 100
        self.rep = 0


class Enemies:
    def __init__(self, hp, strength, speed, shield) -> None:
        self.hp = hp
        self.ststrength =strength
        self.speed = speed
        self.shield =shield

player = characters()




