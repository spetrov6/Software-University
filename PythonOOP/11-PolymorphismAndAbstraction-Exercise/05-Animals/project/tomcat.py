from project.cat import Cat


class Tomcat(Cat):
    def __init__(self, name, age):
        self.gender = "Male"
        super().__init__(name, age, self.gender)

    @staticmethod
    def make_sound():
        return "Hiss"
