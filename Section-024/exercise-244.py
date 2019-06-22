class Chicken:
    total_eggs = 0

    def __init__(self, species, name):
        self.species = species
        self.name = name
        self.eggs = 0

    def lay_egg(self):
        Chicken.total_eggs += 1
        self.eggs += 1
