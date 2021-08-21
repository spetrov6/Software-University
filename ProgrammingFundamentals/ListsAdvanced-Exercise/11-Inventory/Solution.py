journal = input().split(", ")
command = input()
while command != "Craft!":
    command_list = command.split(" - ")
    command = command_list[0]
    item = command_list[1]
    if command == "Collect":
        if item not in journal:
            journal.append(item)
    elif command == "Drop":
        if item in journal:
            journal.remove(item)
    elif command == "Renew":
        if item in journal:
            journal.remove(item)
            journal.append(item)
    elif command == "Combine Items":
        item = item.split(":")
        if item[0] in journal:
            index = journal.index(item[0])
            journal.insert(index + 1,item[1])
    command = input()
print(*journal,sep=", ")