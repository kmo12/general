class Robot:
    def __init__(self, alive=1):
        self.alive = alive
        self.health = 100
        self.motivation = 100

    def checking_condition(self, current_health):
        if current_health <= 0:
            self.alive = 0
            print("\nAaand  it's dead, you are a monster...")

    def hurting(self, power=0):
        if self.alive == 1:
            if power:
                if 1 < power < 5:
                    self.health -= 10
                    print(f"It hurts a little. Now {self.health=}")
                if power == 5:
                    self.health /= 2
                    print(f"Ouch, it hurts, health was halved. Now {int(self.health)=}")
                if 5 < power <= 10:
                    self.health -= power * 10
                    print(f"Wow, you just hurt the robot in {power * 10}. Now {self.health=}")

                Robot().checking_condition(self.health)
        else:
            print("No, you can't hurt a robot, it's already dead.")



Robot().hurting(3)
print("")
Robot().hurting(5)
print("")
Robot().hurting(7)
print("")
Robot().hurting(10)