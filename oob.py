import random as r

class Rocket():
    def __init__(self, x_loc=0, y_loc=0, height=200):
        self.height = height
        self.x_loc = x_loc
        self.y_loc = y_loc


    def move_rocket(self,y_vel,x_vel):
        self.y_loc += y_vel
        self.x_loc += x_vel

Rocket1 = Rocket(200, 300)

for i in range(5):
    Rocket1.move_rocket(int(input(f"At what rate is the rocket moving vertically? : ")), \
                        int(input(f"At what rate is the rocket moving horizontally? : ")))
    print(Rocket1.y_loc)
    print(Rocket1.x_loc)
    print()

def rocket_fleet():
    set = 0
    whichone = 0
    list =[]
    while set < 4:
        rdmrocket = Rocket(r.randrange(50, 450),(r.randrange(50, 450)))
        list.append(rdmrocket)
        set +=1
    for gabagool in list:
        print(f"Rocket {whichone+1} is at x={gabagool.x_loc}, y={gabagool.y_loc}.")
        whichone += 1
        gabagool.x_loc += r.randrange(10, 150)
        gabagool.y_loc += r.randrange(10, 150)
    whichone=0
    for gabagool in list:
        print(f"Rocket {whichone+1} is NOW at x={gabagool.x_loc}, y={gabagool.y_loc}.")
        whichone += 1

def get_distance():
    p
rocket_fleet()





class Rocket():
    def __init__(self, x_loc=0, y_loc=0, color="red", mass=200 ):
        self.color = color
        self.x_loc = x_loc
        self.y_loc = y_loc
        self.mass = mass


    def move_rocket(self,y_vel,x_vel):
        self.y_loc += y_vel
        self.x_loc += x_vel

rocketnew1 = Rocket()
rocketnew2 = Rocket(100, 2, "blue", 800)
news=[rocketnew1,rocketnew2]
for rocket in news:
    print(rocket.color, rocket.mass)