money = float(input())
gender = input()
age = int(input())
sport = input()
price = 0
if gender == "m":
    if sport == "Gym":
        price = 42
    elif sport == "Boxing":
        price = 41
    elif sport == "Yoga":
        price = 45
    elif sport == "Zumba":
        price = 34
    elif sport == "Dances":
        price = 51
    else:
        price = 39
else:
    if sport == "Gym":
        price = 35
    elif sport == "Boxing":
        price = 37
    elif sport == "Yoga":
        price = 42
    elif sport == "Zumba":
        price = 31
    elif sport == "Dances":
        price = 53
    else:
        price = 37
if age <= 19:
    price -= price * 0.20
if money >= price:
    print(f"You purchased a 1 month pass for {sport}.")
else:
    print(f"You don't have enough money! You need ${price - money:.2f} more.")