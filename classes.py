from random import randint


class characters:

    def __init__(self) -> None:
        self.hp = 100
        self.maxhp = 100
        self.strength = 1
        self.agility = 1
        self.weapon = 0
        self.speed = 1
        self.shield = 0
        self.damage = self.strength * self.weapon
        self.eberseg = 100
        self.rep = 0


class Enemies:
    def __init__(self, hp, strength, speed, shield) -> None:
        self.hp = hp
        self.ststrength = strength
        self.speed = speed
        self.shield = shield


player = characters()


class weapon:
    def __init__(self, name, damage, price) -> None:
        self.damage = damage
        self.price = price
        self.name = name

    def __str__(self):
        return self.name


class defen:
    def __init__(self, name, price) -> None:
        self.shield = shield
        self.price = price
        self.name = name


class shield(defen):
    def __init__(self, name, shield, price) -> None:
        super().__init__(name, shield, price)

    def __str__(self):
        return self.name


class armor(defen): #
    def __init__(self, name, shield, price) -> None:
        super().__init__(name, shield, price)

    def __str__(self):
        return self.name
