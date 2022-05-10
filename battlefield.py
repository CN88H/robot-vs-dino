from fleet import Fleet
from herd import Herd
# import random

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

        self.battle()

        self.display_winners()

        # get battle phase

    def battle(self):
        print("Pick who to attack.")        

        # valid_response = False

        # while valid_response == False:
        while len(self.herd.dinosaurs) > 0 and len(self.fleet.robots) > 0:

            self.selected_turn = input("1 for dinosaurs and 2 for robots: ")

            if self.selected_turn == "1":
                self.selected_turn = self.herd
                # valid_response = True
                print(f"You picked {self.selected_turn}.")
                self.dino_turn()
         
            elif self.selected_turn == "2":
                self.selected_turn = self.fleet
                # valid_response = True
                print(f"You picked {self.selected_turn}.")
                self.robo_turn()
             
            else:
                print("Please pick again.")

    #     print(f"One of the {self.selected_turn} will attack")
        
    #     if self.selected_turn == self.herd:

    #         self.herd.dinosaurs[0].attack_robot(self.fleet.robots[0])
    #         print(f"{self.fleet.robots}")
            
    #     elif self.selected_turn == self.fleet:
            
    #         self.fleet.robots[0].attack_dino(self.herd.dinosaurs[0])


        #set turns for each
    def dino_turn(self):
        self.herd.dinosaurs[0].attack_robot(self.fleet.robots[0])
        # if robot's health hits zero, remove it from list
        if self.fleet.robots[0].health <= 0:
            print(f"{self.fleet.robots[0]} is dead!")
            self.fleet.robots.remove(self.fleet.robots[0])



        # self.show_dino_opponent_option
        # if self.selected_turn == self.herd:

            

    def robo_turn(self):
        self.fleet.robots[0].attack_dino(self.herd.dinosaurs[0])
        if self.herd.dinosaurs[0].health <= 0:
                self.herd.dinosaurs.remove(self.herd.dinosaurs[0])


        # self.show_robo_opponent_option
        # if self.selected_turn == self.fleet:
            
   
    def show_dino_opponent_option(self):
    # loop through list of dinosaurs and show their names, maybe health
        pass


    def show_robo_opponent_option(self):
        pass


    def display_winners(self):
    # check len of lists, if one is greater than zero, they won
        pass




        #give options for each turn

        #display health until winner is finalize

        #display winner


