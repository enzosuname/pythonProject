class Rocket():
    def __init__(self, x_loc, y_loc, height=200):
        self.height = height
        self.velocity = 10
        self.x_loc = x_loc
        self.y_loc = y_loc

    def move_up(self):
        self.y_loc += self.velocity

Rocket1 = Rocket(2,3)
Rocket2 = Rocket(200, 300)

for i in range(10):
    Rocket2.move_up()
    print(Rocket2.y_loc)
    print()

enemy_rockets = [Rocket(80, 90) for i in range(10)]
for i in range(10):
    rocket=Rocket(50, 60)
    enemy_rockets.append(rocket)

for rocket in enemy_rockets:
    print(rocket)
