class user():
    def sign_in(self):
        print("logged in")

class wizard(user):
    def __init__(self,name,power):
        self.name =name
        self.power =power

    def attack(self):
        print(f"attacking with the power of {self.power}")

class elves(user):
     def __init__(self,name,gunshots):
        self.name =name
        self.gunshots =gunshots


    def attack(self):
        print(f"attacking with guns with {gunshots} bullets" )

wizard1=wizard('merlin', 1000)
elves1 = elves("kevin", 24)

wizard.attack()
elves.attack()

