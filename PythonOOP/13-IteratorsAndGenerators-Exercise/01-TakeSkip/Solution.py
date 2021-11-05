class take_skip:
    def __init__(self, step, count):
        self.step = step
        self.count = count
        self.steps_count = 0
        self.starting_count_number = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.steps_count >= self.count:
            raise StopIteration
        self.steps_count += 1
        current_count_number = self.starting_count_number
        self.starting_count_number += self.step
        return current_count_number