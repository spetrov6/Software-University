health = 100
bitcoins = 0
dungeons = input().split("|")
room_number = 0
a_life = True
for room in dungeons:
    room = room.split()
    room_number += 1
    command = room[0]
    points = int(room[1])
    if command == "potion":
        if health + points > 100:
            print(f"You healed for {100 - health} hp.")
            health = 100
        else:
            print(f"You healed for {points} hp.")
            health += points
        print(f"Current health: {health} hp.")
    elif command == "chest":
        bitcoins += points
        print(f"You found {points} bitcoins.")
    else:
        if health - points <= 0:
            a_life = False
            print(f"You died! Killed by {command}.")
            print(f"Best room: {room_number}")
            break
        else:
            health -= points
            print(f"You slayed {command}.")
if a_life:
    print(f"You've made it!\nBitcoins: {bitcoins}\nHealth: {health}")
