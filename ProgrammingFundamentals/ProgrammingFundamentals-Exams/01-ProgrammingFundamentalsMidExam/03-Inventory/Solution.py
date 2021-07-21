items = input().split(", ")
command = input()
while command != "Craft!":
    activity,item = command.split(" - ")[0],command.split(" - ")[1]
    if activity == "Collect" and item not in items:
        items.append(item)
    elif activity == "Drop" and item in items:
        items.remove(item)
    elif activity == "Renew" and item in items:
        items.remove(item)
        items.append(item)
    elif activity == "Combine Items":
        old_item,new_item = item.split(":")[0],item.split(":")[1]
        if old_item in items:
            items.insert(items.index(old_item) + 1,new_item)
    command = input()
print(", ".join(items))

