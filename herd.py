from dinosaur import Dinosaur

class Herd:
    def __init__(self):
        self.dinosaurs = []
        self.create_herd()

    def create_herd(self):
        first_dino = Dinosaur("T Rex", 12)
        second_dino = Dinosaur("Triceratops", 10)
        third_dino = Dinosaur("Spinosaurus", 15)
        self.dinosaurs.append(first_dino)
        self.dinosaurs.append(second_dino)
        self.dinosaurs.append(third_dino)
        
        # self.herd_list = [self.first_dino, self.second_dino, self.third_dino]

        




# from dinosaur import Dinosaur

# t_rex = Dinosaur("Big T")

# triceratops = Dinosaur("Trio Point")

# spinosaurus = Dinosaur("Spike")