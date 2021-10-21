class ExercisePlan:
    __plan_id = 0

    def __init__(self, trainer_id, equipment_id, duration):
        self.trainer_id = trainer_id
        self.equipment_id = equipment_id
        self.duration = duration
        self.id = ExercisePlan.get_next_id()

    @classmethod
    def from_hours(cls, trainer_id, equipment_id, hours):
        return cls(trainer_id, equipment_id, hours * 60)

    @staticmethod
    def get_next_id():
        ExercisePlan.__plan_id += 1
        return ExercisePlan.__plan_id

    def __repr__(self):
        return f"Plan <{self.id}> with duration {self.duration} minutes"



