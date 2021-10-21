class Trainer:
    __trainer_id = 0

    def __init__(self, name):
        self.name = name
        self.id = Trainer.get_next_id()

    @staticmethod
    def get_next_id():
        Trainer.__trainer_id += 1
        return Trainer.__trainer_id

    def __repr__(self):
        return f"Trainer <{self.id}> {self.name}"