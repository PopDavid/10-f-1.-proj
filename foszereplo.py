class characters:

    def __init__(self, hp) -> None:
        self.hp = hp
        self.strength = 0
        self.agility = 1
        self.weapon = 1
        self.speed = 10
        self.shield = 0
        self.damage = self.strength * self.weapon
        self.eberseg = 100

player =characters(hp = 10)
        

