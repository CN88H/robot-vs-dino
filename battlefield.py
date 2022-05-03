from fleet import Fleet
from herd import Herd
from dinosaur import Dinosaur
from weapon import Weapon
from robot import Robot
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
        print("Pick who to attack.")
        

        valid_response = False

        while valid_response == False:

            self.selected_turn = input("1 for dinosaurs and 2 for robots: ")

            if self.selected_turn == "1":
                self.selected_turn = self.herd
                valid_response = True
            elif self.selected_turn == "2":
                self.selected_turn = self.fleet
                valid_response = True
            else:
                print("Please pick again.")

        # get battle phase
    def battle(self):
        pass


        #set turns for each
    def dino_turn(self, dinosaur):
        pass

    def robo_turn(self, robot):
        pass

    def show_dino_opponent_option(self):
        pass

    def show_robo_opponent_option(self):
        pass

    def diplay_winners(self):
        pass



        #give options for each turn

        #display health until winner is finalize

        #display winner
        pass

