min_walks = int(input())
count_walks = int(input())
calories_day = int(input())
calories_burn = (min_walks * count_walks) * 5
if calories_burn >= calories_day / 2:
    print(f"Yes, the walk for your cat is enough. Burned calories per day: {calories_burn}.")
else:
    print(f"No, the walk for your cat is not enough. Burned calories per day: {calories_burn}.")