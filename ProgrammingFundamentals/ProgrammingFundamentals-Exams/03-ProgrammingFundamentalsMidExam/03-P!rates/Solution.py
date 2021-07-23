command = input()
cities = {}
while command != "Sail":
    city,population,gold = command.split("||")
    population,gold = int(population),int(gold)
    if city not in cities:
        cities[city] = {"population":0,"gold":0}
    cities[city]["population"] += population
    cities[city]["gold"] += gold
    command = input()
command = input()
while command != "End":
    actions = command.split("=>")
    if actions[0] == "Plunder":
        town,peoples,gold = actions[1],int(actions[2]),int(actions[3])
        cities[town]["population"] -= peoples
        cities[town]["gold"] -= gold
        print(f"{town} plundered! {gold} gold stolen, {peoples} citizens killed.")
        if cities[town]["population"] <=0 or cities[town]["gold"] <= 0:
            cities.pop(town)
            print(f"{town} has been wiped off the map!")
    elif actions[0] == "Prosper":
        town,gold = actions[1],int(actions[2])
        if gold < 0:
            print("Gold added cannot be a negative number!")
        else:
            cities[town]["gold"] += gold
            print(f'{gold} gold added to the city treasury. {town} now has {cities[town]["gold"]} gold.')
    command = input()
cities = dict(sorted(cities.items(),key=lambda kvp:(-kvp[1]["gold"],kvp[0])))
if len(cities) == 0:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")
else:
    print(f"Ahoy, Captain! There are {len(cities)} wealthy settlements to go to:")
    for key,value in cities.items():
        print(f'{key} -> Population: {value["population"]} citizens, Gold: {value["gold"]} kg')