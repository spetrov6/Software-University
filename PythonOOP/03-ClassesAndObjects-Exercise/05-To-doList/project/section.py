from project.task import Task


class Section:
    def __init__(self, name: str):
        self.name = name
        self.tasks = []

    def add_task(self, task):
        if task not in self.tasks:
            self.tasks.append(task)
            return f"Task {task.details()} is added to the section"
        return f"Task is already in the section {self.name}"

    def complete_task(self, task_name: str):
        for task in self.tasks:
            if task.name == task_name:
                task.completed = True
                return f"Completed task {task_name}"
        return f"Could not find task with the name {task_name}"

    def clean_section(self):
        count_of_removed_tasks = 0
        for task in self.tasks:
            if task.completed:
                self.tasks.remove(task)
                count_of_removed_tasks += 1
        return f"Cleared {count_of_removed_tasks} tasks."

    def view_section(self):
        result = ""
        result += f"Section {self.name}:\n"
        for task in self.tasks:
            result += f"{task.details()}\n"
        return result


