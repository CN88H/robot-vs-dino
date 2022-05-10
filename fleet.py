from robot import Robot

# robots = ["bender", "wallee", ""]

class Fleet:
    def __init__(self):
        self.robots = []
        self.create_fleet()

    def create_fleet(self):        
        robo_1 = Robot("Bender")
        robo_2 = Robot("Gerrald")
        robo_3 = Robot("Gundam")
        self.robots.append(robo_1)
        self.robots.append(robo_2)
        self.robots.append(robo_3)
        

    # def __str__(self) -> str:
    #     return self.name
        #create one more robot
        #use .append to add each robot object into self.robots