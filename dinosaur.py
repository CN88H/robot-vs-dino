from robot import Robot

class Dinosaur:
    def __init__(self, name, dino_attack_power):
        self.name = name
        self.health = 100
        self.dino_attack_power = dino_attack_power


    def attack_robot(self, robot):
        robot.health -= self.dino_attack_power
    



        # self.stamina = 100
        # self.slash -= 10
        # self.bite -= 15
        # self.stomp -= 20




