from project.animals.animal import Mammal
from project.food import Meat


class Mouse(Mammal):
    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    @staticmethod
    def make_sound():
        return "Squeak"

    def feed(self, food):
        type_of_foods = ["Vegetable", "Fruit"]
        if food.__class__.__name__ in type_of_foods:
            self.weight += 0.10 * food.quantity
            self.food_eaten += food.quantity

        return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"


class Dog(Mammal):
    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    @staticmethod
    def make_sound():
        return "Woof!"

    def feed(self, food):
        if isinstance(food, Meat):
            self.weight += 0.40 * food.quantity
            self.food_eaten += food.quantity
            return

        return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"


class Cat(Mammal):
    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    @staticmethod
    def make_sound():
        return "Meow"

    def feed(self, food):
        type_of_foods = ["Vegetable", "Meat"]
        if food.__class__.__name__ in type_of_foods:
            self.weight += 0.30 * food.quantity
            self.food_eaten += food.quantity

        return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"


class Tiger(Mammal):
    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    @staticmethod
    def make_sound():
        return "ROAR!!!"

    def feed(self, food):
        if isinstance(food, Meat):
            self.weight += 1.00 * food.quantity
            self.food_eaten += food.quantity
            return

        return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"