from math import floor,ceil
days = int(input())
food = int(input())
dog_food = float(input())
cat_food = float(input())
turtle_food = float(input()) / 1000
dog_total = dog_food * days
cat_total = cat_food * days
turtle_total = turtle_food * days
eaten_food = dog_total + cat_total + turtle_total
if food >= eaten_food:
    print(f"{floor(food - eaten_food)} kilos of food left.")
else:
    print(f"{ceil(eaten_food - food)} more kilos of food are needed.")
