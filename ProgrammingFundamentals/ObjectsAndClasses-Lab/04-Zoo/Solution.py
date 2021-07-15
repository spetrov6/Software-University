class Zoo:
    __animals = 0
    def __init__(self,name_of_zoo):
        self.name_of_zoo = name_of_zoo
        self.mammals = []
        self.fishes = []
        self.birds = []
    def add_animal(self,species,name):
        if species == "mammal":
            self.mammals.append(name)
        elif species == "fish":
            self.fishes.append(name)
        elif species == "bird":
            self.birds.append(name)
    def get_info(self,species,animals_count):
        Zoo.__animals = animals_count
        if species == "mammal":
            return f"Mammals in {self.name_of_zoo}: {', '.join(self.mammals)}\nTotal animals: {Zoo.__animals}"
        elif species == "fish":
            return f"Fishes in {self.name_of_zoo}: {', '.join(self.fishes)}\nTotal animals: {Zoo.__animals}"
        elif species == "bird":
            return f"Birds in {self.name_of_zoo}: {', '.join(self.birds)}\nTotal animals: {Zoo.__animals}"
zoo = Zoo(input())
animals = int(input())
for i in range(animals):
    spicies,name = input().split()
    zoo.add_animal(spicies,name)
print(zoo.get_info(input(),animals))

