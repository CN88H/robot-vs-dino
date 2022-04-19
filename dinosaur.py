class Dinosaur:
    def __init__(self, name):
        self.name = name
        self.health = 100

    def attack(self):
        self.slash -= 10
        self.bite -= 15
        self.stomp -= 20
    