day_events = input().split("|")
energy = 100
coins = 100
successful = True
for index in range(len(day_events)):
    day_events[index] = day_events[index].split("-")
    event = day_events[index][0]
    amount = int(day_events[index][1])
    if event == "rest":
        if energy + amount <= 100:
            energy += amount
            print(f"You gained {amount} energy."f"\nCurrent energy: {energy}.")
        else:
            print(f"You gained {100 - energy} energy.")
            energy += 100 - energy
            print(f"Current energy: {energy}.")
    elif event == "order":
        if energy >= 30:
            coins += amount
            energy -= 30
            print(f"You earned {amount} coins.")
        else:
            energy += 50
            print("You had to rest!")
    else:
        if coins > amount:
            coins -= amount
            print(f"You bought {event}.")
        else:
            print(f"Closed! Cannot afford {event}.")
            successful = False
            break
if successful:
    print("Day completed!"f"\nCoins: {coins}"f"\nEnergy: {energy}")