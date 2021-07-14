class Party:
    def __init__(self):
        self.peoples_list = []
    def __len__(self):
        return len(self.peoples_list)
command = input()
peoples = Party()
while command != "End":
    peoples.peoples_list.append(command)
    command = input()
print(f"Going: {', '.join(peoples.peoples_list)}")
print(f"Total: {len(peoples)}")