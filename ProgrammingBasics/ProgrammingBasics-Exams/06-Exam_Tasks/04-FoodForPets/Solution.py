days_count = int(input())
food_amount = float(input())
dog = 0
cat = 0
count = 0
biscuits = 0
for days in range(days_count):
    count += 1
    dog_food = int(input())
    cat_food = int(input())
    dog += dog_food
    cat += cat_food
    if count == 3:
        biscuits += (dog_food + cat_food) * 0.10
        count = 0
print(f"Total eaten biscuits: {int(biscuits)}gr.")
print(f"{((cat + dog) / food_amount) * 100:.2f}% of the food has been eaten.")
print(f"{(dog  / (dog + cat)) * 100:.2f}% eaten from the dog.")
print(f"{(cat / (dog + cat)) * 100:.2f}% eaten from the cat.")