number_wagons = int(input())
wagons = [0] * number_wagons
command = input()
while command != "End":
    command = command.split()
    if command[0] == "add":
        wagons[-1] += int(command[1])
    elif command[0] == "insert":
        wagons[int(command[1])] += int(command[2])
    else:
        wagons[int(command[1])] -= int(command[2])
    command = input()
print(wagons)
