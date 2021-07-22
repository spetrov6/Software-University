items = input().split("!")
command_string = input()
while command_string != "Go Shopping!":
    command_list = command_string.split()
    command = command_list[0]
    item = command_list[1]
    if len(command_list) == 3:
        item2 = command_list[2]
    if command == "Urgent" and item not in items:
        items.insert(0,item)
    elif command == "Unnecessary" and item in items:
        items.remove(item)
    elif command == "Correct" and item in items:
        items = [i.replace(item,item2) for i in items]
    elif command == "Rearrange" and item in items:
        items.remove(item)
        items.append(item)
    command_string = input()
print(*items,sep=", ")
