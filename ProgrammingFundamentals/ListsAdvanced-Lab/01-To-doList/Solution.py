notes = input()
result = ["0"] * 10
while notes != "End":
    priority,task = notes.split("-")
    priority = int(priority) - 1
    result[priority] = task
    notes = input()
print([i for i in result if i != "0"])