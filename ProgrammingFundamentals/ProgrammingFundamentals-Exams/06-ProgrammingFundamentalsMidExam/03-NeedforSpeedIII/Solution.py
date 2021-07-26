number_of_cars = int(input())
cars_info = {}
for _ in range(number_of_cars):
    car,mileage,fuel = input().split("|")
    cars_info[car] = {"mileage":int(mileage),"fuel":int(fuel)}
command = input()
while command != "Stop":
    actions = command.split(" : ")
    if actions[0] == "Drive":
        car,distance,fuel = actions[1],int(actions[2]),int(actions[3])
        if fuel > cars_info[car]["fuel"]:
            print("Not enough fuel to make that ride")
        else:
            cars_info[car]["mileage"] += distance
            cars_info[car]["fuel"] -= fuel
            print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")
        if cars_info[car]["mileage"] >= 100000:
            cars_info.pop(car)
            print(f"Time to sell the {car}!")
    elif actions[0] == "Refuel":
        car,fuel = actions[1],int(actions[2])
        if cars_info[car]["fuel"] + fuel <= 75:
            cars_info[car]["fuel"] += fuel
            print(f"{car} refueled with {fuel} liters")
        else:
            print(f'{car} refueled with {75 - cars_info[car]["fuel"]} liters')
            cars_info[car]["fuel"] += 75 - cars_info[car]["fuel"]
    elif actions[0] == "Revert":
        car,km = actions[1],int(actions[2])
        if cars_info[car]["mileage"] - km < 10000:
            cars_info[car]["mileage"] = 10000
        else:
            cars_info[car]["mileage"] -= km
            print(f"{car} mileage decreased by {km} kilometers")
    command = input()
cars_info = dict(sorted(cars_info.items(),key=lambda kvp:(-kvp[1]["mileage"],kvp[0])))
for key,value in cars_info.items():
    print(f'{key} -> Mileage: {value["mileage"]} kms, Fuel in the tank: {value["fuel"]} lt.')