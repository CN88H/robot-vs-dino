from dinosaur import Dinosaur

class Herd:
    def __init__(self):
        self.dinosaurs = []
        self.create_herd()

    def create_herd(self):
        dino_1 = Dinosaur("T Rex", 30)
        dino_2 = Dinosaur("Triceratops", 40)
        dino_3 = Dinosaur("Spinosaurus", 50)
        self.dinosaurs.append(dino_1)
        self.dinosaurs.append(dino_2)
        self.dinosaurs.append(dino_3)
        

    # def __str__(self) -> str:
    #     return self.name
        # self.herd_list = [self.first_dino, self.second_dino, self.third_dino]

        




# from dinosaur import Dinosaur

# t_rex = Dinosaur("Big T")

# triceratops = Dinosaur("Trio Point")

# spinosaurus = Dinosaur("Spike")