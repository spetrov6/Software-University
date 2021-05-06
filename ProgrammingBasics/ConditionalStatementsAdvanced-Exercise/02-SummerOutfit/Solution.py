degrees = int(input())
day_time = input()
if day_time == "Morning":
    if degrees >= 10 and degrees <= 18:
        Outfit = "Sweatshirt"
        Shoes = "Sneakers"
    elif degrees > 18 and degrees <= 24:
        Outfit = "Shirt"
        Shoes = "Moccasins"
    elif degrees >= 25:
        Outfit = "T-Shirt"
        Shoes = "Sandals"
elif day_time == "Afternoon":
    if degrees >= 10 and degrees <= 18:
        Outfit = "Shirt"
        Shoes = "Moccasins"
    elif degrees > 18 and degrees <= 24:
        Outfit = "T-Shirt"
        Shoes = "Sandals"
    elif degrees >= 25:
        Outfit = "Swim Suit"
        Shoes = "Barefoot"
else:
    Outfit = "Shirt"
    Shoes = "Moccasins"
print(f"It's {degrees} degrees, get your {Outfit} and {Shoes}.")