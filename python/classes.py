from random import randint


class characters: #sablon

    def __init__(self) -> None:
        self.hp = 100
        self.strength = 1
        self.agility = 1
        self.speed = 1
        self.weapon = 0
        self.shield = 0
        self.damage = self.strength * self.weapon
        self.eberseg = 100
        self.rep = 0

class Enemies:
    def __init__(self, name, hp, strength, speed, shield) -> None:
        self.name = name
        self.hp = hp
        self.strength = strength
        self.speed = speed
        self.shield = shield
    def __str__(self) -> str:
        return self.name
    
class weapon:
    def __init__(self, name, damage, price) -> None:
        self.damage = damage
        self.price = price
        self.name = name

    def __str__(self):
        return self.name

class shield:
    def __init__(self, name, shield, price) -> None:
        self.shield = shield
        self.price = price
        self.name = name

    def __str__(self):
        return self.name
    
class armor:
    def __init__(self, name,shield, price) -> None:
        self.shield = shield
        self.price = price
        self.name = name

    def __str__(self):
        return self.name