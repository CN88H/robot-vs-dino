from robot import Robot

# robots = ["bender", "wallee", ""]

class Fleet:
    def __init__(self) -> None:
        self.robots = []
        self.create_fleet()

    def create_fleet(self):        
        bender_robot = Robot("Bender")
        Gerrald = Robot("Gerrald")
        Gundam = Robot("Gundam")
        self.robots.append(bender_robot)
        self.robots.append(Gerrald)
        self.robots.append(Gundam)
        
        #create one more robot
        #use .append to add each robot object into self.robots