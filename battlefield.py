from fleet import Fleet
from herd import Herd
# from dinosaur import Dinosaur
# from weapon import Weapon
# from robot import Robot
import random

class Battlefield:
    def __init__(self):
        self.fleet = Fleet()
        self.herd = Herd()
        
# display welcome
    def display_welcome(self):
        print("________________________________________________________")
        print("Welcome to the battle between robots and dinosaurs!")
        print("________________________________________________________")


    def run_game(self):
        self.display_welcome()

        self.choose_attacker()

        self.battle()

        self.display_winners()

        # get battle phase

    def choose_attacker(self):

        print("Pick who to attack.")        

        valid_response = False

        # while valid_response == False:
        while len(self.herd.dinosaurs) > 0 and len(self.fleet.robots) > 0:

            self.selected_turn = input("1 for dinosaurs and 2 for robots: ")

            if self.selected_turn == "1":
                self.selected_turn = self.dino_turn()
                # valid_response = True
                print(f"You picked {self.selected_turn}.")
                if len(self.fleet.robots) > 0:
                    self.robo_turn
            elif self.selected_turn == "2":
                self.selected_turn = self.robo_turn()
                # valid_response = True
                print(f"You picked {self.selected_turn}.")
                if len(self.herd.dinosaurs) > 0:
                    self.dino_turn
            else:
                print("Please pick again.")

    def battle(self):
        print(f"One of the {self.selected_turn} will attack")
        
        if self.selected_turn == self.herd:

            self.herd.dinosaurs[0].attack_robot(self.fleet.robots[0])
            print(f"{self.fleet.robots}")
                if self.




            
        elif self.selected_turn == self.fleet:
            
            self.fleet.robots[0].attack_dino(self.herd.dinosaurs[0])


        #set turns for each
    def dino_turn(self, dinosaur):
        pass

    def robo_turn(self, robot):
        pass

    def show_dino_opponent_option(self):
        # print(f"{Dinosaur.")
        pass

    def show_robo_opponent_option(self):
        pass

    def display_winners(self):
        if len(self.herd.dinosaurs) > len(self.fleet.robots):
            print("Dinosaurs Win!")
        else:
            print("Robots Win!")



        #give options for each turn

        #display health until winner is finalize

        #display winner


