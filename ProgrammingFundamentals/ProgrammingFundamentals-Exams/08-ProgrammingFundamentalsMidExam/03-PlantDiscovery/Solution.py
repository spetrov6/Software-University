plants_count = int(input())
plants_info = {}
for _ in range(plants_count):
    info = input().split("<->")
    plant,rarity = info[0],int(info[1])
    plants_info[plant] = {"rarity":rarity,"rating":[]}
command = input()
while command != "Exhibition":
    activity = command.split(": ")
    if activity[0] == "Rate":
        plant,rating = activity[1].split(" - ")[0],int(activity[1].split(" - ")[1])
        if plant in plants_info:
            plants_info[plant]["rating"].append(rating)
        else:
            print("error")
    elif activity[0] == "Update":
        plant, new_rarity = activity[1].split(" - ")[0], int(activity[1].split(" - ")[1])
        if plant in plants_info:
            plants_info[plant]["rarity"] = new_rarity
        else:
            print("error")
    elif activity[0] == "Reset":
        plant = activity[1]
        if plant in plants_info:
            plants_info[plant]["rating"] = []
        else:
            print("error")
    else:
        print("error")
    command = input()
for key in plants_info:
    if len(plants_info[key]["rating"]) > 0:
        plants_info[key]["rating"] = sum(plants_info[key]["rating"]) / len(plants_info[key]["rating"])
    else:
        plants_info[key]["rating"] = 0
plants_info = dict(sorted(plants_info.items(),key = lambda kvp:(kvp[1]["rarity"],kvp[1]["rating"]),reverse=True))
print(f"Plants for the exhibition:")
for key,value in plants_info.items():
    print(f'- {key}; Rarity: {value["rarity"]}; Rating: {value["rating"]:.2f}')

