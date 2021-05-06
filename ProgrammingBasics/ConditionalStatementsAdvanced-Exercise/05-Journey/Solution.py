budged = float(input())
season = input()
price = 0
if budged > 1000:
    price = budged * 0.90
    print("Somewhere in Europe"f"\nHotel - {price:.2f}")
elif 100 < budged <= 1000:
    if season == "summer":
        price = budged * 0.40
        print("Somewhere in Balkans"f"\nCamp - {price:.2f}")
    else:
        price = budged * 0.80
        print("Somewhere in Balkans"f"\nHotel - {price:.2f}")
else:
    if season == "summer":
        price = budged * 0.30
        print("Somewhere in Bulgaria"f"\nCamp - {price:.2f}")
    else:
        price = budged * 0.70
        print("Somewhere in Bulgaria"f"\nHotel - {price:.2f}")


