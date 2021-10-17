class Zoo:
    def __init__(self, name, budget, animal_capacity, worker_capacity):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = worker_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal, price):
        if len(self.animals) < self.__animal_capacity and self.__budget - price >= 0:
            self.__budget -= price
            self.animals.append(animal)
            return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

        elif len(self.animals) < self.__animal_capacity:
            return "Not enough budget"

        return "Not enough space for animal"

    def hire_worker(self, worker):
        if len(self.workers) < self.__workers_capacity:
            self.workers.append(worker)
            return f"{worker.name} the {worker.__class__.__name__} hired successfully"

        return "Not enough space for worker"

    def fire_worker(self, name):
        for worker in self.workers:

            if worker.name == name:
                self.workers.remove(worker)
                return f"{name} fired successfully"

        return f"There is no {name} in the zoo"

    def pay_workers(self):
        salary_sum = 0

        for worker in self.workers:
            salary_sum += worker.salary

        if salary_sum <= self.__budget:
            self.__budget -= salary_sum
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"

        return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        take_care_needed_money_sum = 0

        for animal in self.animals:
            take_care_needed_money_sum += animal.money_for_care

        if take_care_needed_money_sum <= self.__budget:
            self.__budget -= take_care_needed_money_sum
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"

        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        lions = []
        cheetahs = []
        tigers = []
        info = ""
        for animal in self.animals:
            if animal.__class__.__name__ == "Lion":
                lions.append(animal.__repr__())
            elif animal.__class__.__name__ == "Cheetah":
                cheetahs.append(animal.__repr__())
            else:
                tigers.append(animal.__repr__())

        info += f"You have {len(self.animals)} animals\n"
        info += f"----- {len(lions)} Lions:\n" + '\n'.join(lions) + "\n"
        info += f"----- {len(tigers)} Tigers:\n" + '\n'.join(tigers) + "\n"
        info += f"----- {len(cheetahs)} Cheetahs:\n" + '\n'.join(cheetahs)

        return info

    def workers_status(self):
        keepers = []
        caretakers = []
        vets = []
        info = ""
        for worker in self.workers:
            if worker.__class__.__name__ == "Keeper":
                keepers.append(worker.__repr__())
            elif worker.__class__.__name__ == "Caretaker":
                caretakers.append(worker.__repr__())
            else:
                vets.append(worker.__repr__())

        info += f"You have {len(self.workers)} workers\n"
        info += f"----- {len(keepers)} Keepers:\n" + '\n'.join(keepers) + "\n"
        info += f"----- {len(caretakers)} Caretakers:\n" + '\n'.join(caretakers) + "\n"
        info += f"----- {len(vets)} Vets:\n" + '\n'.join(vets)

        return info

