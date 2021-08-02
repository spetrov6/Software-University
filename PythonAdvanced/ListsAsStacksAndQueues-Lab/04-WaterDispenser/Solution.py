from collections import deque
water_quantity = int(input())
peoples = deque()
name = input()
while name != "Start":
    peoples.append(name)
    name = input()
command = input()
while command != "End":
    if command.startswith("refill"):
        water_quantity += int(command.split()[-1])
    else:
        if water_quantity >= int(command):
            print(f"{peoples.popleft()} got water")
            water_quantity -= int(command)
        else:
            print(f"{peoples.popleft()} must wait")
    command = input()
print(f"{water_quantity} liters left")