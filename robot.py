from weapon import Weapon
# from dinosaur import Dinosaur

class Robot:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.weapon = Weapon("sword", 50)

    def attack_dino(self, dinosaur): 
        dinosaur.health -= self.weapon.attack_power
        print(f"{self.name} attack the {dinosaur.name} with a {self.weapon.weapon_name}.  {dinosaur.name} health is now {dinosaur.health}")





    # def get_weapon(self):
    #     self.