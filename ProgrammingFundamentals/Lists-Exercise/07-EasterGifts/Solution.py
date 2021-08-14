presents_list = input().split(sep=" ")
command = input()
index_2 = 0
counter= 0
while command != "No Money":
    command = command.split(sep=" ")
    if command[0] == "OutOfStock":
        for i in presents_list:
            if i == command[1]:
                presents_list[counter] = "None"
            counter += 1
    elif command[0] == "Required":
        index_2 = int(command[2])
        if 0 <= index_2 < len(presents_list):
            presents_list[index_2] = command[1]
    elif command[0] == "JustInCase":
            presents_list[-1] = command[1]
    counter = 0
    command = input()
while "None" in presents_list:
    presents_list.remove("None")
print(*presents_list,sep=" ")


