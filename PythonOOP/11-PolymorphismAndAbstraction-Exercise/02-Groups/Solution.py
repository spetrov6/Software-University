class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def __repr__(self):
        return f"{self.name} {self.surname}"

    def __add__(self, other):
        return Person(self.name, other.surname)


class Group:
    def __init__(self, name, people):
        self.name = name
        self.people = people

    def __len__(self):
        return len(self.people)

    def __add__(self, other):
        all_peoples = []
        all_peoples.extend(self.people), all_peoples.extend(other.people)
        return Group(f"{self.name} {other.name}", all_peoples)

    def __repr__(self):
        return f"Group {self.name} with members {', '.join([f'{x.name} {x.surname}' for x in self.people])}"

    def __iter__(self):
        for index in range(len(self.people)):
            yield f"Person {index}: {self.people[index].name} {self.people[index].surname}"

    def __getitem__(self, index):
        return f"Person {index}: {self.people[index].name} {self.people[index].surname}"