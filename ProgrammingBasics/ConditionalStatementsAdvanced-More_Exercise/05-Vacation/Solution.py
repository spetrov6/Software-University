budget = float(input())
season = input()
if budget <= 1000:
    place = "Camp"
    if season == "Summer":
        location = "Alaska"
        price = budget * 0.65
    else:
        location = "Morocco"
        price = budget * 0.45
elif 1000 < budget <= 3000:
    place = "Hut"
    if season == "Summer":
        location = "Alaska"
        price = budget * 0.80
    else:
        location = "Morocco"
        price = budget * 0.60
else:
    price = budget * 0.90
    place = "Hotel"
    if season == "Summer":
        location = "Alaska"
    else:
        location = "Morocco"
print(f"{location} - {place} - {price:.2f}")