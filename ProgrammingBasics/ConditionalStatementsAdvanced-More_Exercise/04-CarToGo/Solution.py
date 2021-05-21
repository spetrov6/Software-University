budget = float(input())
season = input()
if budget <= 100:
    classe = "Economy class"
    if season == "Summer":
        car = "Cabrio"
        price = budget * 0.35
    else:
        car = "Jeep"
        price = budget * 0.65
elif 100 < budget <= 500:
    classe = "Compact class"
    if season == "Summer":
        car = "Cabrio"
        price = budget * 0.45
    else:
        car = "Jeep"
        price = budget * 0.80
elif budget > 500:
    classe = "Luxury class"
    car = "Jeep"
    price = budget * 0.90
print(f"{classe}"f"\n{car} - {price:.2f}")