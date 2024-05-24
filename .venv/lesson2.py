# Task 1

class Pet:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.hunger = 50
        self.energy = 50
        self.happiness = 50

    def feed(self):
        print(f"\n\nKitchen: \n")
        self.hunger -= 10
        self.energy += 5
        self.happiness += 5
        print(f"{self.name} is now fed. His energy is {self.energy}, hunger is {self.hunger} and happiness is {self.happiness}")

    def play(self):
        print(f"\n\nGames: \n")
        if self.energy >= 10:
            self.happiness += 10
            self.energy -= 10
            print(f"{self.name} plays! His happiness is {self.happiness} and energy is {self.energy}")
        else:
            print(f"{self.name} doesn't have energy to play...")

    def sleep(self):
        print(f"\n\nSleep: \n")
        self.energy += 20
        self.hunger += 10
        print(f"{self.name} is now sleeping! His energy is now {self.energy} and hunger is now {self.hunger}")

    def status(self):
        print(f"\n\nStatus: \n")
        print(f"Name: {self.name}")
        print(f"Species: {self.species}")
        print(f"Hunger: {self.hunger}")
        print(f"Energy: {self.energy}")
        print(f"Happiness: {self.happiness}")

# Приклад використання
my_pet = Pet("Whiskers", "Cat")
print(f"Now you have a pet {my_pet.name}, and it's a {my_pet.species}")
while(True):
    x = str(input("What do you want your pet to do? status/feed/play/sleep/exit : "))
    if x == "status":
        my_pet.status()
    elif x == "feed":
        my_pet.feed()
    elif x == "play":
        my_pet.play()
    elif x == "sleep":
        my_pet.sleep()
    elif x == "exit":
        print("Bye!")
        break
    else:
        print("Invalid command! status/feed/play/sleep/exit : ")