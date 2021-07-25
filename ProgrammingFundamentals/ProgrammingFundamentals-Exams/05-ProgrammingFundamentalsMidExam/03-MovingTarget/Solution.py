targets = [int(i) for i in input().split()]
command_string = input()
strike_list = []
while command_string != "End":
    command_list = command_string.split()
    command = command_list[0]
    index1 = int(command_list[1])
    index2 = int(command_list[2])
    if command == "Shoot":
        if 0 <= index1 < len(targets):
            if targets[index1] > 0:
                targets[index1] -= index2
            if targets[index1] <= 0:
                targets[index1] = 0
    elif command == "Add":
        if 0 <= index1 < len(targets):
            targets.insert(index1,index2)
        else:
            print("Invalid placement!")
    elif command == "Strike":
        if index1 - index2 >= 0 and index1 + index2 < len(targets):
            for index in range(index1 - index2,index1 + index2 + 1):
                targets[index] = 0
        else:
            print("Strike missed!")
    while 0 in targets:
        targets.remove(0)
    command_string = input()
print(*targets,sep="|")
