houses = [int(i) for i in input().split("@")]
jump = input()
last_house = 0
success = False
fail_count = 0
while jump != "Love!":
    jump = jump.split()
    jump = int(jump[1])
    index = last_house + jump
    if index >= len(houses):
        index = 0
    if houses[index] - 2 == 0:
        houses[index] -= 2
        print(f"Place {index} has Valentine's day.")
    elif houses[index] - 2 > 0:
        houses[index] -= 2
    elif houses[index] - 2 < 0:
        print(f"Place {index} already had Valentine's day.")
    last_house = index
    jump = input()
print(f"Cupid's last position was {last_house}.")
if sum(houses) == 0:
    success = True
else:
    for i in houses:
        if i > 0:
            fail_count += 1
if success:
    print("Mission was successful.")
else:
    print(f"Cupid has failed {fail_count} places.")