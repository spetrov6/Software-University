food_buy = int(input()) * 1000
command = input()
food_left = food_buy
while command != "Adopted":
    food = int(command)
    food_left -= food
    command = input()
if food_left >= 0:
    print(f"Food is enough! Leftovers: {food_left} grams.")
else:
    print(f"Food is not enough. You need {abs(food_left)} grams more.")