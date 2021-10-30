from project.cat import Cat


class Kitten(Cat):
    def __init__(self, name, age):
        self.gender = "Female"
        super().__init__(name, age, self.gender)

    @staticmethod
    def make_sound():
        return "Meow"