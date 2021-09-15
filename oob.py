class Rocket():
    def __init__(self, x_loc=0, y_loc=0, height=200):
        self.height = height
        self.x_loc = x_loc
        self.y_loc = y_loc


    def move_rocket(self,y_vel,x_vel):
        self.y_loc += y_vel
        self.x_loc += x_vel

Rocket2 = Rocket(200, 300)

for i in range(10):
    Rocket2.move_rocket(int(input(f"At what rate is the rocket moving vertically? : ")), \
                        int(input(f"At what rate is the rocket moving horizontally? : ")))
    print(Rocket2.y_loc)
    print(Rocket2.x_loc)
    print()

def rocket_fleet():
