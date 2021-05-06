budged = int(input())
season = input()
fishman = int(input())
season_price = {"Spring": 3000, "Summer": 4200, "Autumn": 4200, "Winter": 2600}
for key,value in season_price.items():
    if season == key:
        if fishman <= 6 and fishman > 0 :
            price = value - (value * 0.10)
        elif fishman >=7 and fishman <= 11:
            price = value - (value * 0.15)
        elif fishman >= 12:
            price = value - (value * 0.25)
if season != "Autumn":
    if fishman % 2 == 0:
        price = price - (price * 0.05)

if budged >= price:
    print(f"Yes! You have {budged - price:0.2f} leva left.")
else:
    print(f"Not enough money! You need {price - budged:0.2f} leva.")