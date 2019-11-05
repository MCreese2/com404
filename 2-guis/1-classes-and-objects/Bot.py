#Creates a class called bot
class Bot:
    #My constuctor, defines how a bot is created (name is mandatory)
    def __init__(self, name, age=0, energy=0, shield_level=0):
        self.name = name
        self.age = age
        self.energy = energy
        self.shield_level = shield_level

    #1st Method; displays the bots name in a box
    def display_name(self):
        print("-" * (len(self.name)+4))
        print("| {} |".format(self.name))
        print("-" * (len(self.name)+4))

    def display_age(self):
        print("""\n   {}
 /----\\""".format(self.age))

    def display_energy(self):
        print("\nEnergy Level: ", end="")
        print("▌" * self.energy, "({})".format(self.energy))

    def display_shield(self):
        print("\n" + "=" * (len(str(self.shield_level))+4))
        print("| {} |".format(self.shield_level))
        print("\\" + "_" * (len(str(self.shield_level))+2) + "/\n")

